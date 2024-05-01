def hacer_album(artista, album, canciones=None):
    album = {'artista': artista, 'album': album}
    if canciones:
        album['canciones'] = canciones
    return album

album = hacer_album('The Beatles', 'Abbey Road')
print(album)

album = hacer_album('The Beatles', 'Abbey Road', 17)
print(album)


