from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
import os

app = FastAPI()

# Directories to store uploaded files
SAMPLES_DIR = "/uploaded_files/samples"
STREAM_AUDIO_DIR = "/uploaded_files/streamAudio"

os.makedirs(SAMPLES_DIR, exist_ok=True)
os.makedirs(STREAM_AUDIO_DIR, exist_ok=True)

@app.post("/train")
async def train(
    samples: List[UploadFile] = File(...),
):
    if len(samples) < 5:
        raise HTTPException(status_code=400, detail="Exactly 5 audio files are required")

    file_paths = []
    
    # Save each uploaded sample file
    for file in samples:
        file_path = os.path.join(SAMPLES_DIR, file.filename)
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        file_paths.append(file_path)
    
    return {"file_paths": file_paths}

@app.post("/analyze")
async def analyze(
    audio_file: UploadFile = File(...),
):
    file_path = os.path.join(STREAM_AUDIO_DIR, audio_file.filename)
    
    # Save the uploaded audio file
    with open(file_path, "wb") as f:
        content = await audio_file.read()
        f.write(content)
    
    return {"file_path": file_path}
