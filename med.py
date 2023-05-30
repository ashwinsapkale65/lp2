# Define the symptoms and their corresponding treatments
symptoms_treatments = {
    'Flu': ['Drink hot water', 'Avoid cold eatables.'],
    'Yellowish eyes and skin': ['Put eye drops', 'Have healthy sleep, do not strain your eyes.'],
    'Dark color urine': ['Drink lots of water, juices, and eat fruits. Avoid alcohol consumption.'],
    'Pale bowel movement': ['Drink lots of water and exercise regularly.'],
    'Fatigue': ['Drink lots of water, juices, and eat fruits.'],
    'Vomiting': ['Drink salt and water.'],
    'Fever': ['Put a hot water cloth on the head and take Crocin.'],
    'Pain in joints': ['Apply painkiller and take Crocin.'],
    'Weakness': ['Drink salt and water, eat fruits.'],
    'Stomach Pain': ['Avoid outside food and eat fruits.']
}

# Define the diseases and their corresponding symptoms
diseases_symptoms = {
    'Hemochromatosis': ['Stomach Pain', 'Pain in joints', 'Weakness', 'Dark color urine', 'Yellowish eyes and skin'],
    'Hepatitis C': ['Pain in joints', 'Fever', 'Fatigue', 'Vomiting', 'Pale bowel movement'],
    'Hepatitis B': ['Pale bowel movement', 'Dark color urine', 'Yellowish eyes and skin'],
    'Hepatitis A': ['Flu', 'Yellowish eyes and skin'],
    'Jaundice': ['Yellowish eyes and skin'],
    'Flu': ['Flu']
}

# Get patient symptoms
patient_symptoms = []
for symptom in symptoms_treatments:
    answer = input(f"Does the patient have {symptom}? (yes/no): ")
    if answer.lower() == 'yes':
        patient_symptoms.append(symptom)

# Find possible diseases based on patient symptoms
possible_diseases = []
for disease, symptoms in diseases_symptoms.items():
    if all(symptom in patient_symptoms for symptom in symptoms):
        possible_diseases.append(disease)

# Print possible diseases
print("Possible diseases:")
for disease in possible_diseases:
    print(disease)

# Print advice for each symptom
print("\nAdvice:")
for symptom in patient_symptoms:
    if symptom != 'Stomach Pain':
        treatments = symptoms_treatments.get(symptom, [])
        if treatments:
            print(f"- {treatments[0]}")
            if len(treatments) > 1:
                print(f"  {treatments[1]}")

