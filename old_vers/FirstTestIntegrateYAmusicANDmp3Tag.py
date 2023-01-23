import os
import yandex_music
from yandex_music import Client
import shutil



client = Client().init()


type_to_name = {
    'track': 'трек',
    'artist': 'исполнитель',
    'album': 'альбом',
    'playlist': 'плейлист',
    'video': 'видео',
    'user': 'пользователь',
    'podcast': 'подкаст',
    'podcast_episode': 'эпизод подкаста',
    'genre': 'жанр',
}


path_log = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\log\\'
path_dir = 'C:\\Users\\admin\\Desktop\\!Готово'

donesTotals = 0
errorTotals = 0

lyricsTotals = 0

listErrors = ''

def send_search_request_and_print_result(query):

    try:
        search_result = client.search(query)
        """search_result.tracks"""
        text = [f'']

        best_result_text = ''
        if search_result.best:
            type_ = search_result.best.type
            best = search_result.best.result

            text.append(f'❗️Лучший результат: {type_to_name.get(type_)}')

            if type_ in ['track', 'podcast_episode']:
                artists = ''
                if best.artists:
                    artists = ' - ' + ', '.join(artist.name for artist in best.artists)
                best_result_text = best.title + artists
            elif type_ == 'artist':
                best_result_text = best.name
            elif type_ in ['album', 'podcast']:
                best_result_text = best.title
            elif type_ == 'playlist':
                best_result_text = best.title
            elif type_ == 'video':
                best_result_text = f'{best.title} {best.text}'

            text.append(f'Содержимое лучшего результата: {best_result_text}\n')



        if best.artists:
            TempAboutSong = ''.join(artist.name for artist in best.artists)

        text.append(f'Artist: {TempAboutSong}')

        TempAboutSong = best.title

        text.append(f'Track: {TempAboutSong}')

        if best.albums:
            TempAboutSong = ''.join(albums.title for albums in best.albums)

        text.append(f'Album: {TempAboutSong}')

        if best.albums:
            TempAboutSong = ''.join(albums.genre for albums in best.albums)

        with open(path_log + 'genre.txt', 'a', encoding='utf-8') as ff:
            ff.writelines(f'\n{TempAboutSong}')

        text.append(f'Genre: {TempAboutSong}')
        #text.append('')

        supplement = best.get_supplement()
        if supplement.lyrics:
            text.append(f'Lyrics: True')
            global lyricsTotals
            lyricsTotals = lyricsTotals + 1
        else:
            text.append(f'Lyrics: False')



        search_result.tracks.results[0].albums[0].download_cover(filename = path_dir + '\\' + query + '.jpg', size = '400x400')


        text.append('')
        print('\n'.join(text))

        global donesTotals
        donesTotals = donesTotals + 1

        with open(path_log + 'report.txt', 'a', encoding='utf-8') as f:
            f.writelines('\n'.join(text))

    except Exception as err:
        print(f'ERROR: {err}')
        global errorTotals
        errorTotals = errorTotals + 1
        with open(path_log + 'report.txt', 'a', encoding='utf-8') as f:
            f.writelines(f'\nERROR: {err}\n')

        with open(path_log + 'TempData.txt', 'a', encoding='utf-8') as f:
            f.writelines(f'{err}\n')

        global listErrors
        listErrors = listErrors + f'\n{query}'

        shutil.move(path_dir + '\\' + query + '.mp3', 'C:\\Users\\admin\\Desktop\\\\notData\\' + query + '.mp3')

def logPrint(str):
    print(str)
    with open(path_log + 'report.txt', 'a', encoding='utf-8') as f:
        f.writelines(str)



if __name__ == '__main__':

    arr1 = os.listdir(path_dir)
    arr = [x.split('.mp3')[0] for x in arr1]

    done = 0
    while not done:

        mess = ''

        for i, x in enumerate(arr):
            mess = f'\n{i} Поиск: {x}'
            logPrint(mess)

            send_search_request_and_print_result(x)

        done = 1

        mess = f'\nСделано: {donesTotals}, Ошибок: {errorTotals}, Texts: {lyricsTotals}'
        logPrint(mess)

        print(listErrors)



