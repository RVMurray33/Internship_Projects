import torch
from google.cloud import texttospeech
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Jarvis: Goodbye!")
        break
    
    # Tokenize and encode the input text with attention_mask
    input_ids = tokenizer.encode('int', return_tensors='pt', max_length=512, truncation=True)
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long, device=input_ids.device)

    # Generate text using the model with attention_mask
    output = model.generate(input_ids=input_ids, 
                        max_length=50, 
                        num_return_sequences=1,
                        attention_mask=attention_mask,
                        pad_token_id=tokenizer.eos_token_id)
    
    # Decode the generated output to text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    
    print("Jarvis:", generated_text)

#Text-to-Speech
client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text=generated_text)
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
