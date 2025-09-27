# Install the assemblyai package by executing the command "pip install assemblyai"

import assemblyai as aai

aai.settings.api_key = ""

# audio_file = "./local_file.mp3"
audio_file = "audio.mp3"

config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.universal)

transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
  raise RuntimeError(f"Transcription failed: {transcript.error}")

print(transcript.text)