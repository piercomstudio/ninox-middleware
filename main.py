from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
import os

app = FastAPI()

API_TOKEN = os.getenv("NINOX_API_TOKEN")
TEAM_ID = "DMgaGJbRZKFZcrGvb"
DATABASE_ID = "dpk1s9iqd6n6"

# ✅ Endpoint na získanie zoznamu tabuliek
@app.get("/get_tables")
def get_tables():
    url = f"https://api.ninox.com/v1/teams/{TEAM_ID}/databases/{DATABASE_ID}/tables"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # Nastavíme správne kódovanie
    data = response.json()
    return JSONResponse(content=data, media_type="application/json; charset=utf-8")

# ✅ Endpoint na získanie dát z konkrétnej tabuľky podľa ID
@app.get("/get_table_data/{table_id}")
def get_table_data(table_id: str):
    url = f"https://api.ninox.com/v1/teams/{TEAM_ID}/databases/{DATABASE_ID}/tables/{table_id}/records"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # Nastavíme správne kódovanie
    data = response.json()
    return JSONResponse(content=data, media_type="application/json; charset=utf-8")
