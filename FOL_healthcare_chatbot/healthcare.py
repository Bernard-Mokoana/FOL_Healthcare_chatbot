knowledge_base = {
    "flu": {"fever", "cough", "sore throat"},
    "common cold": {"sneezing", "runny nose", "mild fever"},
    "malaria": {"fever", "chills", "sweating", "headache"},
    "covid19": {"fever", "cough", "shortness of breath", "loss of taste"},
    "strep throat": {"sore throat", "swollen lymph nodes", "fever"}
}

advice_base = {
    "flu": [
        "Drink fluids",
        "Rest",
        "Consult a doctor if symptoms worsen"
    ],
    "common cold": [
        "Stay warm",
        "Use saline nasal drops",
        "Drink hot tea with honey"
    ],
    "malaria": [
        "Take antimalarial medication",
        "Avoid mosquito bites",
        "Seek immediate medical attention"
    ],
    "covid19": [
        "Isolate yourself",
        "Wear a mask",
        "Get tested and monitor oxygen levels"
    ],
    "strep throat": [
        "Take prescribed antibiotics",
        "Gargle with warm salt water",
        "Avoid sharing utensils"
    ]
}


def match_diseases(user_symptoms):
    possible_diseases = []

    for disease, symptoms in knowledge_base.items():
        if symptoms.issubset(user_symptoms):
            possible_diseases.append(disease)
    
    return possible_diseases

def main():
    print("Welcome to the HealthBot!")
    print("Please enter your symptoms (comma-separated):")
    user_input = input("Symptoms: ")
    
    symptoms_input = {s.strip().lower() for s in user_input.split(",")}
    

    matched = match_diseases(symptoms_input)

    print("\nBased on your symptoms, you might have:")
    if matched:
        for disease in matched:
            print(f"- {disease.capitalize()}")
            for advice in advice_base[disease]:
                print(f"  Advice: {advice}")
    else:
        print("No disease matched exactly. Please consult a healthcare professional.")

if __name__ == "__main__":
    main()
