from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'oisr_bec4KsnkT7N3BfVhLKcQNZS6ZlQ6UE7OrdvXWFf'
url = 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/f8e49087-0afd-49b2-adc8-e448a5d04495'

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open('server/data/extracted.txt','r') as f:
    text = f.readlines()
f.close()

text = [line.replace('\n','') for line in text]

text = ''.join(str(line) for line in text)

with open('server/data/speech.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_HenryV3Voice').get_result()
    audio_file.write(res.content)