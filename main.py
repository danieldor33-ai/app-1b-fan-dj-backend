from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import datetime

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

state = {
    "current_song": "Song A",
    "end_time": datetime.datetime.utcnow().isoformat(),
    "song_index": 0
}

class SongState(BaseModel):
    current_song: str
    end_time: str
    song_index: int

@app.get("/get_state")
def get_state():
    return state

@app.post("/update_song")
def update_song(new_state: SongState):
    global state
    state = new_state.dict()
    return {"status": "updated"}
