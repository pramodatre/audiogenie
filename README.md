# AudioGenie
AudioGenie uses Audio to deliver educational content

# Running AudioGenie
Docker compose is used to package AudioGenie. 

First, we need data that includes XTTS v2 model from coqui. Could not use the model by direct download using model name. Instead, the downloaded model weights are to be placed under `app/tts_models--multilingual--multi-dataset--xtts_v2`.

Second, we need voices to clone to be placed as audio files under `app/voices`.

Once the data files are placed, launch the following command to build the docker image.
```
docker compose build
```

To lauch the FastAPI service that wraps XTTS, run
```
docker compose up
```

Here is a request to initiate text to speech (TTS) conversion
```
http://0.0.0.0:8008/tts?text=Welcome to our audio journey into the fascinating world of relativity theory! I'm your host, Dr. Spacetime, and together we'll explore how Albert Einstein revolutionized our understanding of space, time, and the universe itself. Buckle up, because we're about to bend your mind!
``` 

If docker is running on CPU-only hardware, expect very slow conversion.