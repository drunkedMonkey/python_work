def hacer_album(artista, album, canciones=None):
    album = {'artista': artista, 'album': album}
    if canciones:
        album['canciones'] = canciones
    return album

active = True
albums = []

while active:
    artista = input("¿Cuál es el nombre del artista? ")
    album = input("¿Cuál es el nombre del album? ")
    canciones = input("¿Cuántas canciones tiene el album? ")
    album = hacer_album(artista, album, canciones)
    albums.append(album)
    repeat = input("¿Quieres que otro album sea registrado? (yes/no) ")
    if(repeat == "no"):
        active = False

print("\n--- Resultados de la encuesta ---")
for album in albums:
    print(album)
    