from typing import Any, Literal
from pandas import Series
from argparse import Namespace

import pandas
from fastapi import FastAPI
from hackathon_submission.backend.utils import common
from hackathon_submission.schemas.sql import SQL
from pandas import DataFrame
from hackathon_submission.backend.inference import prepareData
from pydantic import BaseModel
from hackathon_submission.backend.inference import runInference

app: FastAPI = FastAPI()

class SymptomStr(BaseModel):
    message: str

class Symptoms(BaseModel):
    abdominal_pain: int
    abnormal_menstruation: int
    acidity: int
    acute_liver_failure: int
    altered_sensorium: int
    anxiety: int
    back_pain: int
    belly_pain: int
    blackheads: int
    bladder_discomfort: int
    blister: int
    blood_in_sputum: int
    bloody_stool: int
    blurred_and_distorted_vision: int
    breathlessness: int
    brittle_nails: int
    bruising: int
    burning_micturition: int
    chest_pain: int
    chills: int
    cold_hands_and_feets: int
    coma: int
    congestion: int
    constipation: int
    continuous_feel_of_urine: int
    continuous_sneezing: int
    cough: int
    cramps: int
    dark_urine: int
    dehydration: int
    depression: int
    diarrhoea: int
    dischromic_patches: int
    distention_of_abdomen: int
    dizziness: int
    drying_and_tingling_lips: int
    enlarged_thyroid: int
    excessive_hunger: int
    extra_marital_contacts: int
    family_history: int
    fast_heart_rate: int
    fatigue: int
    fluid_overload: int
    foul_smell_of_urine: int
    headache: int
    high_fever: int
    hip_joint_pain: int
    history_of_alcohol_consumption: int
    increased_appetite: int
    indigestion: int
    inflammatory_nails: int
    internal_itching: int
    irregular_sugar_level: int
    irritability: int
    irritation_in_anus: int
    itching: int
    joint_pain: int
    knee_pain: int
    lack_of_concentration: int
    lethargy: int
    loss_of_appetite: int
    loss_of_balance: int
    loss_of_smell: int
    malaise: int
    mild_fever: int
    mood_swings: int
    movement_stiffness: int
    mucoid_sputum: int
    muscle_pain: int
    muscle_wasting: int
    muscle_weakness: int
    nausea: int
    neck_pain: int
    nodal_skin_eruptions: int
    obesity: int
    pain_behind_the_eyes: int
    pain_during_bowel_movements: int
    pain_in_anal_region: int
    painful_walking: int
    palpitations: int
    passage_of_gases: int
    patches_in_throat: int
    phlegm: int
    polyuria: int
    prominent_veins_on_calf: int
    puffy_face_and_eyes: int
    pus_filled_pimples: int
    receiving_blood_transfusion: int
    receiving_unsterile_injections: int
    red_sore_around_nose: int
    red_spots_over_body: int
    redness_of_eyes: int
    restlessness: int
    runny_nose: int
    rusty_sputum: int
    scurring: int
    shivering: int
    silver_like_dusting: int
    sinus_pressure: int
    skin_peeling: int
    skin_rash: int
    slurred_speech: int
    small_dents_in_nails: int
    spinning_movements: int
    spotting_urination: int
    stiff_neck: int
    stomach_bleeding: int
    stomach_pain: int
    sunken_eyes: int
    sweating: int
    swelled_lymph_nodes: int
    swelling_joints: int
    swelling_of_stomach: int
    swollen_blood_vessels: int
    swollen_extremeties: int
    swollen_legs: int
    throat_irritation: int
    toxic_look_typhos: int
    ulcers_on_tongue: int
    unsteadiness: int
    visual_disturbances: int
    vomiting: int
    watering_from_eyes: int
    weakness_in_limbs: int
    weakness_of_one_body_side: int
    weight_gain: int
    weight_loss: int
    yellow_crust_ooze: int
    yellow_urine: int
    yellowing_of_eyes: int
    yellowish_skin: int


def getUsersTable() -> DataFrame:
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)
    df: DataFrame = pandas.read_sql_table(table_name="Users", con=sql.conn)
    sql.closeConnection()
    return df


def usernameExists(username: str, df: DataFrame) -> bool:
    return username in df["Username"].values


def checkPassword(username: str, password: str, df: DataFrame) -> bool:
    row: Any = df[df["Username"] == username]

    if row["Password"].to_list()[0] == password:
        return True
    return False


@app.get(path="/")
def check() -> Literal[True]:
    return True


@app.post(path="/api/account/login")
def login(username: str, password: str) -> bool:
    username = username.lower()
    df: DataFrame = getUsersTable()

    userExists: bool = usernameExists(username=username, df=df)
    if userExists:
        return checkPassword(username=username, password=password, df=df)
    return False


@app.post(path="/api/account/logout")
def logout() -> Literal[True]:
    return True


@app.post(path="/api/account/signup")
def signup(username: str, password: str) -> dict:
    username = username.lower()
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)
    df: DataFrame = getUsersTable()

    userExists: bool = usernameExists(username=username, df=df)
    if userExists:
        return {"username": False}

    df.set_index("index", inplace=True)
    df = df.append(
        other={"Username": username, "Password": password},
        ignore_index=True,
    )

    sql.writeDFToDB(df=df, tableName="Users", keepIndex=True)
    sql.closeConnection()

    return {"username": username}

@app.post(path="/api/inference/preprocess")
def preprocessData(data: Symptoms)    ->  dict:
    row: Series = Series(data)
    message: str = prepareData.to_symptoms_string(row=row)
    return {"message": message} 


@app.post(path="/api/inference/prognosis")
def inferencePrognosis(data: SymptomStr) -> dict:
    df: DataFrame = DataFrame(data={"symptoms": data.message})
    
    FLAGS: Namespace = Namespace(
            batch_size=1,
            benchmark_mode=False,
            bf16=True,
            input_file=df,
            intel=True,
            is_inc_int8=False,
            logfile="",
            n_runs=100,
            saved_model_dir=common.MODEL_PATH,
            seq_length=512,
        )

    predictions: list = runInference.main(flags=FLAGS)
    pairs: dict[str, float] = predictions[0]["prognosis"]

    formattedPairs: dict[str, list] = {"Prognosis": [], "Probability": []}

    prognosis: str
    for prognosis in pairs.keys():
        formattedPairs["Prognosis"].append(prognosis)
        formattedPairs["Probability"].append(str(pairs[prognosis] * 100) + "%")

    return formattedPairs


@app.get(path="/api/storage/symptoms")
def getSymptoms() -> bool:
    pass


@app.get(path="/api/storage/prognosis")
def getPrognosis() -> bool:
    pass


@app.post(path="/api/generate/report")
def generateReport() -> bool:
    pass
