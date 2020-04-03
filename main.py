from dictionary_logic import DictionaryLogic
from constants import GeneralConstants


if __name__ == '__main__':
    DictionaryLogic(filepath=GeneralConstants.DICTIONARY_JSON_FILEPATH).process_word_translation()

