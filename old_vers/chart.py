import os

from yandex_music import Client


CHART_ID = 'world'
TOKEN = os.environ.get('TOKEN')

client = Client(TOKEN).init()
chart = client.chart(CHART_ID).chart

text = [f'π {chart.title}', chart.description, '', 'Π’ΡΠ΅ΠΊΠΈ:']

for track_short in chart.tracks:
    track, chart = track_short.track, track_short.chart
    artists = ''
    if track.artists:
        artists = ' - ' + ', '.join(artist.name for artist in track.artists)

    track_text = f'{track.title}{artists}'

    if chart.progress == 'down':
        track_text = 'π» ' + track_text
    elif chart.progress == 'up':
        track_text = 'πΊ ' + track_text
    elif chart.progress == 'new':
        track_text = 'π ' + track_text
    elif chart.position == 1:
        track_text = 'π ' + track_text

    track_text = f'{chart.position} {track_text}'
    text.append(track_text)

print('\n'.join(text))