def make_album(name, album_title, track_count=None):
    album = {'Name': name, 'Album': album_title}
    if track_count is not None:
        album['Tracks'] = track_count
    return album

def print_album(album, index):
    print(f"\nAlbum {index + 1}:")
    for key, value in album.items():
        print(f"\t{key.title()} : {value}")

album_list = []
album_count = int(input("Give number of albums: "))

for i in range(album_count):
    name = input("Give Artist Name: ")
    title = input("Give Album Title: ")
    has_tracks = input("Does it have a track count? (Y/N): ")

    if has_tracks.lower() == 'y':
        track_count = input("Give Track Count: ")
        album = make_album(name, title, track_count)
    else:
        album = make_album(name, title)

    album_list.append(album)

for i in range(album_count):
    print_album(album_list[i], i)
