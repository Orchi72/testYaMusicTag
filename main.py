import os
import shutil
import yandex_music
from structs import *
from yandex_music import Client

client = Client().init()

path_log = 'log/report.txt'
path_genre = 'log/genre.txt'
path_dir = 'C:/Users/admin/Desktop/!Готово/'
path_dest = 'C:/Users/admin/Desktop/notData/'

donesTotals = 0
errorTotals = 0
lyricsTotals = 0
listErrors = ''






def send_search_request_and_print_result(query):

    global donesTotals
    global lyricsTotals
    global errorTotals
    global listErrors


    try:
        search_result = client.search(query)
        # print(search_result.best)

        text = []
        best_result_text = ''



        if search_result.best:

            artists = ''
            track = ''
            album = ''
            year = ''
            genre = ''

            if search_result.best.type == 'track':

                best_res = search_result.best.result

                if best_res.artists:
                    artists = ', '.join(artist.name for artist in best_res.artists)

                track = best_res.title

                if best_res.albums:
                    album = ''.join(albums.title for albums in best_res.albums)

                    year = best_res.albums[0].year

                    temp_about_song = ''.join(albums.genre for albums in best_res.albums)
                    if temp_about_song in genres_k_v:
                        genre = genres_k_v[temp_about_song]

                with open(path_genre, 'a', encoding='utf-8') as ff:
                    ff.writelines(f'\n{genre}')

                text.append(f"Результат: {artists + ' - ' + track}\n")
                # Разбор тегов
                text.append(f'Artist: {artists}')
                text.append(f'Track: {track}')
                text.append(f'Album: {album}')
                text.append(f'Year: {year}')
                text.append(f'Genre: {genre}')

                supplement = best_res.get_supplement()
                if supplement.lyrics:
                    text.append(f'Lyrics: True')
                    lyricsTotals = lyricsTotals + 1
                else:
                    text.append(f'Lyrics: False')

                flag = 0
                for t in str(artists.split(' ')):
                    if t.lower() in template_search_uncorrect:
                        flag = 1

                if query.split(' - ')[1].lower() != track.lower() or flag == 1 :
                    asd = f"WARNING: {query.split(' - ')[1]} != {track}/ flag = {flag}"
                    print(f'{asd}')
                    shutil.move(path_dir + query + '.mp3', path_dest + query + '.mp3')
                    return

            else:
                log_print(f'ERROR: NoData', path_log)

                errorTotals = errorTotals + 1
                listErrors = listErrors + f'\n{query}'

                shutil.move(path_dir + query + '.mp3', path_dest + query + '.mp3')
                return

        #

        search_result.tracks.results[0].albums[0].download_cover(filename=path_dir + query + '.jpg',
                                                                 size='400x400')











        # MDATA = client.tracks(['51039982:7091468'])
        #

        text.append('')
        log_print('\n'.join(text), path_log)

        donesTotals = donesTotals + 1

    except Exception as err:

        log_print(f'Exception: {err}', path_log)
        errorTotals = errorTotals + 1
        listErrors = listErrors + f'\n{query}'

        shutil.move(path_dir + query + '.mp3', path_dest + query + '.mp3')


def log_print(message, file_log):
    print(message)
    with open(file_log, 'a', encoding='utf-8') as f:
        f.writelines(message)


if __name__ == '__main__':

    tmp = os.listdir(path_dir)
    arr = []
    done = 0

    for x in tmp:
        if x.endswith('.mp3'):
            arr.append(x.split('.mp3')[0])

    while not done:

        mess = ''

        for i, x in enumerate(arr):
            mess = f'\n{i} Поиск: {x}\n'
            log_print(mess, path_log)

            send_search_request_and_print_result(x)

        done = 1

        mess = f'\nНайдено песен: {donesTotals}, Ошибок: {errorTotals}, Тестов найдено: {lyricsTotals}'
        log_print(mess, path_log)

        print(listErrors)
