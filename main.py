import sys
import psycopg2
from difflib import get_close_matches
from utils import (
    load_dictionary_data,
    get_user_input,
)
from constants import (
    INITIAL_STATEMENT,
    MATCH_OFFER_STATEMENT,
    MAX_NUM_OF_CLOSE_MATCHES_TO_RETURN,
    POSITIVE_CONFIRMATION_INPUT,
    TRANSLATE_ANOTHER_WORD_STATEMENT,
    WORD_NOT_EXISTS_STATEMENT,
    SYSTEM_EXIT_CODE,
)

DICTIONARY_WORDS_DATA = load_dictionary_data()


def process_word_translation():
    word_to_translate = get_user_input(INITIAL_STATEMENT)
    word_translation = translate(word_to_translate)
    is_translate_another_word = get_user_input(TRANSLATE_ANOTHER_WORD_STATEMENT % word_translation)
    if is_translate_another_word.upper() == POSITIVE_CONFIRMATION_INPUT:
        process_word_translation()
    else:
        sys.exit(SYSTEM_EXIT_CODE)


def translate(word_to_translate):
    word_to_translate = word_to_translate.lower()
    if word_to_translate in DICTIONARY_WORDS_DATA:
        word_translation = DICTIONARY_WORDS_DATA[word_to_translate]
    else:
        word_translation = handle_missing_word_in_dictionary(word_to_translate)
    return word_translation


def handle_missing_word_in_dictionary(word_to_translate):
    result_statement = WORD_NOT_EXISTS_STATEMENT % word_to_translate
    close_matches = get_close_matches(
        word_to_translate,
        DICTIONARY_WORDS_DATA.keys(),
        n=MAX_NUM_OF_CLOSE_MATCHES_TO_RETURN,
    )
    if len(close_matches) > 0:
        word_first_match = close_matches[0]
        user_input = input(MATCH_OFFER_STATEMENT % word_first_match)
        if user_input.upper() == POSITIVE_CONFIRMATION_INPUT:
            result_statement = translate(word_first_match)
    return result_statement


# def main():
#     handle_word_translation()
    # conn = psycopg2.connect(host="localhost", database="growos", user="growos", password="growos")
    # cur = conn.cursor()
    # cur.execute(f'select * from twe.plots limit 1')


if __name__ == '__main__':
    process_word_translation()
