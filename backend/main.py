#main, models are together
#database was from an earlier learning attempt
#upload was from the audio upload attempt

from fastapi import FastAPI
from models import Sounds, Spaces
import pymongo
app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome To FastAPI World"}
    db.fs.files.find( { filename: myFileName } ).sort( { uploadDate: 1 } )

    db.fs.chunks.find( { files_id: myFileID } ).sort( { n: 1 } )