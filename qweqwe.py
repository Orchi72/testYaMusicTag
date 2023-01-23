
from yandex_music import Client

client = Client().init()

MDATA = client.tracks(['20223793:1556833'])

print(MDATA)
