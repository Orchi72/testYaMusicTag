import os
import shutil


path_log = 'log/report.txt'
path_genre = 'log/genre.txt'
path_dir = 'C:/Users/admin/Desktop/исход/'
path_dest = 'C:/Users/admin/Desktop/Data/'

donesTotals = 0
errorTotals = 0
lyricsTotals = 0
listErrors = ''



if __name__ == '__main__':

    tmp = os.listdir(path_dir)
    temp_arr = []
    arr = []
    done = 0

    artists = []

    list_art = []

    for x in tmp:
        if x.endswith('.mp3'):
            temp_arr.append(x.split(' - ')[0])

    for x in temp_arr:
        spl = x.split(' & ')
        for y in spl:
            arr.append(y)






    for artist in arr:

        if artist.strip() != '':
            # print(line.strip())
            #count += 1

            if artist.strip() not in artists:
                artists.append(artist.strip())

    print(artists)
    print(f'Count: {len(artists)}')


    min_song = 12
    artist_with_min_song = []

    for temp_art in temp_arr:

        count = 0

        for x in temp_arr:

            if x == temp_art:
                count += 1


        if count > min_song:
            if temp_art not in artist_with_min_song:
                artist_with_min_song.append(temp_art)

    print(artist_with_min_song)
    print(f'Count: {len(artist_with_min_song)}')




    shutil.move(path_dir + query + '.mp3', path_dest + query + '.mp3')