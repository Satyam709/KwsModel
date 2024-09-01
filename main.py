from fastapi import FastAPI, File, UploadFile, HTTPException
from pathlib import Path
import shutil
from typing import List
import os
from multilingual_kws import run

app = FastAPI()

@app.get('/')
def hello():
    return 'hello world'

@app.post("/store_audio_files")
async def store_audio_files(
    word:str,
    input_files: List[UploadFile] = File(...),
    additional_file: UploadFile = File(...)
):
    if len(input_files) != 5:
        raise HTTPException(status_code=400, detail="Exactly 5 files are required for the first directory")
    # Directory to store the 5 audio files
    audio_files_dir = Path("audio_files")
    audio_files_dir.mkdir(parents=True, exist_ok=True)
    
    
    
    file_names = []
    for input_file in input_files:
        # Create a new file name for the stored audio file
        output_file_name = f"stored_{input_file.filename}"
        output_file_path = audio_files_dir / output_file_name

        # Copy the input audio file to the new file
        with input_file.file as input_file_obj:
            with open(output_file_path, "wb") as output_file_obj:
                shutil.copyfileobj(input_file_obj, output_file_obj)

        file_names.append(output_file_name)
        
    
    # Directory to store the additional audio file
    additional_audio_dir = Path("additional_audio")
    additional_audio_dir.mkdir(parents=True, exist_ok=True)

    # Create a new file name for the additional audio file
    additional_file_name = f"additional_{additional_file.filename}"
    additional_file_path = additional_audio_dir / additional_file_name

    # Copy the additional audio file to the new file
    try:
        # Write the additional file to a new file
        with open(additional_file_path, "wb") as additional_file_obj:
            shutil.copyfileobj(additional_file.file, additional_file_obj)
    except Exception as e:
        return {"error": f"Failed to store additional file: {str(e)}"}

    os.chdir("./audio_files")
    contents = os.listdir()
    print(contents)
    
    out_dir = Path(f"./output/{word}")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    
    print(f"Training on {word}: \n")
    
    print("MODEL :")
    os.chdir(f"./output/{word}")
    
    
    
    
   
    run.train(
        keyword = word,
        samples_dir = "/multilingual_kws/audio_files",
        embedding = "/multilingual_kws/multilingual_context_73_0.8011/",
        unknown_words = "/multilingual_kws/",
        background_noise = "/multilingual_kws/_background_noise_",
        output = f"/multilingual_kws/output/{word}"
    )
    
    print("trained")
    
    return {
        "message": f"Audio files stored successfully {contents}!",
        "stored_files": file_names,
        "additional_file": additional_file_name
    }
