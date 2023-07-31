from google.cloud import texttospeech
from pydub import AudioSegment

# Create a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="Wizz Air!")

# Build the voice request
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.MALE,
)

# Select the type of audio file you want
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Write the response to the output file.
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)

# Load TTS audio
tts_audio = AudioSegment.from_mp3("output.mp3")

# Load background audio (replace 'background.mp3' with your actual file)
background_audio = AudioSegment.from_mp3("components/test.mp3")

# Overlay the two audio files
combined = tts_audio.overlay(background_audio)

# Export to mp3
combined.export("combined.mp3", format='mp3')
