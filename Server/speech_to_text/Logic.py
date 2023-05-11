import Server.speech_to_text.API as STT_Api

class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]


class Logic(Singleton):

    def __init__(cls):
        pass

    @staticmethod
    def parse_audio_to_txt(file_name):
        txt = STT_Api.parse_audio_to_text(file_name)
        return txt

