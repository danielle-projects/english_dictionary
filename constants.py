

class StatementConstants:

    def __init__(self):
        self.INITIAL_STATEMENT = "Enter the word you want to translate:\n"
        self.TRANSLATE_ANOTHER_WORD_STATEMENT = "{}\n Would you like to translate another word?\n"
        self.WORD_NOT_EXISTS_STATEMENT = "The word '{}' doesn\'t exist. \n"
        self.MATCH_OFFER_STATEMENT = "Did you mean '{}' instead? Enter Y if yes or N if no\n"


class GeneralConstants:

    def __init__(self):
        self.DICTIONARY_JSON_FILEPATH = 'dictionary.json'
        self.POSITIVE_CONFIRMATION_INPUT = 'Y'
        self.MAX_NUM_OF_CLOSE_MATCHES_TO_RETURN = 1
        self.SYSTEM_EXIT_CODE = 0
