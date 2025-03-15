from fastapi import FastAPI
import requests
import os

app = FastAPI()

# Skrytý API token (bude v Environment Variables na Render.com)
API_TOKEN = os.getenv("NINOX_API_TOKEN")

# ✅ Tvoje správne Ninox ID
TEAM_ID = "DMgaGJbRZKFZcrGvb"
DATABASE_ID = "dpk1s9iqd6n6"

# 🟢 Endpoint na získanie zoznamu tabuliek
@app.get("/get_tables")
def get_tables():
    url = f"https://api.ninox.com/v1/teams/{TEAM_ID}/databases/{DATABASE_ID}/tables"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()

# 🟢 Endpoint na získanie dát z konkrétnej tabuľky podľa jej ID
@app.get("/get_table_data/{table_id}")
def get_table_data(table_id: str):
    url = f"https://api.ninox.com/v1/teams/{TEAM_ID}/databases/{DATABASE_ID}/tables/{table_id}/records"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()
