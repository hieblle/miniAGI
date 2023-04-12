import requests

CHUNK_SIZE = 1024

XI_API_KEY = "fe948e1825744b2e25f9ac0a161d4698"

url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": XI_API_KEY
}

data = {
  "text": "Some very long text to be read by the voice",
  "voice_settings": {
    "stability": 0,
    "similarity_boost": 0
  }
}

with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
