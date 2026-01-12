from fastapi import FastAPI, UploadFile, File
from app.schemas import DetectResponse
from app.services.detector import detect_symbols_mock

app = FastAPI(title="HVAC Symbol Backend (Mock)")



@app.post("/detect", response_model=DetectResponse)
async def detect(file: UploadFile = File(...)):
    # read file 
    content = await file.read()

    symbols = detect_symbols_mock(content, file.filename)
    

    return {
        "file_name": file.filename,
        "symbols": symbols
    }
