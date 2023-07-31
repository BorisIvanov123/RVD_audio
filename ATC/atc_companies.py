from google.cloud import texttospeech
from pydub import AudioSegment
import os

# Create a client
client = texttospeech.TextToSpeechClient()

# Company Names
companies = ['Lufthansa', 'Speedbird','Air France', 'Turkish', 'Qatari', 'Austrian', 'Ryanair', 'Wizz Air', 'Flying Bulgaria', 'KLM']

def create_audio(text, filename):
    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

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
    with open(filename + ".mp3", "wb") as out:
        out.write(response.audio_content)

    # Load TTS audio
    tts_audio = AudioSegment.from_mp3(filename + ".mp3")

    # Load background audio (replace 'background.mp3' with your actual file)
    background_audio = AudioSegment.from_mp3("components/test.mp3")

    # Overlay the two audio files
    combined = tts_audio.overlay(background_audio)

    # Export to mp3
    combined.export("atc_companies_audios/" + filename + "_combined.mp3", format='mp3')

# Create directory if it doesn't exist
if not os.path.exists('atc_companies_audios'):
    os.makedirs('atc_companies_audios')

# Generate audio files for each company
for company in companies:
    create_audio(company, company)
