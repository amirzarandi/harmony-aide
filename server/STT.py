import openai

def stt(wav_path):
    openai.api_key="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"
    audio_file= open(f"{wav_path}", "rb")
    transc = openai.Audio.transcribe("whisper-1", audio_file)
    print(transc)
    return transc

stt("server/audio_test.wav")