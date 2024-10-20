import torch
from google.cloud import texttospeech
from transformers import pipeline

# Initialize text generation pipeline with GPT-2 model
pipe = pipeline("text-generation", model="openai-community/gpt2")
pipe("Hello, I am Jarvis. I am an AI assistant, how may I help you?")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Jarvis: Goodbye!")
        break
    
    # Generate AI response using the pipeline
    response = pipe(user_input)[0]['generated_text']
    print("Jarvis:", response)

#Text-to-Speech
client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text=response)
voice = texttospeech.VoiceSelectionParams(
    language_code='en-GB',
    name='en-GB-News-L',
    ssml_gender=texttospeech.SsmlVoiceGender.MALE,
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    request={
        'input': synthesis_input, 
        'voice' : voice, 
        'audio_config': audio_config
    }
)

with open('output.mp3', 'wb') as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
