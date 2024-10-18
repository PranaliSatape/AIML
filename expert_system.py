def diagnose(answers):
    # Parse user answers
    fever = answers[0] == 'yes'
    sore_throat = answers[1] == 'yes'
    cough = answers[2] == 'yes'
    shortness_of_breath = answers[3] == 'yes'
    body_aches = answers[4] == 'yes'
    taste_smell_loss = answers[5] == 'yes'
    chills = answers[6] == 'yes'
    headache = answers[7] == 'yes'
    close_contact = answers[8] == 'yes'
    respiratory_history = answers[9] == 'yes'

    # Check conditions and return the diagnosis
    if fever and taste_smell_loss and close_contact:
        return 'Diagnosis: COVID-19 (High Risk)'

    if fever and cough and body_aches and chills:
        return 'Diagnosis: Influenza (Flu)'

    if cough and sore_throat and headache:
        return 'Diagnosis: Common Cold (Upper Respiratory Infection)'

    if headache and body_aches and no_respiratory_symptoms(fever, cough, shortness_of_breath):
        return 'Diagnosis: Tension Headache or Migraine'

    if shortness_of_breath and respiratory_history:
        return 'Diagnosis: Chronic Respiratory Condition (e.g., Asthma, COPD)'

    if close_contact and (fever or cough):
        return 'Diagnosis: COVID-19 Exposure (Monitor Symptoms Closely)'

    if sore_throat and cough:
        return 'Diagnosis: Acute Pharyngitis (Sore Throat Infection)'

    # Default case if no specific diagnosis is found
    return 'Diagnosis: Unknown (Consult a doctor for more information)'

def no_respiratory_symptoms(fever, cough, shortness_of_breath):
    return not (fever or cough or shortness_of_breath)
