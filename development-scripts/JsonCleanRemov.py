import json
import os

# Function to clean and modify JSON data
def clean_json_data(json_data):
    # Load JSON data
    data = json.loads(json_data)

    # Clean the data by replacing unwanted characters
    cleaned_data = json.dumps(data, ensure_ascii=False).replace("\\n", " ")

    # Load the cleaned JSON data back into a dictionary
    cleaned_data_dict = json.loads(cleaned_data)

    # Fields to remove
    fields_to_remove = ["submitter", "comments", "journal-ref", "doi", "report-no", "license", "versions"]

    # Remove unwanted fields
    for field in fields_to_remove:
        if field in cleaned_data_dict:
            del cleaned_data_dict[field]

    return cleaned_data_dict

# Function to check if the file path exists
def check_file_path(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return file_path

# Read JSON data from file
cwd = os.getcwd()
print(cwd)
input_file_path = check_file_path(f'{cwd}/input.json')
output_file_path = f'{cwd}/output.json'
log_file_path = f'{cwd}/log.txt'

cleaned_json_list = []
n = 0

# Open log file for writing
with open(log_file_path, 'w',encoding='utf-8') as log_file:
    with open(input_file_path, 'r',encoding='utf-8') as file:
        for line in file:
            n += 1
            # Check if the line is a valid JSON object
            line = line.strip()
            if line.startswith("{") and line.endswith("}"):
                try:
                    cleaned_json = clean_json_data(line)
                    cleaned_json_list.append(cleaned_json)
                except json.JSONDecodeError as e:
                    log_file.write(f"Error in line: {n} {e}\n")
                    #print(f"Error decoding JSON: {e}\n")
            if (n%10000  == 0):
                log_file.write(f"Processed: {n} lines\n")
                print(f"Processed: {n} lines\n")

# Write cleaned JSON data to output file as a JSON array
with open(output_file_path, 'w',encoding='utf-8') as file:
    json.dump(cleaned_json_list, file, indent=4, ensure_ascii=False)

# # Print the cleaned JSON data to log file
# with open(log_file_path, 'a') as log_file:
#     for cleaned_json in cleaned_json_list:
#         log_file.write(json.dumps(cleaned_json, indent=4, ensure_ascii=False) + "\n")
