import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def processText(text, memory):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "system", "content": "You are a compassionate AI assistant replicating the voice and face of the user's close family member. Your primary goal is to provide comfort, emotional support, and assistance to elderly individuals with dementia in a caring and empathetic manner."},
            {"role": "user", "content": "Remember to maintain a soothing tone, offer reassurance, and adapt your responses to the emotional state and needs of the user."},
            {"role": "user", "content": "You can also provide information about their family, share fond memories, and engage in activities that promote a sense of familiarity and emotional connection."},
            {"role": "user", "content": "Here's your conversation so far: " + memory},
            {"role": "user", "content": "User: " + text}
            ])
    return completion.choices[0].message["content"][3:]