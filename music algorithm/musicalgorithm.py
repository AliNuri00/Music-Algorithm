#veriyi okumak gerekli kod yani kütüphane
import pandas as pd

#Bize gerek sütünlar yani adamın adı mahnı adı...
columns = ['genre', 'artist_name', 'track_name']

#ilk başda yazdığımız veriyi okuyoruz
musics = pd.read_csv('SpotifyFeatures.csv', usecols=columns)

#Random şarkı veren funkçia yano kod
def get_random_song():
    return musics.sample(1).iloc[0]



#Türüne göre rastgele 30 şarkı çekirik bu filedan intten yüklenen
def get_song_by_genre(genre):
    by_genre = musics[musics['genre'] == genre]
    length = len(by_genre)
    if length >= 20:
        return by_genre.sample(30)
    else:
        return by_genre.sample(length)


#artist adına göre random 10 mahnı çekirik o csv dosyasınnan
def get_song_by_artist(artist):
    by_artist = musics[musics['artist_name'] == artist]
    length = len(by_artist)
    if length >= 20:
       return by_artist.sample(15)
    else:
         return by_artist.sample(length)  



#Türüne ve artist adına gçre random çektiğimiz
#şarkılardan 10 random aşrkı çekirik
def suggest_10_songs(genre, artist):
    by_genre = get_song_by_genre(genre)
    by_artist = get_song_by_artist(artist)
    concat = pd.concat([by_genre, by_artist])
    length = len(concat)
    if length >= 10:
        return concat.sample(10)
    else:
        return concat.sample(length)



#Başlangıç şarkısını seçirik
current = get_random_song()

#İndi şarkı başdasın
while True:
    #indi çalan mahnıyı yazdırırıq
    print("*************************************************************************")
    print(current['artist_name'], "-", current['track_name'], "çalınıyor..")
    print("*************************************************************************")
    #10 dene şarkı önerisi veriyoruz
    print("Öneriler")
    suggestions = suggest_10_songs(current['genre'], current['artist_name'])
    for i in range(len(suggestions)):
        print(i+1, suggestions.iloc[i]['artist_name'],
        "-", suggestions.iloc[i]['track_name'])

    #user 1 şarkı seçir ve çıkmak üçün -1 yazır
    choose = input("Choose:")
    if choose == '-1':
        break
    else:
        current = suggestions.iloc[int(choose)-1]