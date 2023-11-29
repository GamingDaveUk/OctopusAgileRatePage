import json
from datetime import datetime

def get_current_value_inc_vat(json_file_path):
    # Load JSON data from the file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Get the current date and time
    current_datetime = datetime.now()

    # Iterate through the "results" list to find the corresponding "value_inc_vat"
    for result in data['results']:
        valid_from = datetime.strptime(result['valid_from'], "%Y-%m-%dT%H:%M:%SZ")
        valid_to = datetime.strptime(result['valid_to'], "%Y-%m-%dT%H:%M:%SZ")

        # Check if the current time is within the valid range
        if valid_from <= current_datetime <= valid_to:
            return result['value_inc_vat']

    # If no matching time range is found, return None or an appropriate value
    return None

# Example usage with the file path
json_file_path = 'data.json'
current_value_inc_vat = get_current_value_inc_vat(json_file_path)

# Print or use the result
print("Current value_inc_vat:", current_value_inc_vat)
