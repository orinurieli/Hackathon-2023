import speech_recognition as sr
import os
from pydub import AudioSegment


def parse_audio_to_text(audio_file_path):
    # Initialize the recognizer
    r = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        # Read the entire audio file
        audio = r.record(source)

        try:
            # Use the recognizer to convert speech to text
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Speech recognition could not understand audio."
        except sr.RequestError as e:
            return "Could not request results from Google Speech Recognition service; {0}".format(e)

def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    # Set the path to the ffmpeg executable
    ffmpeg_path = "path/to/ffmpeg/executable"  # Replace with the actual path

    # Set the environment variable for ffmpeg
    os.environ["PATH"] += os.pathsep + ffmpeg_path
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export(wav_file_path, format='wav')

