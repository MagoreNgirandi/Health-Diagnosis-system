knowledge_base = {
    "disease 1: Diabetes": ["fatigue"],
    "disease 2: Hypertension": ["headaches"],
    "disease 3: Hyperthyroidism": ["weight loss"],
    "disease 4: Hypothyroidism": ["dry skin"],
    "disease 5: Bronchitis": ["coughing"],}
def diagnise_disease(symptoms):
    possible_diseases = ""
    for disease, disease_symptoms in knowledge_base.items():
        matching_symptoms = [symptom for symptom in symptoms if symptom in disease_symptoms]
        if len(matching_symptoms) == 1:
           print("")
    return possible_diseases
def main():
    print("Welcome to the Disease Diagnosis Centre")
    symptoms = input("Please enter your symptoms: ")
    symptoms = [symptom.strip().lower() for symptom in symptoms.split(",")]
    possible_diseases = diagnise_disease(symptoms)
    if possible_diseases:
        print("posible_diseases:")
        for disease in possible_diseases:
            print("possible_diseases")
    else:
        print("please visit nearest medical centre and see the Doctor")

if __name__ == "__main__":
    main()