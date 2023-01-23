import os

from yandex_music import Client


ALBUM_ID = 103189744

client = Client().init()

album = client.albums_with_tracks('22036250')
tracks = []
for i, volume in enumerate(album.volumes):
    if len(album.volumes) > 1:
        tracks.append(f'💿 Диск {i + 1}')
    tracks += volume

text = 'АЛЬБОМ\n\n'
text += f'{album.title}\n'
text += f"Исполнитель: {', '.join([artist.name for artist in album.artists])}\n"
text += f'{album.year} · {album.genre}\n'



text += 'Список треков:'

print(text)

for track in tracks:
    if isinstance(track, str):
        print(track)
    else:
        artists = ''
        if track.artists:
            artists = ' - ' + ', '.join(artist.name for artist in track.artists)
        print(track.title + artists)