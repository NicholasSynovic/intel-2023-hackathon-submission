import time
from argparse import Namespace

import streamlit as st
from hackathon_submission.conf import dbPath, hideSidebarCSS, pageState
from hackathon_submission.schemas.sql import SQL
from hackathon_submission.utils import runInference
from hackathon_submission.utils.prepareData import to_symptoms_string
from pandas import DataFrame, Series
from streamlit_extras.switch_page_button import switch_page
import pandas

HEADER: str = f"""# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic

## {st.session_state["username"]}'s New Symptoms

Please select all relevant symptoms, then press "Submit Symptoms" at the bottom
of this page.
"""


def inference(data: DataFrame) -> None:
    FLAGS: Namespace = Namespace(
        batch_size=1,
        benchmark_mode=False,
        bf16=True,
        input_file=data,
        intel=True,
        is_inc_int8=False,
        logfile="",
        n_runs=100,
        saved_model_dir="model",
        seq_length=512,
    )

    predictions = runInference.main(flags=FLAGS)
    pairs: dict[str, float] = predictions[0]["prognosis"]

    foo: dict[str, list] = {"prognosis": [], "probability": []}

    prognosis: str
    for prognosis in pairs.keys():
        foo["prognosis"].append(prognosis)
        foo["probability"].append(pairs[prognosis])

    df: DataFrame = DataFrame(data=foo)

    print(df)


