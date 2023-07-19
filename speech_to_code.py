import  openai
from openai import Completion
import time
import speech_recognition as sr
openai.api_key = ""
def speechtotext():
        r=sr.Recognizer()
        with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Please say Something")
                    audio=r.listen(source)
                    z=r.recognize_google(audio)
                    print(z)
                    return(z)
                    

def generate_text():
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=speechtotext(),
        max_tokens=2000,
        top_p=1,
        temperature=0,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text


generated_text = generate_text()
print(generated_text)


