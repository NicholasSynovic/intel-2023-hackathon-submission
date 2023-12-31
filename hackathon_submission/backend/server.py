import time
from argparse import Namespace
from typing import Any, Literal

import pandas
from fastapi import FastAPI, File, UploadFile
from pandas import DataFrame, Series
from pydantic import BaseModel

from hackathon_submission.backend.inference import (cvInference, prepareData,
                                                    runInference)
from hackathon_submission.backend.utils import common
from hackathon_submission.schemas.sql import SQL

app: FastAPI = FastAPI()


class Reports:
    def __init__(
        self,
        username: str,
        reportTime: float,
        symptoms: str,
        prognosis1: str,
        probability1: str,
        prognosis2: str,
        probability2: str,
        prognosis3: str,
        probability3: str,
        prognosis4: str,
        probability4: str,
        prognosis5: str,
        probability5: str,
        image: str,
    ) -> None:
        self.data: dict = {
            "Username": [username],
            "Report Time": [reportTime],
            "Symptoms": [symptoms],
            "Prognosis 1": [prognosis1],
            "Prognosis 2": [prognosis2],
            "Prognosis 3": [prognosis3],
            "Prognosis 4": [prognosis4],
            "Prognosis 5": [prognosis5],
            "Probability 1": [probability1],
            "Probability 2": [probability2],
            "Probability 3": [probability3],
            "Probability 4": [probability4],
            "Probability 5": [probability5],
            "Image": [image],
        }

    def to_df(self) -> DataFrame:
        df: DataFrame = DataFrame(data=self.data)
        return df


class ReportData(BaseModel):
    username: str
    symptoms: str
    reportTime: float
    type_: str
    Prognosis: list
    Probability: list
    image: str


class SymptomStr(BaseModel):
    message: str
    username: str


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


class DeleteReport(BaseModel):
    uuid: str


def getUsersTable() -> DataFrame:
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)
    df: DataFrame = pandas.read_sql_table(table_name="Users", con=sql.conn)
    sql.closeConnection()
    return df


def getReportsTable() -> DataFrame:
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)

    try:
        df: DataFrame = pandas.read_sql_table(table_name="Reports", con=sql.conn)
    except ValueError:
        df: DataFrame = DataFrame()
    except KeyError:
        df: DataFrame = DataFrame()
    df.index.name = "ID"

    sql.closeConnection()
    return df


def getImagesTable() -> DataFrame:
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)

    try:
        df: DataFrame = pandas.read_sql_table(table_name="Images", con=sql.conn)
    except ValueError:
        df: DataFrame = DataFrame()
    except KeyError:
        df: DataFrame = DataFrame()
    df.index.name = "ID"

    sql.closeConnection()
    return df


def predictFromImage(username: str, image: bytes) -> None:
    prediction: list = list(cvInference.main(imageBytes=image))

    if prediction == [1, 0]:
        prognosis = "Ill"
    if prediction == [0, 1]:
        prognosis = "Normal"

    from ast import literal_eval

    print(type(str(image)))
    print(type(literal_eval(str(image))))

    reportData: ReportData = ReportData(
        username=username,
        symptoms="X-Ray Photo",
        reportTime=time.time(),
        type_="cv",
        Prognosis=[prognosis, "", "", "", ""],
        Probability=["", "", "", "", ""],
        image=str(image),
    )
    createReport(fpReportData=reportData)


def usernameExists(username: str, df: DataFrame) -> bool:
    return username in df["Username"].values


def checkPassword(username: str, password: str, df: DataFrame) -> bool:
    row: Any = df[df["Username"] == username]

    if row["Password"].to_list()[0] == password:
        return True
    return False


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

    foo: DataFrame = DataFrame(data={"Username": [username], "Password": [password]})

    bar: DataFrame = pandas.concat(objs=[df, foo], ignore_index=True)

    sql.writeDFToDB(df=bar, tableName="Users", keepIndex=False)
    sql.closeConnection()

    return {"username": username}


@app.post(path="/api/inference/nlp/preprocess")
def preprocessData(data: Symptoms) -> dict:
    row: Series = Series(data.__dict__)
    message: str = prepareData.to_symptoms_string(row=row)
    return {"message": message}


@app.post(path="/api/inference/nlp/prognosis")
def inferencePrognosis(data: SymptomStr) -> dict:
    df: DataFrame = DataFrame(data={"symptoms": [data.message]})

    FLAGS: Namespace = Namespace(
        batch_size=1,
        benchmark_mode=False,
        bf16=True,
        input_file=df,
        intel=True,
        is_inc_int8=False,
        logfile="",
        n_runs=100,
        saved_model_dir=common.NLP_MODEL_PATH,
        seq_length=512,
    )

    predictions: list = runInference.main(flags=FLAGS)

    pairs: dict[str, float] = predictions[0]["prognosis"]

    formattedPairs: dict[str, Any] = {
        "username": data.username,
        "symptoms": data.message,
        "reportTime": time.time(),
        "type_": "nlp",
        "Prognosis": [],
        "Probability": [],
    }

    prognosis: str
    for prognosis in pairs.keys():
        formattedPairs["Prognosis"].append(prognosis)
        formattedPairs["Probability"].append(str(pairs[prognosis] * 100) + "%")

    return formattedPairs