def main() -> None:
    st.set_page_config(**pageState)
    st.markdown(**hideSidebarCSS)

    st.write(HEADER)

    (
        col1,
        col2,
        col3,
    ) = st.columns(spec=[1, 1, 1], gap="large")

    with col1:
        itching = st.checkbox(label="Itching")
        skin_rash = st.checkbox(label="Skin rash")
        nodal_skin_eruptions = st.checkbox(label="Nodal skin eruptions")
        continuous_sneezing = st.checkbox(label="Continuous sneezing")
        shivering = st.checkbox(label="Shivering")
        chills = st.checkbox(label="Chills")
        joint_pain = st.checkbox(label="Joint pain")
        stomach_pain = st.checkbox(label="Stomach pain")
        acidity = st.checkbox(label="Acidity")
        ulcers_on_tongue = st.checkbox(label="Ulcers on tongue")
        muscle_wasting = st.checkbox(label="Muscle wasting")
        vomiting = st.checkbox(label="Vomiting")
        burning_micturition = st.checkbox(label="Burning micturition")
        spotting_urination = st.checkbox(label="Spotting urination")
        fatigue = st.checkbox(label="Fatigue")
        weight_gain = st.checkbox(label="Weight gain")
        anxiety = st.checkbox(label="Anxiety")
        cold_hands_and_feets = st.checkbox(label="Cold hands and feets")
        mood_swings = st.checkbox(label="Mood swings")
        weight_loss = st.checkbox(label="Weight loss")
        restlessness = st.checkbox(label="Restlessness")
        lethargy = st.checkbox(label="Lethargy")
        patches_in_throat = st.checkbox(label="Patches in throat")
        irregular_sugar_level = st.checkbox(label="Irregular sugar level")
        cough = st.checkbox(label="Cough")
        high_fever = st.checkbox(label="High fever")
        sunken_eyes = st.checkbox(label="Sunken eyes")
        breathlessness = st.checkbox(label="Breathlessness")
        sweating = st.checkbox(label="Sweating")
        dehydration = st.checkbox(label="Dehydration")
        indigestion = st.checkbox(label="Indigestion")
        headache = st.checkbox(label="Headache")
        yellowish_skin = st.checkbox(label="Yellowish skin")
        dark_urine = st.checkbox(label="Dark urine")
        nausea = st.checkbox(label="Nausea")
        loss_of_appetite = st.checkbox(label="Loss of appetite")
        pain_behind_the_eyes = st.checkbox(label="Pain behind the eyes")
        back_pain = st.checkbox(label="Back pain")
        constipation = st.checkbox(label="Constipation")
        abdominal_pain = st.checkbox(label="Abdominal pain")
        diarrhoea = st.checkbox(label="Diarrhoea")
        mild_fever = st.checkbox(label="Mild fever")
        yellow_urine = st.checkbox(label="Yellow urine")
        yellowing_of_eyes = st.checkbox(label="Yellowing of eyes")
        acute_liver_failure = st.checkbox(label="Acute liver failure")

    with col2:
        swelling_of_stomach = st.checkbox(label="Swelling of stomach")
        swelled_lymph_nodes = st.checkbox(label="Swelled lymph nodes")
        malaise = st.checkbox(label="Malaise")
        blurred_and_distorted_vision = st.checkbox(label="Blurred and distorted vision")
        phlegm = st.checkbox(label="Phlegm")
        throat_irritation = st.checkbox(label="Throat irritation")
        redness_of_eyes = st.checkbox(label="Redness of eyes")
        sinus_pressure = st.checkbox(label="Sinus pressure")
        runny_nose = st.checkbox(label="Runny nose")
        congestion = st.checkbox(label="Congestion")
        chest_pain = st.checkbox(label="Chest pain")
        weakness_in_limbs = st.checkbox(label="Weakness in limbs")
        fast_heart_rate = st.checkbox(label="Fast heart rate")
        pain_during_bowel_movements = st.checkbox(label="Pain during bowel movements")
        pain_in_anal_region = st.checkbox(label="Pain in anal region")
        bloody_stool = st.checkbox(label="Bloody stool")
        irritation_in_anus = st.checkbox(label="Irritation in anus")
        neck_pain = st.checkbox(label="Neck pain")
        dizziness = st.checkbox(label="Dizziness")
        cramps = st.checkbox(label="Cramps")
        bruising = st.checkbox(label="Bruising")
        obesity = st.checkbox(label="Obesity")
        swollen_legs = st.checkbox(label="Swollen legs")
        swollen_blood_vessels = st.checkbox(label="Swollen blood vessels")
        puffy_face_and_eyes = st.checkbox(label="Puffy face and eyes")
        enlarged_thyroid = st.checkbox(label="Enlarged thyroid")
        brittle_nails = st.checkbox(label="Brittle nails")
        swollen_extremeties = st.checkbox(label="Swollen extremeties")
        excessive_hunger = st.checkbox(label="Excessive hunger")
        extra_marital_contacts = st.checkbox(label="Extra marital contacts")
        drying_and_tingling_lips = st.checkbox(label="Drying and tingling lips")
        slurred_speech = st.checkbox(label="Slurred speech")
        knee_pain = st.checkbox(label="Knee pain")
        hip_joint_pain = st.checkbox(label="Hip joint pain")
        muscle_weakness = st.checkbox(label="Muscle weakness")
        stiff_neck = st.checkbox(label="Stiff neck")
        swelling_joints = st.checkbox(label="Swelling joints")
        movement_stiffness = st.checkbox(label="Movement stiffness")
        spinning_movements = st.checkbox(label="Spinning movements")
        loss_of_balance = st.checkbox(label="Loss of balance")
        unsteadiness = st.checkbox(label="Unsteadiness")
        weakness_of_one_body_side = st.checkbox(label="Weakness of one body side")
        loss_of_smell = st.checkbox(label="Loss of smell")
        bladder_discomfort = st.checkbox(label="Bladder discomfort")

    with col3:
        foul_smell_of_urine = st.checkbox(label="Foul smell of urine")
        continuous_feel_of_urine = st.checkbox(label="Continuous feel of urine")
        passage_of_gases = st.checkbox(label="Passage of gases")
        internal_itching = st.checkbox(label="Internal itching")
        toxic_look_typhos = st.checkbox(label="Toxic look (typhos)")
        depression = st.checkbox(label="Depression")
        irritability = st.checkbox(label="Irritability")
        muscle_pain = st.checkbox(label="Muscle pain")
        altered_sensorium = st.checkbox(label="Altered sensorium")
        red_spots_over_body = st.checkbox(label="Red spots over body")
        belly_pain = st.checkbox(label="Belly pain")
        abnormal_menstruation = st.checkbox(label="Abnormal menstruation")
        dischromic_patches = st.checkbox(label="Dischromic patches")
        watering_from_eyes = st.checkbox(label="Watering from eyes")
        increased_appetite = st.checkbox(label="Increased appetite")
        polyuria = st.checkbox(label="Polyuria")
        family_history = st.checkbox(label="Family history")
        mucoid_sputum = st.checkbox(label="Mucoid sputum")
        rusty_sputum = st.checkbox(label="Rusty sputum")
        lack_of_concentration = st.checkbox(label="Lack of concentration")
        visual_disturbances = st.checkbox(label="Visual disturbances")
        receiving_blood_transfusion = st.checkbox(label="Receiving blood transfusion")
        receiving_unsterile_injections = st.checkbox(
            label="Receiving unsterile injections"
        )
        coma = st.checkbox(label="Coma")
        stomach_bleeding = st.checkbox(label="Stomach bleeding")
        distention_of_abdomen = st.checkbox(label="Distention of abdomen")
        history_of_alcohol_consumption = st.checkbox(
            label="History of alcohol consumption"
        )
        fluid_overload = st.checkbox(label="Fluid overload")
        blood_in_sputum = st.checkbox(label="Blood in sputum")
        prominent_veins_on_calf = st.checkbox(label="Prominent veins on calf")
        palpitations = st.checkbox(label="Palpitations")
        painful_walking = st.checkbox(label="Painful walking")
        pus_filled_pimples = st.checkbox(label="Pus filled pimples")
        blackheads = st.checkbox(label="Blackheads")
        scurring = st.checkbox(label="Scurring")
        skin_peeling = st.checkbox(label="Skin peeling")
        silver_like_dusting = st.checkbox(label="Silver like dusting")
        small_dents_in_nails = st.checkbox(label="Small dents in nails")
        inflammatory_nails = st.checkbox(label="Inflammatory nails")
        blister = st.checkbox(label="Blister")
        red_sore_around_nose = st.checkbox(label="Red sore around nose")
        yellow_crust_ooze = st.checkbox(label="Yellow crust ooze")

    bottomCol1, bottomCol2 = st.columns(spec=[2, 2], gap="large")

    with bottomCol1:
        submitButton = st.button(label="Submit Symptoms")
        if submitButton:
            data: dict[str, int] = {
                "itching": int(itching),
                "skin_rash": int(skin_rash),
                "nodal_skin_eruptions": int(nodal_skin_eruptions),
                "continuous_sneezing": int(continuous_sneezing),
                "shivering": int(shivering),
                "chills": int(chills),
                "joint_pain": int(joint_pain),
                "stomach_pain": int(stomach_pain),
                "acidity": int(acidity),
                "ulcers_on_tongue": int(ulcers_on_tongue),
                "muscle_wasting": int(muscle_wasting),
                "vomiting": int(vomiting),
                "burning_micturition": int(burning_micturition),
                "spotting_ urination": int(spotting_urination),
                "fatigue": int(fatigue),
                "weight_gain": int(weight_gain),
                "anxiety": int(anxiety),
                "cold_hands_and_feets": int(cold_hands_and_feets),
                "mood_swings": int(mood_swings),
                "weight_loss": int(weight_loss),
                "restlessness": int(restlessness),
                "lethargy": int(lethargy),
                "patches_in_throat": int(patches_in_throat),
                "irregular_sugar_level": int(irregular_sugar_level),
                "cough": int(cough),
                "high_fever": int(high_fever),
                "sunken_eyes": int(sunken_eyes),
                "breathlessness": int(breathlessness),
                "sweating": int(sweating),
                "dehydration": int(dehydration),
                "indigestion": int(indigestion),
                "headache": int(headache),
                "yellowish_skin": int(yellowish_skin),
                "dark_urine": int(dark_urine),
                "nausea": int(nausea),
                "loss_of_appetite": int(loss_of_appetite),
                "pain_behind_the_eyes": int(pain_behind_the_eyes),
                "back_pain": int(back_pain),
                "constipation": int(constipation),
                "abdominal_pain": int(abdominal_pain),
                "diarrhoea": int(diarrhoea),
                "mild_fever": int(mild_fever),
                "yellow_urine": int(yellow_urine),
                "yellowing_of_eyes": int(yellowing_of_eyes),
                "acute_liver_failure": int(acute_liver_failure),
                "fluid_overload": int(fluid_overload),
                "swelling_of_stomach": int(swelling_of_stomach),
                "swelled_lymph_nodes": int(swelled_lymph_nodes),
                "malaise": int(malaise),
                "blurred_and_distorted_vision": int(blurred_and_distorted_vision),
                "phlegm": int(phlegm),
                "throat_irritation": int(throat_irritation),
                "redness_of_eyes": int(redness_of_eyes),
                "sinus_pressure": int(sinus_pressure),
                "runny_nose": int(runny_nose),
                "congestion": int(congestion),
                "chest_pain": int(chest_pain),
                "weakness_in_limbs": int(weakness_in_limbs),
                "fast_heart_rate": int(fast_heart_rate),
                "pain_during_bowel_movements": int(pain_during_bowel_movements),
                "pain_in_anal_region": int(pain_in_anal_region),
                "bloody_stool": int(bloody_stool),
                "irritation_in_anus": int(irritation_in_anus),
                "neck_pain": int(neck_pain),
                "dizziness": int(dizziness),
                "cramps": int(cramps),
                "bruising": int(bruising),
                "obesity": int(obesity),
                "swollen_legs": int(swollen_legs),
                "swollen_blood_vessels": int(swollen_blood_vessels),
                "puffy_face_and_eyes": int(puffy_face_and_eyes),
                "enlarged_thyroid": int(enlarged_thyroid),
                "brittle_nails": int(brittle_nails),
                "swollen_extremeties": int(swollen_extremeties),
                "excessive_hunger": int(excessive_hunger),
                "extra_marital_contacts": int(extra_marital_contacts),
                "drying_and_tingling_lips": int(drying_and_tingling_lips),
                "slurred_speech": int(slurred_speech),
                "knee_pain": int(knee_pain),
                "hip_joint_pain": int(hip_joint_pain),
                "muscle_weakness": int(muscle_weakness),
                "stiff_neck": int(stiff_neck),
                "swelling_joints": int(swelling_joints),
                "movement_stiffness": int(movement_stiffness),
                "spinning_movements": int(spinning_movements),
                "loss_of_balance": int(loss_of_balance),
                "unsteadiness": int(unsteadiness),
                "weakness_of_one_body_side": int(weakness_of_one_body_side),
                "loss_of_smell": int(loss_of_smell),
                "bladder_discomfort": int(bladder_discomfort),
                "foul_smell_of urine": int(foul_smell_of_urine),
                "continuous_feel_of_urine": int(continuous_feel_of_urine),
                "passage_of_gases": int(passage_of_gases),
                "internal_itching": int(internal_itching),
                "toxic_look_(typhos)": int(toxic_look_typhos),
                "depression": int(depression),
                "irritability": int(irritability),
                "muscle_pain": int(muscle_pain),
                "altered_sensorium": int(altered_sensorium),
                "red_spots_over_body": int(red_spots_over_body),
                "belly_pain": int(belly_pain),
                "abnormal_menstruation": int(abnormal_menstruation),
                "dischromic _patches": int(dischromic_patches),
                "watering_from_eyes": int(watering_from_eyes),
                "increased_appetite": int(increased_appetite),
                "polyuria": int(polyuria),
                "family_history": int(family_history),
                "mucoid_sputum": int(mucoid_sputum),
                "rusty_sputum": int(rusty_sputum),
                "lack_of_concentration": int(lack_of_concentration),
                "visual_disturbances": int(visual_disturbances),
                "receiving_blood_transfusion": int(receiving_blood_transfusion),
                "receiving_unsterile_injections": int(receiving_unsterile_injections),
                "coma": int(coma),
                "stomach_bleeding": int(stomach_bleeding),
                "distention_of_abdomen": int(distention_of_abdomen),
                "history_of_alcohol_consumption": int(history_of_alcohol_consumption),
                "fluid_overload": int(fluid_overload),
                "blood_in_sputum": int(blood_in_sputum),
                "prominent_veins_on_calf": int(prominent_veins_on_calf),
                "palpitations": int(palpitations),
                "painful_walking": int(painful_walking),
                "pus_filled_pimples": int(pus_filled_pimples),
                "blackheads": int(blackheads),
                "scurring": int(scurring),
                "skin_peeling": int(skin_peeling),
                "silver_like_dusting": int(silver_like_dusting),
                "small_dents_in_nails": int(small_dents_in_nails),
                "inflammatory_nails": int(inflammatory_nails),
                "blister": int(blister),
                "red_sore_around_nose": int(red_sore_around_nose),
                "yellow_crust_ooze": int(yellow_crust_ooze),
            }

            row: Series = Series(data=data)
            symptomStr: str = to_symptoms_string(row=row)
            df: DataFrame = DataFrame(data={"symptoms": [symptomStr]})

            with bottomCol2:
                with st.spinner("Predicting prognosis..."):
                    inference(data=df)
                switch_page(page_name="Report")

    st.divider()


if __name__ == "__main__":
    main()
