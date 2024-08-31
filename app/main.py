from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {'message': 'hello world'}


# @app.post("/store_audio_files")
# async def store_audio_files(
#     input_files: List[UploadFile] = File(...),
#     additional_file: UploadFile = File(...)
# ):
#     if len(input_files) != 5:
#         raise HTTPException(status_code=400, detail="Exactly 5 files are required for the first directory")

#     # Directory to store the 5 audio files
#     audio_files_dir = Path("audio_files")
#     audio_files_dir.mkdir(parents=True, exist_ok=True)

#     file_names = []
#     for input_file in input_files:
#         # Create a new file name for the stored audio file
#         output_file_name = f"stored_{input_file.filename}"
#         output_file_path = audio_files_dir / output_file_name

#         # Copy the input audio file to the new file
#         with input_file.file as input_file_obj:
#             with open(output_file_path, "wb") as output_file_obj:
#                 shutil.copyfileobj(input_file_obj, output_file_obj)

#         file_names.append(output_file_name)
    
#     # Directory to store the additional audio file
#     additional_audio_dir = Path("additional_audio")
#     additional_audio_dir.mkdir(parents=True, exist_ok=True)

#     # Create a new file name for the additional audio file
#     additional_file_name = f"additional_{additional_file.filename}"
#     additional_file_path = additional_audio_dir / additional_file_name

#     # Copy the additional audio file to the new file
#     with additional_file.file as additional_file_obj:
#         with open(additional_file_path, "wb") as additional_file_obj:
#             shutil.copyfileobj(additional_file_obj, additional_file_obj)

#     return {
#         "message": "Audio files stored successfully!",
#         "stored_files": file_names,
#         "additional_file": additional_file_name
#     }