import json
from constants import GeneralConstants

general_constants = GeneralConstants()


class DictionaryUtils:

    @staticmethod
    def load_dictionary_data():
        with open(general_constants.DICTIONARY_JSON_FILEPATH) as dictionary_data:
            dictionary_data_dict = json.load(dictionary_data)
            return dictionary_data_dict

    @staticmethod
    def get_user_input(statement_for_user):
        user_input = input(statement_for_user)
        return user_input

