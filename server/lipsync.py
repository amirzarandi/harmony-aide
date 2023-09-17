import os
import requests

from dotenv import load_dotenv
load_dotenv()

def LipSync(video, audio):
    payload = {
        "input_face": video,
        "input_audio": audio,
    }

    response = requests.post(
        "https://api.gooey.ai/v2/Lipsync/",
        headers={
            "Authorization": "Bearer " + os.environ["GOOEY_API_KEY"],
        },
        json=payload,
    )
    assert response.ok, response.content

    result = response.json()
    print(video, audio)
    print(result['output']['output_video'])
    return result['output']['output_video']

if __name__ == '__main__':
    LipSync("https://storage.googleapis.com/palliative-ai/video.mp4", "https://storage.googleapis.com/palliative-ai/voice.wav")