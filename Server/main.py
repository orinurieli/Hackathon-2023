import Server.speech_to_text.Logic as stt
import Server.open_ai.Logic as gpt
import resources.summaries as rsc

if __name__ == "__main__":
    # for generic in the future
    stt_logic = stt.Logic()
    gpt_logic = gpt.Logic()
    data_base = rsc.database()

    text = stt_logic.parse_audio_to_txt("C:/Users/amirk/Downloads/test.wav")
    gpt_summary = gpt_logic.generate_solution(''.join(str(element) for element in data_base.data), text)
    print(gpt_summary)