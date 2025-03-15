from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import requests

app = FastAPI()  # ✅ Toto musí byť na začiatku!

TEAM_ID = "TVOJE_TEAM_ID"
DATABASE_ID = "TVOJE_DATABASE_ID"
API_TOKEN = "TVOJ_API_TOKEN"

@app.get("/get_tables")
def get_tables():
    url = f"https://api.ninox.com/v1/teams/{TEAM_ID}/databases/{DATABASE_ID}/tables"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    return JSONResponse(content=json.loads(json.dumps(data, ensure_ascii=False)), media_type="application/json; charset=utf-8")

@app.get("/get_table_data/{table_id}")
def get_table_data(table_id: str):
    url = f"https://api.ninox.com/v1/teams/{TEAM_ID}/databases/{DATABASE_ID}/tables/{table_id}/records"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    return JSONResponse(content=json.loads(json.dumps(data, ensure_ascii=False)), media_type="application/json; charset=utf-8")
