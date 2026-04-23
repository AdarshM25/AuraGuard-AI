from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil

from video_utils import extract_frames
from hash_utils import generate_hashes
from compare import compare_hashes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend is working"}

@app.post("/compare/")
async def compare_videos(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    try:
        with open("v1.mp4", "wb") as f:
            shutil.copyfileobj(file1.file, f)

        with open("v2.mp4", "wb") as f:
            shutil.copyfileobj(file2.file, f)

        frames1 = extract_frames("v1.mp4")
        frames2 = extract_frames("v2.mp4")

        hashes1 = generate_hashes(frames1)
        hashes2 = generate_hashes(frames2)

        similarity = compare_hashes(hashes1, hashes2)

        return {
            "match_percentage": round(similarity, 2),
            "status": "Piracy Detected" if similarity > 50 else "Safe"
        }

    except Exception as e:
        print("ERROR:", e)
        return {"match_percentage": 0, "status": "Error"}