import openai, os

from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def stt(wav_path):
    audio_file= open(f"{wav_path}", "rb")
    transc = openai.Audio.transcribe("whisper-1", audio_file)
    return transc

# print(stt("server/audio_test.wav").text)
with open("server/data/extracted.txt","w") as f:
    f.write(stt("server/data/audio_ext.wav").text)
f.close()
