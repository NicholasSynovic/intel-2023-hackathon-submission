import pandas
import streamlit as st
from hackathon_submission.conf import dbPath, hideSidebarCSS, pageState
from hackathon_submission.schemas.sql import SQL
from pandas import DataFrame
from streamlit_extras.switch_page_button import switch_page

HEADER: str = f"""# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic

## {st.session_state["username"]}'s New Symptoms

Please select all relevant symptoms, then press "Submit Symptoms" at the bottom
of this page.
"""


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

    submitButton = st.button(label="Submit Symptoms")
    if submitButton:
        data: dict[str, bool] = {
            "itching": itching,
            "skin_rash": skin_rash,
            "nodal_skin_eruptions": nodal_skin_eruptions,
            "continuous_sneezing": continuous_sneezing,
            "shivering": shivering,
            "chills": chills,
            "joint_pain": joint_pain,
            "stomach_pain": stomach_pain,
            "acidity": acidity,
            "ulcers_on_tongue": ulcers_on_tongue,
            "muscle_wasting": muscle_wasting,
            "vomiting": vomiting,
            "burning_micturition": burning_micturition,
            "spotting_ urination": spotting_urination,
            "fatigue": fatigue,
            "weight_gain": weight_gain,
            "anxiety": anxiety,
            "cold_hands_and_feets": cold_hands_and_feets,
            "mood_swings": mood_swings,
            "weight_loss": weight_loss,
            "restlessness": restlessness,
            "lethargy": lethargy,
            "patches_in_throat": patches_in_throat,
            "irregular_sugar_level": irregular_sugar_level,
            "cough": cough,
            "high_fever": high_fever,
            "sunken_eyes": sunken_eyes,
            "breathlessness": breathlessness,
            "sweating": sweating,
            "dehydration": dehydration,
            "indigestion": indigestion,
            "headache": headache,
            "yellowish_skin": yellowish_skin,
            "dark_urine": dark_urine,
            "nausea": nausea,
            "loss_of_appetite": loss_of_appetite,
            "pain_behind_the_eyes": pain_behind_the_eyes,
            "back_pain": back_pain,
            "constipation": constipation,
            "abdominal_pain": abdominal_pain,
            "diarrhoea": diarrhoea,
            "mild_fever": mild_fever,
            "yellow_urine": yellow_urine,
            "yellowing_of_eyes": yellowing_of_eyes,
            "acute_liver_failure": acute_liver_failure,
            "fluid_overload": fluid_overload,
            "swelling_of_stomach": swelling_of_stomach,
            "swelled_lymph_nodes": swelled_lymph_nodes,
            "malaise": malaise,
            "blurred_and_distorted_vision": blurred_and_distorted_vision,
            "phlegm": phlegm,
            "throat_irritation": throat_irritation,
            "redness_of_eyes": redness_of_eyes,
            "sinus_pressure": sinus_pressure,
            "runny_nose": runny_nose,
            "congestion": congestion,
            "chest_pain": chest_pain,
            "weakness_in_limbs": weakness_in_limbs,
            "fast_heart_rate": fast_heart_rate,
            "pain_during_bowel_movements": pain_during_bowel_movements,
            "pain_in_anal_region": pain_in_anal_region,
            "bloody_stool": bloody_stool,
            "irritation_in_anus": irritation_in_anus,
            "neck_pain": neck_pain,
            "dizziness": dizziness,
            "cramps": cramps,
            "bruising": bruising,
            "obesity": obesity,
            "swollen_legs": swollen_legs,
            "swollen_blood_vessels": swollen_blood_vessels,
            "puffy_face_and_eyes": puffy_face_and_eyes,
            "enlarged_thyroid": enlarged_thyroid,
            "brittle_nails": brittle_nails,
            "swollen_extremeties": swollen_extremeties,
            "excessive_hunger": excessive_hunger,
            "extra_marital_contacts": extra_marital_contacts,
            "drying_and_tingling_lips": drying_and_tingling_lips,
            "slurred_speech": slurred_speech,
            "knee_pain": knee_pain,
            "hip_joint_pain": hip_joint_pain,
            "muscle_weakness": muscle_weakness,
            "stiff_neck": stiff_neck,
            "swelling_joints": swelling_joints,
            "movement_stiffness": movement_stiffness,
            "spinning_movements": spinning_movements,
            "loss_of_balance": loss_of_balance,
            "unsteadiness": unsteadiness,
            "weakness_of_one_body_side": weakness_of_one_body_side,
            "loss_of_smell": loss_of_smell,
            "bladder_discomfort": bladder_discomfort,
            "foul_smell_of urine": foul_smell_of_urine,
            "continuous_feel_of_urine": continuous_feel_of_urine,
            "passage_of_gases": passage_of_gases,
            "internal_itching": internal_itching,
            "toxic_look_(typhos)": toxic_look_typhos,
            "depression": depression,
            "irritability": irritability,
            "muscle_pain": muscle_pain,
            "altered_sensorium": altered_sensorium,
            "red_spots_over_body": red_spots_over_body,
            "belly_pain": belly_pain,
            "abnormal_menstruation": abnormal_menstruation,
            "dischromic _patches": dischromic_patches,
            "watering_from_eyes": watering_from_eyes,
            "increased_appetite": increased_appetite,
            "polyuria": polyuria,
            "family_history": family_history,
            "mucoid_sputum": mucoid_sputum,
            "rusty_sputum": rusty_sputum,
            "lack_of_concentration": lack_of_concentration,
            "visual_disturbances": visual_disturbances,
            "receiving_blood_transfusion": receiving_blood_transfusion,
            "receiving_unsterile_injections": receiving_unsterile_injections,
            "coma": coma,
            "stomach_bleeding": stomach_bleeding,
            "distention_of_abdomen": distention_of_abdomen,
            "history_of_alcohol_consumption": history_of_alcohol_consumption,
            "fluid_overload": fluid_overload,
            "blood_in_sputum": blood_in_sputum,
            "prominent_veins_on_calf": prominent_veins_on_calf,
            "palpitations": palpitations,
            "painful_walking": painful_walking,
            "pus_filled_pimples": pus_filled_pimples,
            "blackheads": blackheads,
            "scurring": scurring,
            "skin_peeling": skin_peeling,
            "silver_like_dusting": silver_like_dusting,
            "small_dents_in_nails": small_dents_in_nails,
            "inflammatory_nails": inflammatory_nails,
            "blister": blister,
            "red_sore_around_nose": red_sore_around_nose,
            "yellow_crust_ooze": yellow_crust_ooze,
        }
        st.divider()


if __name__ == "__main__":
    main()
