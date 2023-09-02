from pathlib import Path

import pandas
import streamlit as st
from hackathon_submission.conf import dbPath, hideSidebarCSS, pageState
from hackathon_submission.schemas.sql import SQL
from pandas import DataFrame
from streamlit_extras.switch_page_button import switch_page

HEADER: str = f"""# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic

## {st.session_state["username"]}'s Portal
"""

def main() -> None:
    st.set_page_config(**pageState)
    st.markdown(**hideSidebarCSS)

    st.write(HEADER)
    
    col1, _, col2, col3 = st.columns(spec=[1,1,1,1], gap="small")

    with col1:
        logoutButton = st.button(label="Logout")
        if logoutButton:
            st.session_state["username"] = None
            switch_page(page_name="Login")

    with col2:
        newSymptomsButton = st.button(label="New Symptoms")
    with col3:
        talkToDoctorButton = st.button(label="Talk to an AI Doctor")

    st.divider()

    col1, col2, col3, = st.columns(spec=[1,1,1], gap="large")
    
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
        receiving_unsterile_injections = st.checkbox(label="Receiving unsterile injections")
        coma = st.checkbox(label="Coma")
        stomach_bleeding = st.checkbox(label="Stomach bleeding")
        distention_of_abdomen = st.checkbox(label="Distention of abdomen")
        history_of_alcohol_consumption = st.checkbox(label="History of alcohol consumption")
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


if __name__ == "__main__":
    main()
