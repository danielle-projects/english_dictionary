from logic import DictionaryLogic


# def main():
    # conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")
    # cur = conn.cursor()
    # cur.execute(f'select * from twe.plots limit 1')


if __name__ == '__main__':
    DictionaryLogic().process_word_translation()
