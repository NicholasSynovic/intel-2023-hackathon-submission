from argparse import Namespace

import streamlit as st
from pandas import DataFrame
from streamlit_extras.switch_page_button import switch_page

from hackathon_submission.frontend.utils import api, common

MESSAGE: str = f"""## {st.session_state["username"]}'s Symptoms

Please select all relevant symptoms, then press "Submit Symptoms" at the bottom
of this page.
"""


def main() -> None:
    st.set_page_config(**common.SITE_STATE)
    st.markdown(**common.HIDDEN_SIDEBAR_CSS)

    st.write(common.PAGE_HEADER)
    st.write(MESSAGE)

    (
        col1,
        col2,
        col3,
    ) = st.columns(spec=[1, 1, 1], gap="large")

    with col1:
        abdominal_pain = st.checkbox(label="Abdominal pain")
        abnormal_menstruation = st.checkbox(label="Abnormal menstruation")
        acidity = st.checkbox(label="Acidity")
        acute_liver_failure = st.checkbox(label="Acute liver failure")
        altered_sensorium = st.checkbox(label="Altered sensorium")
        anxiety = st.checkbox(label="Anxiety")
        back_pain = st.checkbox(label="Back pain")
        belly_pain = st.checkbox(label="Belly pain")
        blackheads = st.checkbox(label="Blackheads")
        bladder_discomfort = st.checkbox(label="Bladder discomfort")
        blister = st.checkbox(label="Blister")
        blood_in_sputum = st.checkbox(label="Blood in sputum")
        bloody_stool = st.checkbox(label="Bloody stool")
        blurred_and_distorted_vision = st.checkbox(label="Blurred and distorted vision")
        breathlessness = st.checkbox(label="Breathlessness")
        brittle_nails = st.checkbox(label="Brittle nails")
        bruising = st.checkbox(label="Bruising")
        burning_micturition = st.checkbox(label="Burning micturition")
        chest_pain = st.checkbox(label="Chest pain")
        chills = st.checkbox(label="Chills")
        cold_hands_and_feets = st.checkbox(label="Cold hands and feets")
        coma = st.checkbox(label="Coma")
        congestion = st.checkbox(label="Congestion")
        constipation = st.checkbox(label="Constipation")
        continuous_feel_of_urine = st.checkbox(label="Continuous feel of urine")
        continuous_sneezing = st.checkbox(label="Continuous sneezing")
        cough = st.checkbox(label="Cough")
        cramps = st.checkbox(label="Cramps")
        dark_urine = st.checkbox(label="Dark urine")
        dehydration = st.checkbox(label="Dehydration")
        depression = st.checkbox(label="Depression")
        diarrhoea = st.checkbox(label="Diarrhoea")
        dischromic_patches = st.checkbox(label="Dischromic patches")
        distention_of_abdomen = st.checkbox(label="Distention of abdomen")
        dizziness = st.checkbox(label="Dizziness")
        drying_and_tingling_lips = st.checkbox(label="Drying and tingling lips")
        enlarged_thyroid = st.checkbox(label="Enlarged thyroid")
        excessive_hunger = st.checkbox(label="Excessive hunger")
        extra_marital_contacts = st.checkbox(label="Extra marital contacts")
        family_history = st.checkbox(label="Family history")
        fast_heart_rate = st.checkbox(label="Fast heart rate")
        fatigue = st.checkbox(label="Fatigue")
        fluid_overload = st.checkbox(label="Fluid overload")
        foul_smell_of_urine = st.checkbox(label="Foul smell of urine")

    with col2:
        headache = st.checkbox(label="Headache")
        high_fever = st.checkbox(label="High fever")
        hip_joint_pain = st.checkbox(label="Hip joint pain")
        history_of_alcohol_consumption = st.checkbox(
            label="History of alcohol consumption"
        )
        increased_appetite = st.checkbox(label="Increased appetite")
        indigestion = st.checkbox(label="Indigestion")
        inflammatory_nails = st.checkbox(label="Inflammatory nails")
        internal_itching = st.checkbox(label="Internal itching")
        irregular_sugar_level = st.checkbox(label="Irregular sugar level")
        irritability = st.checkbox(label="Irritability")
        irritation_in_anus = st.checkbox(label="Irritation in anus")
        itching = st.checkbox(label="Itching")
        joint_pain = st.checkbox(label="Joint pain")
        knee_pain = st.checkbox(label="Knee pain")
        lack_of_concentration = st.checkbox(label="Lack of concentration")
        lethargy = st.checkbox(label="Lethargy")
        loss_of_appetite = st.checkbox(label="Loss of appetite")
        loss_of_balance = st.checkbox(label="Loss of balance")
        loss_of_smell = st.checkbox(label="Loss of smell")
        malaise = st.checkbox(label="Malaise")
        mild_fever = st.checkbox(label="Mild fever")
        mood_swings = st.checkbox(label="Mood swings")
        movement_stiffness = st.checkbox(label="Movement stiffness")
        mucoid_sputum = st.checkbox(label="Mucoid sputum")
        muscle_pain = st.checkbox(label="Muscle pain")
        muscle_wasting = st.checkbox(label="Muscle wasting")
        muscle_weakness = st.checkbox(label="Muscle weakness")
        nausea = st.checkbox(label="Nausea")
        neck_pain = st.checkbox(label="Neck pain")
        nodal_skin_eruptions = st.checkbox(label="Nodal skin eruptions")
        obesity = st.checkbox(label="Obesity")
        pain_behind_the_eyes = st.checkbox(label="Pain behind the eyes")
        pain_during_bowel_movements = st.checkbox(label="Pain during bowel movements")
        pain_in_anal_region = st.checkbox(label="Pain in anal region")
        painful_walking = st.checkbox(label="Painful walking")
        palpitations = st.checkbox(label="Palpitations")
        passage_of_gases = st.checkbox(label="Passage of gases")
        patches_in_throat = st.checkbox(label="Patches in throat")
        phlegm = st.checkbox(label="Phlegm")
        polyuria = st.checkbox(label="Polyuria")
        prominent_veins_on_calf = st.checkbox(label="Prominent veins on calf")
        puffy_face_and_eyes = st.checkbox(label="Puffy face and eyes")
        pus_filled_pimples = st.checkbox(label="Pus filled pimples")
        receiving_blood_transfusion = st.checkbox(label="Receiving blood transfusion")

    with col3:
        receiving_unsterile_injections = st.checkbox(
            label="Receiving unsterile injections"
        )
        red_sore_around_nose = st.checkbox(label="Red sore around nose")
        red_spots_over_body = st.checkbox(label="Red spots over body")
        redness_of_eyes = st.checkbox(label="Redness of eyes")
        restlessness = st.checkbox(label="Restlessness")
        runny_nose = st.checkbox(label="Runny nose")
        rusty_sputum = st.checkbox(label="Rusty sputum")
        scurring = st.checkbox(label="Scurring")
        shivering = st.checkbox(label="Shivering")
        silver_like_dusting = st.checkbox(label="Silver like dusting")
        sinus_pressure = st.checkbox(label="Sinus pressure")
        skin_peeling = st.checkbox(label="Skin peeling")
        skin_rash = st.checkbox(label="Skin rash")
        slurred_speech = st.checkbox(label="Slurred speech")
        small_dents_in_nails = st.checkbox(label="Small dents in nails")
        spinning_movements = st.checkbox(label="Spinning movements")
        spotting_urination = st.checkbox(label="Spotting urination")
        stiff_neck = st.checkbox(label="Stiff neck")
        stomach_bleeding = st.checkbox(label="Stomach bleeding")
        stomach_pain = st.checkbox(label="Stomach pain")
        sunken_eyes = st.checkbox(label="Sunken eyes")
        sweating = st.checkbox(label="Sweating")
        swelled_lymph_nodes = st.checkbox(label="Swelled lymph nodes")
        swelling_joints = st.checkbox(label="Swelling joints")
        swelling_of_stomach = st.checkbox(label="Swelling of stomach")
        swollen_blood_vessels = st.checkbox(label="Swollen blood vessels")
        swollen_extremeties = st.checkbox(label="Swollen extremeties")
        swollen_legs = st.checkbox(label="Swollen legs")
        throat_irritation = st.checkbox(label="Throat irritation")
        toxic_look_typhos = st.checkbox(label="Toxic look (typhos)")
        ulcers_on_tongue = st.checkbox(label="Ulcers on tongue")
        unsteadiness = st.checkbox(label="Unsteadiness")
        visual_disturbances = st.checkbox(label="Visual disturbances")
        vomiting = st.checkbox(label="Vomiting")
        watering_from_eyes = st.checkbox(label="Watering from eyes")
        weakness_in_limbs = st.checkbox(label="Weakness in limbs")
        weakness_of_one_body_side = st.checkbox(label="Weakness of one body side")
        weight_gain = st.checkbox(label="Weight gain")
        weight_loss = st.checkbox(label="Weight loss")
        yellow_crust_ooze = st.checkbox(label="Yellow crust ooze")
        yellow_urine = st.checkbox(label="Yellow urine")
        yellowing_of_eyes = st.checkbox(label="Yellowing of eyes")
        yellowish_skin = st.checkbox(label="Yellowish skin")

    bottomCol1, bottomCol2, bottomCol3 = st.columns(spec=[1, 1, 1], gap="small")

    with bottomCol1:
        logoutButton = st.button(label="Logout")
        if logoutButton:
            common.logout()

    with bottomCol2:
        submitButton = st.button(label="Submit Symptoms")
        if submitButton:
            data: dict[str, int] = {
                "abdominal_pain": int(abdominal_pain),
                "abnormal_menstruation": int(abnormal_menstruation),
                "acidity": int(acidity),
                "acute_liver_failure": int(acute_liver_failure),
                "altered_sensorium": int(altered_sensorium),
                "anxiety": int(anxiety),
                "back_pain": int(back_pain),
                "belly_pain": int(belly_pain),
                "blackheads": int(blackheads),
                "bladder_discomfort": int(bladder_discomfort),
                "blister": int(blister),
                "blood_in_sputum": int(blood_in_sputum),
                "bloody_stool": int(bloody_stool),
                "blurred_and_distorted_vision": int(blurred_and_distorted_vision),
                "breathlessness": int(breathlessness),
                "brittle_nails": int(brittle_nails),
                "bruising": int(bruising),
                "burning_micturition": int(burning_micturition),
                "chest_pain": int(chest_pain),
                "chills": int(chills),
                "cold_hands_and_feets": int(cold_hands_and_feets),
                "coma": int(coma),
                "congestion": int(congestion),
                "constipation": int(constipation),
                "continuous_feel_of_urine": int(continuous_feel_of_urine),
                "continuous_sneezing": int(continuous_sneezing),
                "cough": int(cough),
                "cramps": int(cramps),
                "dark_urine": int(dark_urine),
                "dehydration": int(dehydration),
                "depression": int(depression),
                "diarrhoea": int(diarrhoea),
                "dischromic_patches": int(dischromic_patches),
                "distention_of_abdomen": int(distention_of_abdomen),
                "dizziness": int(dizziness),
                "drying_and_tingling_lips": int(drying_and_tingling_lips),
                "enlarged_thyroid": int(enlarged_thyroid),
                "excessive_hunger": int(excessive_hunger),
                "extra_marital_contacts": int(extra_marital_contacts),
                "family_history": int(family_history),
                "fast_heart_rate": int(fast_heart_rate),
                "fatigue": int(fatigue),
                "fluid_overload": int(fluid_overload),
                "foul_smell_of_urine": int(foul_smell_of_urine),
                "headache": int(headache),
                "high_fever": int(high_fever),
                "hip_joint_pain": int(hip_joint_pain),
                "history_of_alcohol_consumption": int(history_of_alcohol_consumption),
                "increased_appetite": int(increased_appetite),
                "indigestion": int(indigestion),
                "inflammatory_nails": int(inflammatory_nails),
                "internal_itching": int(internal_itching),
                "irregular_sugar_level": int(irregular_sugar_level),
                "irritability": int(irritability),
                "irritation_in_anus": int(irritation_in_anus),
                "itching": int(itching),
                "joint_pain": int(joint_pain),
                "knee_pain": int(knee_pain),
                "lack_of_concentration": int(lack_of_concentration),
                "lethargy": int(lethargy),
                "loss_of_appetite": int(loss_of_appetite),
                "loss_of_balance": int(loss_of_balance),
                "loss_of_smell": int(loss_of_smell),
                "malaise": int(malaise),
                "mild_fever": int(mild_fever),
                "mood_swings": int(mood_swings),
                "movement_stiffness": int(movement_stiffness),
                "mucoid_sputum": int(mucoid_sputum),
                "muscle_pain": int(muscle_pain),
                "muscle_wasting": int(muscle_wasting),
                "muscle_weakness": int(muscle_weakness),
                "nausea": int(nausea),
                "neck_pain": int(neck_pain),
                "nodal_skin_eruptions": int(nodal_skin_eruptions),
                "obesity": int(obesity),
                "pain_behind_the_eyes": int(pain_behind_the_eyes),
                "pain_during_bowel_movements": int(pain_during_bowel_movements),
                "pain_in_anal_region": int(pain_in_anal_region),
                "painful_walking": int(painful_walking),
                "palpitations": int(palpitations),
                "passage_of_gases": int(passage_of_gases),
                "patches_in_throat": int(patches_in_throat),
                "phlegm": int(phlegm),
                "polyuria": int(polyuria),
                "prominent_veins_on_calf": int(prominent_veins_on_calf),
                "puffy_face_and_eyes": int(puffy_face_and_eyes),
                "pus_filled_pimples": int(pus_filled_pimples),
                "receiving_blood_transfusion": int(receiving_blood_transfusion),
                "receiving_unsterile_injections": int(receiving_unsterile_injections),
                "red_sore_around_nose": int(red_sore_around_nose),
                "red_spots_over_body": int(red_spots_over_body),
                "redness_of_eyes": int(redness_of_eyes),
                "restlessness": int(restlessness),
                "runny_nose": int(runny_nose),
                "rusty_sputum": int(rusty_sputum),
                "scurring": int(scurring),
                "shivering": int(shivering),
                "silver_like_dusting": int(silver_like_dusting),
                "sinus_pressure": int(sinus_pressure),
                "skin_peeling": int(skin_peeling),
                "skin_rash": int(skin_rash),
                "slurred_speech": int(slurred_speech),
                "small_dents_in_nails": int(small_dents_in_nails),
                "spinning_movements": int(spinning_movements),
                "spotting_urination": int(spotting_urination),
                "stiff_neck": int(stiff_neck),
                "stomach_bleeding": int(stomach_bleeding),
                "stomach_pain": int(stomach_pain),
                "sunken_eyes": int(sunken_eyes),
                "sweating": int(sweating),
                "swelled_lymph_nodes": int(swelled_lymph_nodes),
                "swelling_joints": int(swelling_joints),
                "swelling_of_stomach": int(swelling_of_stomach),
                "swollen_blood_vessels": int(swollen_blood_vessels),
                "swollen_extremeties": int(swollen_extremeties),
                "swollen_legs": int(swollen_legs),
                "throat_irritation": int(throat_irritation),
                "toxic_look_typhos": int(toxic_look_typhos),
                "ulcers_on_tongue": int(ulcers_on_tongue),
                "unsteadiness": int(unsteadiness),
                "visual_disturbances": int(visual_disturbances),
                "vomiting": int(vomiting),
                "watering_from_eyes": int(watering_from_eyes),
                "weakness_in_limbs": int(weakness_in_limbs),
                "weakness_of_one_body_side": int(weakness_of_one_body_side),
                "weight_gain": int(weight_gain),
                "weight_loss": int(weight_loss),
                "yellow_crust_ooze": int(yellow_crust_ooze),
                "yellow_urine": int(yellow_urine),
                "yellowing_of_eyes": int(yellowing_of_eyes),
                "yellowish_skin": int(yellowish_skin),
            }

            symptoms: str = api.preprocess(data=data)

            st.write(symptoms)

            with bottomCol3:
                with st.spinner("Predicting prognosis..."):
                    api.prognosis(
                        message=symptoms,
                        username=st.session_state["username"],
                    )
                    switch_page(page_name="report")

    st.write(common.PAGE_FOOTER)
    st.divider()


if __name__ == "__main__":
    main()
