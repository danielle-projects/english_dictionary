import json


def load_dictionary_data():
    with open('dictionary.json') as dictionary_data:
        dictionary_data_dict = json.load(dictionary_data)
        return dictionary_data_dict


def get_user_input(statement_for_user):
    user_input = input(statement_for_user)
    return user_input

