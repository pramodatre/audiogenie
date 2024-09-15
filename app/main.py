import os
from typing import Union

from fastapi import FastAPI

app = FastAPI()

from TTS.api import TTS


tts = TTS(model_path="/app/app/tts_models--multilingual--multi-dataset--xtts_v2", config_path="/app/app/tts_models--multilingual--multi-dataset--xtts_v2/config.json", progress_bar=False, gpu=False)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/tts")
def run_tts(text: str = None):
    tts.tts_to_file(text=text, 
                    file_path="output.wav",
                    speaker_wav="/app/app/voices/Training+Voices.mp3",
                    language="en")

    return {"text": "Conversion complete!"}

@app.get("/tts_files")
def list_tts_files():
    result = os.listdir("/app/app/tts_models--multilingual--multi-dataset--xtts_v2")
    return {"text": str(result)}