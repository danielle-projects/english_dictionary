import sys

import difflib

from constants import GeneralConstants, StatementConstants
from utils import DictionaryUtils


class DictionaryLogic:

    def __init__(self, filepath):
        self.dictionary_words_data = DictionaryUtils.load_dictionary_data(filepath)

    def process_word_translation(self):
        word = DictionaryUtils.get_user_input(StatementConstants.INITIAL_STATEMENT)
        word_translation = self.translate_word(self, word)
        new_word_to_translate = DictionaryUtils.get_user_input(
            StatementConstants.TRANSLATE_ANOTHER_WORD_STATEMENT.format(word_translation))
        if new_word_to_translate.upper() == GeneralConstants.POSITIVE_CONFIRMATION_INPUT:
            self.process_word_translation()
        else:
            sys.exit(GeneralConstants.SYSTEM_EXIT_CODE)

    @staticmethod
    def translate_word(self, word):
        dictionary_words_data = self.dictionary_words_data
        word = word.lower()
        if word in dictionary_words_data:
            word_translation = self.dictionary_words_data[word]
        else:
            word_translation = self.handle_missing_word_in_dictionary(self, word)
        return word_translation

    @staticmethod
    def handle_missing_word_in_dictionary(self, word_to_translate):
        result_statement = StatementConstants.WORD_NOT_EXISTS_STATEMENT.format(word_to_translate)
        close_matches = difflib.get_close_matches(
            word=word_to_translate,
            possibilities=self.dictionary_words_data.keys(),
            n=GeneralConstants.MAX_NUM_OF_CLOSE_MATCHES_TO_RETURN,
        )
        if len(close_matches) > 0:
            word_first_match = close_matches[0]
            user_input = input(StatementConstants.MATCH_OFFER_STATEMENT.format(word_first_match))
            if user_input.upper() == GeneralConstants.POSITIVE_CONFIRMATION_INPUT:
                result_statement = self.translate_word(self, word_first_match)
        return result_statement
