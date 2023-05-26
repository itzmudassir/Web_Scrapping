import pandas as pd

# Read the text file
with open('ok.txt', 'r') as file:
    lines = file.readlines()

# Create empty lists to store diseases and symptoms
diseases = []
symptoms = []

# Extract diseases and symptoms from each line
for line in lines:
    data = line.strip().split(':')
    if len(data) == 2:  # Check if the line contains both disease and symptom
        disease = data[0].strip()
        symptom_string = data[1].strip()
        symptom_list = [symptom.strip() for symptom in symptom_string.split(',')]
        diseases.append(disease)
        symptoms.append(symptom_list)

# Get the maximum number of symptoms for any disease
max_symptoms = max(len(symptom_list) for symptom_list in symptoms)

# Create column names for symptoms
symptom_columns = [f"Symptom {i+1}" for i in range(max_symptoms)]

# Create a DataFrame using pandas
data = {'Disease': diseases}
for i, column in enumerate(symptom_columns):
    data[column] = [symptom_list[i] if len(symptom_list) > i else '' for symptom_list in symptoms]

df = pd.DataFrame(data)

# Save DataFrame to an Excel file
df.to_excel('diseases.xlsx', index=False)
