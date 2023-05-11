import Server.speech_to_text.API as stt

if __name__ == "__main__":
    text = stt.parse_audio_to_text("C:/Users/amirk/Downloads/test.wav")
    print(text)