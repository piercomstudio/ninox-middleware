from fastapi import FastAPI
import requests
import os

app = FastAPI()

API_TOKEN = os.getenv("NINOX_API_TOKEN")
TEAM_ID = "DMgaGJbRZKFZcrGvb"
DATABASE_ID = "dpk1s9iqd6n6"

# ✅ Existujúce endpointy
@app.get("/get_tables")
def get_tables():
    url = f"https://api.ninox.com/v1/teams/{TEAM_ID}/databases/{DATABASE_ID}/tables"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()

@app.get("/get_table_data/{table_id}")
def get_table_data(table_id: str):
    url = f"https://api.ninox.com/v1/teams/{TEAM_ID}/databases/{DATABASE_ID}/tables/{table_id}/records"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()

# ✅ Nový endpoint na získanie surových dát z Ninox API
@app.get("/get_raw_tables")
def get_raw_tables():
    url = f"https://api.ninox.com/v1/teams/{TEAM_ID}/databases/{DATABASE_ID}/tables"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.text  # 🟢 Pošleme dáta bez úprav
