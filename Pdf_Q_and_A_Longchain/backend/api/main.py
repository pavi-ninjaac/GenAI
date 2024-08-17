"""
Contains the FastAPI server related codes.
"""
import sys

sys.path.insert(0, "/home/pavithra/projects/GenAI/Pdf_Q_and_A_Longchain/backend/")
sys.path.insert(0, "/home/pavithra/projects/GenAI/Pdf_Q_and_A_Longchain/backend/")

import os

import uvicorn
from api.schema import QuestionRequest, UploadPdfRequest
from core import constants, main, utils
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Ensure the data directory exists to upload the files.
if not os.path.exists(constants.DATA_FOLDER):
    os.makedirs(constants.DATA_FOLDER)

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload the file to the data directory.

    :param file: The file to upload.
    """
    # Delete the existing files in the directory.
    utils.delete_files_in_directory(constants.DATA_FOLDER)

    # Save the uploaded file in the data directory.
    file_location = os.path.join(constants.DATA_FOLDER, file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return JSONResponse(content={"filename": file.filename}, status_code=200)


@app.post("/ask-question/")
async def ask_question(request: QuestionRequest):
    """
    Generate the answer for the user question.
    """
    generated_answer = main.generate_answer(request.question)
    return JSONResponse(content={"answer": generated_answer})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