@app.post(path="/api/generate/report")
def createReport(fpReportData: ReportData) -> None:
    reportsDF: DataFrame = getReportsTable()
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)

    if fpReportData.type_ == "nlp":
        foo: dict = {
            "username": fpReportData.username,
            "reportTime": fpReportData.reportTime,
            "symptoms": fpReportData.symptoms,
            "prognosis1": fpReportData.Prognosis[0],
            "prognosis2": fpReportData.Prognosis[1],
            "prognosis3": fpReportData.Prognosis[2],
            "prognosis4": fpReportData.Prognosis[3],
            "prognosis5": fpReportData.Prognosis[4],
            "probability1": fpReportData.Probability[0],
            "probability2": fpReportData.Probability[1],
            "probability3": fpReportData.Probability[2],
            "probability4": fpReportData.Probability[3],
            "probability5": fpReportData.Probability[4],
            "image": "",
        }

    if fpReportData.type_ == "cv":
        foo: dict = {
            "username": fpReportData.username,
            "reportTime": fpReportData.reportTime,
            "symptoms": fpReportData.symptoms,
            "prognosis1": fpReportData.Prognosis[0],
            "prognosis2": fpReportData.Prognosis[1],
            "prognosis3": fpReportData.Prognosis[2],
            "prognosis4": fpReportData.Prognosis[3],
            "prognosis5": fpReportData.Prognosis[4],
            "probability1": fpReportData.Probability[0],
            "probability2": fpReportData.Probability[1],
            "probability3": fpReportData.Probability[2],
            "probability4": fpReportData.Probability[3],
            "probability5": fpReportData.Probability[4],
            "image": fpReportData.image,
        }

    nlpReport: Reports = Reports(**foo)
    nlpDF: DataFrame = nlpReport.to_df()
    nlpDF.index.name = "ID"

    df: DataFrame = pandas.concat(
        objs=[reportsDF, nlpDF],
        ignore_index=True,
    )

    sql.writeDFToDB(df=df, tableName="Reports", keepIndex=False)
    sql.closeConnection()


@app.get(path="/api/storage/report")
def getReport(username: str) -> dict:
    df: DataFrame = getReportsTable()
    try:
        userSpecificDF: DataFrame = df[df["Username"] == username].iloc[::-1]
        userSpecificDF.reset_index(drop=True, inplace=True)
        data: dict = userSpecificDF.to_dict()
        data["Image"] = str(data["Image"])
        return data
    except KeyError:
        return {}


@app.delete(path="/api/storage/deleteReports")
def deleteReports(uuid: str) -> None:
    df: DataFrame = getReportsTable()
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)
    df = df[df["Username"] != uuid]
    df.reset_index(drop=True, inplace=True)
    sql.writeDFToDB(df=df, tableName="Reports", keepIndex=False)
    sql.closeConnection()


@app.delete(path="/api/account/delete")
def deleteAccount(username: str) -> None:
    deleteReports(uuid=username)
    df: DataFrame = getUsersTable()
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)
    df = df[df["Username"] != username]
    df.reset_index(drop=True, inplace=True)
    sql.writeDFToDB(df=df, tableName="Users", keepIndex=False)
    sql.closeConnection()


@app.post(path="/api/storage/upload")
async def uploadImage(username: str, file: UploadFile = File(...)) -> None:
    imagesDF: DataFrame = getImagesTable()
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)
    bar = await file.read()
    df: DataFrame = DataFrame(
        data={"Useranme": [username], "Image Data": [bar]},
    )
    df.index.name = "ID"
    foo: DataFrame = pandas.concat(objs=[imagesDF, df])
    sql.writeDFToDB(df=foo, tableName="Images", keepIndex=False)
    sql.closeConnection()

    predictFromImage(username=username, image=bar)


@app.get(path="/api/storage/download/reports")
def downloadReports(username: str) -> dict:
    df: DataFrame = getReportsTable()
    try:
        userSpecificDF: DataFrame = df[df["Username"] == username].iloc[::-1]
        userSpecificDF.reset_index(drop=True, inplace=True)
        data: dict = userSpecificDF.to_dict()
        data["Image"] = str(data["Image"])
        return data
    except KeyError:
        return {}


@app.get(path="/api/account/changeUsername")
def changeUsername(username: str, newUsername: str) -> None:
    df: DataFrame = getUsersTable()
    df["Username"] = df["Username"].str.replace(username, newUsername)
    common.writeDataToTable(df=df, tableName="Users")
