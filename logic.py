import sys
import psycopg2

import difflib

from constants import GeneralConstants, StatementConstants
from utils import DictionaryUtils


class DictionaryLogic:

    dictionary_words_data = DictionaryUtils.load_dictionary_data()

    @staticmethod
    def process_word_translation():
        word = DictionaryUtils.get_user_input(StatementConstants.INITIAL_STATEMENT)
        word_translation = DictionaryLogic.translate_word(word)
        new_word_to_translate = DictionaryUtils.get_user_input(
            StatementConstants.TRANSLATE_ANOTHER_WORD_STATEMENT.format(word_translation))
        if new_word_to_translate.upper() == GeneralConstants.POSITIVE_CONFIRMATION_INPUT:
            DictionaryLogic.process_word_translation()
        else:
            sys.exit(GeneralConstants.SYSTEM_EXIT_CODE)

    @staticmethod
    def translate_word(word):
        dictionary_words_data = DictionaryLogic.dictionary_words_data
        word = word.lower()
        if word in dictionary_words_data:
            word_translation = DictionaryLogic.dictionary_words_data[word]
        else:
            word_translation = DictionaryLogic.handle_missing_word_in_dictionary(word)
        return word_translation

    @staticmethod
    def handle_missing_word_in_dictionary(word_to_translate):
        result_statement = StatementConstants.WORD_NOT_EXISTS_STATEMENT.format(word_to_translate)
        close_matches = difflib.get_close_matches(
            word_to_translate,
            DictionaryLogic.dictionary_words_data.keys(),
            n=GeneralConstants.MAX_NUM_OF_CLOSE_MATCHES_TO_RETURN,
        )
        if len(close_matches) > 0:
            word_first_match = close_matches[0]
            user_input = input(StatementConstants.MATCH_OFFER_STATEMENT.format(word_first_match))
            if user_input.upper() == GeneralConstants.POSITIVE_CONFIRMATION_INPUT:
                result_statement = DictionaryLogic.translate_word(word_first_match)
        return result_statement
