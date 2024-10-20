from ai import decoded_output
from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text=decoded_output)
voice = texttospeech.VoiceSelectionParams(
    language_code='en-GB',
    name='en-GB-News-L',
    ssml_gender=texttospeech.SsmlVoiceGender.MALE,
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    request={'input': decoded_output, 'voice' : voice, 'audio_config': audio_config}
)
with open('output.mp3', 'wb') as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
synthetic_speech = texttospeech.sy
api_key = AIzaSyCI7m98MXhie_LST0su9YbDNlFvWim0Wqs