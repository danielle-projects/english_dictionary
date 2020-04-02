import sys
import json
import logging

from constants import GeneralConstants


class DictionaryUtils:

    @staticmethod
    def load_dictionary_data(filepath):
        try:
            with open(filepath) as dictionary_data:
                dictionary_data_dict = json.load(dictionary_data)
        except OSError:
            logging.warning('cannot open', filepath)
            sys.exit(GeneralConstants.SYSTEM_EXIT_CODE)
        except ValueError as e:
            logging.warning('cannot convert Json to dictionary', e)
            sys.exit(GeneralConstants.SYSTEM_EXIT_CODE)
        return dictionary_data_dict

    @staticmethod
    def get_user_input(statement_for_user):
        user_input = input(statement_for_user)
        return user_input


