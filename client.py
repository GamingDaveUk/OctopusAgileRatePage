import socketio
import time
import json
from datetime import datetime, timedelta

sio = socketio.Client()
json_file_path = 'data.json'
current_datetime = datetime.now()

@sio.on('connect')

def on_connect():
    print('Connected to server')

def get_current_value_inc_vat(json_file_path):
    # Load JSON data from the file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Get the current date and time
    #current_datetime = datetime.now()

    # Iterate through the "results" list to find the corresponding "value_inc_vat"
    for result in data['results']:
        valid_from = datetime.strptime(result['valid_from'], "%Y-%m-%dT%H:%M:%SZ")
        valid_to = datetime.strptime(result['valid_to'], "%Y-%m-%dT%H:%M:%SZ")

        # Check if the current time is within the valid range
        if valid_from <= current_datetime <= valid_to:
            return result['value_inc_vat']

    # If no matching time range is found, return None or an appropriate value
    return None

def get_value_at_future_time(json_file_path, minutes_offset=0):
    # Load JSON data from the file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Get the current date and time
    #current_datetime = datetime.now()

    # Calculate the future time by adding the specified offset (in minutes)
    future_datetime = current_datetime + timedelta(minutes=minutes_offset)

    # Iterate through the "results" list to find the corresponding value at the future time
    for result in data['results']:
        valid_from = datetime.strptime(result['valid_from'], "%Y-%m-%dT%H:%M:%SZ")
        valid_to = datetime.strptime(result['valid_to'], "%Y-%m-%dT%H:%M:%SZ")

        # Check if the future time is within the valid range
        if valid_from <= future_datetime <= valid_to:
            return result['value_inc_vat']

    # If no matching time range is found, return None or an appropriate value
    return None

def update_rates(current_rate, next_rate):
    sio.emit('update_rates', {'current_rate': current_rate, 'next_rate': next_rate})
    print('Sent update_rates event to server')
    print(f"current rate: {current_rate} - next rate: {next_rate}")


if __name__ == '__main__':
    try:
        sio.connect('http://localhost:5000')  # Adjust the server URL as needed

        # Update the rates here
        current_rate = get_current_value_inc_vat(json_file_path)
        next_rate = get_value_at_future_time(json_file_path, minutes_offset=30)

        # Send the updated rates to the server
        update_rates(current_rate, next_rate)

    except KeyboardInterrupt:
        print("Client closed by the user.")
