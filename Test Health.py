 # Import necessary libraries
import tkinter as tk
from tkinter import messagebox

# Define the knowledge base
knowledge_base = {
    "Disease 1: Diabetes": ["excessive thirst", "frequent urination", "fatigue"],
    "Disease 2: Hypertension": ["headaches", "dizziness", "nosebleeds"],
    "Disease 3: Hyperthyroidism": ["weight loss", "rapid heartbeat", "nervousness"],
    "Disease 4: Hypothyroidism": ["weight gain", "fatigue", "dry skin"],
    "Disease 5: Bronchitis": ["coughing", "mucus production", "shortness of breath"]
}
# Define the inference mechanism
def diagnose_disease(symptoms):
    possible_diseases = []
    for disease, disease_symptoms in knowledge_base.items():
        matching_symptoms = [symptom for symptom in symptoms if symptom in disease_symptoms]
        if len(matching_symptoms) >= 2:  # adjust the threshold as needed
            possible_diseases.append(disease)
    return possible_diseases

# Define the user interface
def get_symptoms():
    symptoms = []
    if excessive_thirst.get():
        symptoms.append("excessive thirst")
    if frequent_urination.get():
        symptoms.append("frequent urination")
    if fatigue.get():
        symptoms.append("fatigue")
    if headaches.get():
        symptoms.append("headaches")
    if dizziness.get():
        symptoms.append("dizziness")
    if nosebleeds.get():
        symptoms.append("nosebleeds")
    if weight_loss.get():
        symptoms.append("weight loss")
    if rapid_heartbeat.get():
        symptoms.append("rapid heartbeat")
    if nervousness.get():
        symptoms.append("nervousness")
    if weight_gain.get():
        symptoms.append("weight gain")
    if dry_skin.get():
        symptoms.append("dry skin")
    if coughing.get():
        symptoms.append("coughing")
    if mucus_production.get():
        symptoms.append("mucus production")
    if shortness_of_breath.get():
        symptoms.append("shortness of breath")
    return symptoms

def diagnose():
    symptoms = get_symptoms()
    possible_diseases = diagnose_disease(symptoms)
    if possible_diseases:
        print = ("Possible diseases:\n")
        for disease in possible_diseases:
            print += (disease + "\n")
        messagebox.showinfo("Diagnosis", result)
    else:
             print("Di"Please Consult the Doctor")


