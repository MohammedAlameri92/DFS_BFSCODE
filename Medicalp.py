
# Medical Program to predicted the Diseas
def response(Reply):
    """
    Reads a character from the user and prints it.
    Args:
        Reply: The character entered by the user.
    """
    Reply = input()  # Use input() to read user input in Python
    print(Reply)

def symptom(Patient, indication):
    """
    Asks the user if the patient has a specific symptom.

    Args:
        Patient: The name of the patient.
        indication: The symptom to check.
    """
    Reply = input(f"Does {Patient} have a {indication} (y/n) ?")
    return Reply.lower() == 'y'  # Return True if the user enters 'y'

def hypotheses(Patient, Disease):
    """
    Checks if the patient's symptoms match the criteria for a specific disease.

    Args:
        Patient: The name of the patient.
        Disease: The disease to check.
    """
    if Disease == "measles":
        return {symptom(Patient, "fever") and symptom(Patient, "cough") 
        and symptom(Patient, "conjunctivitis")
        and symptom(Patient, "runny_nose") and symptom(Patient, "rash")}
    elif Disease == "german_measles":
        return {symptom(Patient, "fever") and symptom(Patient, "headache") 
        and symptom(Patient, "runny_nose") and symptom(Patient, "rash")}
    elif Disease == "flu":
        return { symptom(Patient, "fever") and symptom(Patient, "headache")
         and symptom(Patient, "body_ache") and symptom(Patient, "conjunctivitis")
         and symptom(Patient, "chills") and symptom(Patient, "sore_throat") 
         and symptom(Patient, "cough") and symptom(Patient, "runny_nose")}
    elif Disease == "common_cold":
        return {symptom(Patient, "headache") and symptom(Patient, "sneezing") 
        and symptom(Patient, "sore_throat") and symptom(Patient, "chills") 
        and symptom(Patient, "runny_nose")}
    elif Disease == "mumps":
        return symptom(Patient, "fever") and symptom(Patient, "swollen_glands")
    elif Disease == "chicken_pox":
        return {symptom(Patient, "fever") and symptom(Patient, "rash") 
        and symptom(Patient, "body_ache") and symptom(Patient, "chills")}
    elif Disease == "whooping_cough":
        return {symptom(Patient, "cough") and symptom(Patient, "sneezing") 
        and symptom(Patient, "runny_nose")}
    else:
        return False

def go():
    """
    The main function that runs the diagnosis process.
    """
    Patient = input("What is the patient’s name? ")
    for Disease in ["measles", "german_measles", "flu",
     "common_cold", "mumps", "chicken_pox", "whooping_cough"]:
        if hypotheses(Patient, Disease):
            print(f"{Patient} probably has {Disease}")
            return
    print("Sorry, I don’t seem to be able to diagnose the disease.")

if __name__ == "__main__":
    go()
    