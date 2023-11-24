import spacy
import os
import re
import shutil  # You need to import shutil for file copying

nlp = spacy.load("en_core_web_sm")

path = '/home/mukesh/Tensorflow/MDR_Rampup/Gmail/attachments/**Diabetes Health Report**'

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            print(file_path)

            health_report_path = file_path

            # Read the content of the health report file
            with open(health_report_path, "r", encoding="utf-8") as file:
                health_report_content = file.read()

            # Define a regular expression pattern to find the patient's name
            name_pattern = re.compile(r"Name: ([^\n]+)")

            # Search for the pattern in the health report content
            match = name_pattern.search(health_report_content)

            # Check if a match is found
            if match:
                # Extract and print the patient's name
                patient_name = match.group(1)
                name = patient_name.lower()
                if patient_name == "Mukesh":
                    # Specify the folder where you want to save the file
                    save_folder = "/home/mukesh/Tensorflow/MDR_Rampup/Gmail/attachments/**Diabetes Health Report**/med_report"

                    # Create the save folder if it doesn't exist
                    if not os.path.exists(save_folder):
                        os.makedirs(save_folder)

                    # Construct the new file path in the save folder
                    new_file_path = os.path.join(save_folder, os.path.basename(health_report_path))

                    # Copy the original file to the new location
                    shutil.copy(health_report_path, new_file_path)

                    print("File saved in:", new_file_path)
                else:
                    print("Patient name does not match.")
            else:
                print("Patient name not found.")
