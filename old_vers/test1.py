"""song = songdetails.scan('c:\\Users\\admin\\Desktop\\!Готов\\Adam Hairston - All the time.mp3')"""
import yandex_music

"""
album
albumartist
artist
artwork
comment
compilation
composer
discnumber
genre
lyrics
totaldiscs
totaltracks
tracknumber
tracktitle
year
isrc
"""

import music_tag
from yandex_music import Client

f = music_tag.load_file("2rbina 2rista - Mortal Kombat.mp3")

# dict access returns a MetadataItem
title_item = f['title']
print(f)
print('')



genre_to_name = {
    '': 'NONE',
    'rap': 'исполнитель',
    'rusrap': 'альбом',
    'alternative': 'плейлист',
    'techno': 'видео',
    'foreignrap': 'пользователь',

    'podcast': 'подкаст',
    'podcast_episode': 'эпизод подкаста',
    'genre': 'жанр',
    'genre': 'жанр',
}





client = Client().init()
test123 = Client(language='ru').genres()
#print(test123)


cover = yandex_music.Cover().__init__()
print(cover)

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



search_result = client.search(text='2rbina 2rista - 2rbina 2rista')#,type_='track')
"""search_result.tracks"""
text = [f'']
#print(search_result)

search_result.tracks.results[0].albums[0].download_cover(filename='TestCover.jpg', size='200x200')


search_result = client.search(text='Amaranthine - Amaranthe')#,type_='track')

best_result_text = ''
if search_result.best:
    type_ = search_result.best.type
    best = search_result.best.result

    supplement = best.get_supplement()
    if supplement.lyrics:
        print(supplement.lyrics.full_lyrics)
    else:
        print('Текст песни отсутствует')
    print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
    print(supplement)


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
f['artist'] = TempAboutSong

TempAboutSong = best.title

text.append(f'Track: {TempAboutSong}')
f['title'] = TempAboutSong

if best.albums:
    TempAboutSong = ''.join(albums.title for albums in best.albums)

text.append(f'Album: {TempAboutSong}')
f['album'] = TempAboutSong

if best.albums:
    TempAboutSong = ''.join(albums.genre for albums in best.albums)

text.append(f'Genre: {TempAboutSong}')
f['genre'] = genre_to_name.get(TempAboutSong)


if best.albums:
    Year = best.albums[0].year

text.append(f'Year: {Year}')
f['year'] = Year

print(best.albums)

text.append('')

text.append('')
print('\n'.join(text))


print(f['lyrics'])


with open('TestCover.jpg', 'rb') as img_in:
    f['artwork'] = img_in.read()



f.save()

# additional values can be appended to the tags
#f.append_tag('title', 'subtitle')


print(f)