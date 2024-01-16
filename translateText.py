from deep_translator import GoogleTranslator
from enum import Enum
import csv

class Language(Enum):
    es = 'es'
    fr = 'fr'
    ru = 'ru'
    zh_CN = 'zh-CN'
    hi = 'hi'


text = {
    'deletePostConfirmation': "Are you sure to delete this post",
    'ok': "OK",
}

text_file_path = 'language_data.text'

def target_language(language, text):
    outcomes = {}
    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        for key, value in text.items():
            translator = GoogleTranslator(source='auto', target=language).translate(text=text[key])
            outcomes[key] = translator
            text_file.write(f"{key}: {translator}\n")


target_language(text=text, language=Language.hi.value)


# language = 'Hindi'
# outcomes = {}
# if language == Language.Spanish.value:
#     for key, value in text.items():
#         translator = GoogleTranslator(source='auto', target='es').translate(text=text[key])
#         outcomes[key] = translator
#     print(outcomes)
# elif language == Language.French.value:
#     for key, value in text.items():
#         translator = GoogleTranslator(source='auto', target='fr').translate(text=text[key])
#         outcomes[key] = translator
#     print(outcomes)
# elif language == Language.Russian.value:
#     for key, value in text.items():
#         translator = GoogleTranslator(source='auto', target='ru').translate(text=text[key])
#         outcomes[key] = translator
#     print(outcomes)
# elif language == Language.Chinese.value:
#     for key, value in text.items():
#         translator = GoogleTranslator(source='auto', target='zh-CN').translate(text=text[key])
#         outcomes[key] = translator
#     print(outcomes)
# elif language == Language.Hindi.value:
#     for key, value in text.items():
#         translator = GoogleTranslator(source='auto', target='hi').translate(text=text[key])
#         outcomes[key] = translator
#     print(outcomes)
# else:
#     print('Invalid')


# def target_language(language, text):
#     outcomes = {}
#     for key, value in text.items():
#         translator = GoogleTranslator(source='auto', target=language).translate(text=text[key])
#         outcomes[key] = translator
#     print(outcomes)
#
#
# target_language(text=text, language=Language.hi.value)

# text = 'keep it up, Thank you.'
# spanish_translator = GoogleTranslator(source='auto', target='es').translate(text=text)
# french_translator = GoogleTranslator(source='auto', target='fr').translate(text=text)
# russian_translator = GoogleTranslator(source='auto', target='ru').translate(text=text)
# chinese_translator = GoogleTranslator(source='auto', target='zh-CN').translate(text=text)
# hindi_translator = GoogleTranslator(source='auto', target='hi').translate(text=text)
#
# outcomes = {
#     'english': text,
#     'french': french_translator,
#     'spanish': spanish_translator,
#     'russian': russian_translator,
#     'hindi': hindi_translator,
#     'chinese': chinese_translator
# }
# final_text = [outcomes]
# print(final_text)


# text = {
#     'deletePostConfirmation': "Are you sure to delete this post",
#     'ok': "OK",
#     'delete': "Delete",
#     'shareInGroups': "Share in groups"
# }
# final_text = None
# for key, value in text.items():
#     spanish_translator = GoogleTranslator(source='auto', target='es').translate(text=text[key])
#     french_translator = GoogleTranslator(source='auto', target='fr').translate(text=text[key])
#     russian_translator = GoogleTranslator(source='auto', target='ru').translate(text=text[key])
#     chinese_translator = GoogleTranslator(source='auto', target='zh-CN').translate(text=text[key])
#     hindi_translator = GoogleTranslator(source='auto', target='hi').translate(text=text[key])
#
#     outcomes = {
#         'english': text[key],
#         'french': french_translator,
#         'spanish': spanish_translator,
#         'russian': russian_translator,
#         'hindi': hindi_translator,
#         'chinese': chinese_translator
#     }
#     final_text = [outcomes]
#     print(final_text)
