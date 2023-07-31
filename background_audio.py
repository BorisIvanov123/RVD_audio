from gtts import gTTS
from pydub import AudioSegment
import numpy as np
from scipy.io.wavfile import write, read
from scipy.signal import butter, lfilter

### Sound Effect ###
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def create_audio(text, filename, audio_type):
    tts = gTTS(text)
    tts.save(filename + '.mp3')
    
    if audio_type == 'ATC':
        sound = AudioSegment.from_file(filename + '.mp3', format="mp3")

        # Convert mp3 to wav for processing
        sound.export(filename + '.wav', format="wav")

        # Read wav file
        rate, data = read(filename + '.wav')

        # Generate white noise
        noise = np.random.normal(size=data.shape)

        # Convert data type to int16 to avoid overflow and underflow
        noise = (noise * np.iinfo(np.int16).max).astype(np.int16)

        # Add white noise to data
        data_with_noise = data + noise

        # Apply band pass filter
        data_with_noise_and_filter = butter_bandpass_filter(data_with_noise, 300.0, 3000.0, rate)

        # Write back to wav file
        write(filename + '.wav', rate, data_with_noise_and_filter.astype(np.int16))

        # Convert wav back to mp3
        sound_with_noise_and_filter = AudioSegment.from_file(filename + '.wav', format="wav")
        
        # Reduce bit rate to simulate signal degradation
        sound_with_noise_and_filter = sound_with_noise_and_filter.apply_gain(-20)  # Reduce volume by 10 dB
        sound_with_noise_and_filter.export(filename + '.mp3', format="mp3", bitrate="64k")

create_audio('This is a test', 'test', 'ATC')

### END OF CODE of audio effect ###