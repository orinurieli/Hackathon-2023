import Server.open_ai.API as Gpt_api

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
    def generate_solution(database, issue):
        text = f"I am going to send you a history of a calls center that were resolved in json format." \
                 f" :\n{database}\n\n" \
                 f"I need your help to resolve another issue based on the previous data.\n" \
                 f"Add short suggestions by your experience in new field.\n" \
                 f"The solution fields must base on the data above.\n" \
                 f"Before your solution, summarize the issue and give a short solution in the above template.\n" \
                 f"Do not rank your solution.\n" \
                 f"Do not add extra fields except the suggestion field.\n" \
                 f"The issue:\n" \
                 f" :\n{issue}\n\n"
        summary = Gpt_api.summarize_text(text)
        return summary

