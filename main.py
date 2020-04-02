import sys
import psycopg2

import difflib

from constants import (
    StatementConstants,
    GeneralConstants,
)
from utils import DictionaryUtils

dictionary_utils = DictionaryUtils()
statements_constants = StatementConstants()
general_constants = GeneralConstants()

DICTIONARY_WORDS_DATA = dictionary_utils.load_dictionary_data()


def process_word_translation():
    word_to_translate = dictionary_utils.get_user_input(statements_constants.INITIAL_STATEMENT)
    word_translation = _translate_word(word_to_translate)
    new_word_to_translate = dictionary_utils.get_user_input(statements_constants.TRANSLATE_ANOTHER_WORD_STATEMENT.format(word_translation))
    if new_word_to_translate.upper() == general_constants.POSITIVE_CONFIRMATION_INPUT:
        process_word_translation()
    else:
        sys.exit(general_constants.SYSTEM_EXIT_CODE)


def _translate_word(word):
    word = word.lower()
    if word in DICTIONARY_WORDS_DATA:
        word_translation = DICTIONARY_WORDS_DATA[word]
    else:
        word_translation = _handle_missing_word_in_dictionary(word)
    return word_translation


def _handle_missing_word_in_dictionary(word_to_translate):
    result_statement = statements_constants.WORD_NOT_EXISTS_STATEMENT.format(word_to_translate)
    close_matches = difflib.get_close_matches(
        word_to_translate,
        DICTIONARY_WORDS_DATA.keys(),
        n=general_constants.MAX_NUM_OF_CLOSE_MATCHES_TO_RETURN,
    )
    if len(close_matches) > 0:
        word_first_match = close_matches[0]
        user_input = input(statements_constants.MATCH_OFFER_STATEMENT.format(word_first_match))
        if user_input.upper() == general_constants.POSITIVE_CONFIRMATION_INPUT:
            result_statement = _translate_word(word_first_match)
    return result_statement


# def main():
#     handle_word_translation()
    # conn = psycopg2.connect(host="localhost", database="growos", user="growos", password="growos")
    # cur = conn.cursor()
    # cur.execute(f'select * from twe.plots limit 1')


if __name__ == '__main__':
    process_word_translation()
