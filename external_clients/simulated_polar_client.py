import requests
import random
from datetime import datetime

params = {
    "session_name": f"Training {datetime.now().strftime('%Y-%m-%d %H:%M')}",
    "heart_rate": random.randint(80, 140),
    "calories": random.randint(100, 500),
    "duration": random.randint(10, 60),
    "session_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    "date_of_birth": "1995-08-15",
    "gender": "male",
}

# Wrap in JSON-RPC structure
data = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": params,
    "id": 1
}
response = requests.post("http://localhost:8069/fitness/api/session", json=data, auth=('admin', 'admin'))

print("Status:", response.status_code)
print("Response:", response.text)