import os
import yandex_music
from yandex_music import Client



client = Client().init()





def send_search_request_and_print_result(query):
    search_result = client.search(query)

    text = [f'Результаты по запросу "{query}":', '']




    text.append('')
    text.append('')
    text.append('')













    MDATA = yandex_music.MetaData(search_result.best.result)
    MDATA = client.tracks(['51039982:7091468'])
    """, '40133452:5206873', '48966383:6693286', '51385674:7163467'])"""
    text.append('---------------------------------------------------------------------------------')
    text.append(f'MDATA: {MDATA}')





    text.append('')
    print('\n'.join(text))



if __name__ == '__main__':
    while True:
        input_query = input('Введите поисковой запрос: ')
        send_search_request_and_print_result(input_query)