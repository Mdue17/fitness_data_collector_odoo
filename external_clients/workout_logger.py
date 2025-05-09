import requests
from datetime import datetime

gender_input = input("Gender (1 = Male, 2 = Female): ")
gender = "male" if gender_input == "1" else "female"

# Ask the user for date of birth
dob = input("Date of Birth (YYYY-MM-DD): ")

params = {
    "session_name": input("Session name: "),
    "heart_rate": int(input("AVG heart rate: ")),
    "calories": int(input("Calories burned: ")),
    "duration": int(input("Duration (min): ")),
    "session_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    "date_of_birth": dob,
    "gender": gender
}

data = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": params,
    "id": 1
}

response = requests.post("http://localhost:8069/fitness/api/session", json=data, auth=('admin', 'admin'))
print("Status:", response.status_code)
print("Response:", response.text)