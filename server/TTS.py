import os
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

from dotenv import load_dotenv
load_dotenv()

apikey = os.getenv("IBM_API_KEY")
url = 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/f8e49087-0afd-49b2-adc8-e448a5d04495'

authenticator = IAMAuthenticator(apikey)
TextToSpeech = TextToSpeechV1(authenticator=authenticator)
TextToSpeech.set_service_url(url)

def tts(text):
    text = [line.replace('\n','') for line in text]
    text = ''.join(str(line) for line in text)

    with open('./data/audio_res.mp3', 'wb') as audio_file:
        res = TextToSpeech.synthesize(text, accept='audio/mp3', voice='en-US_HenryV3Voice').get_result()
        audio_file.write(res.content)