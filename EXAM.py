class Cancion:
    def __init__(self, nombre, artista, duracion):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        return f"{self.nombre} - {self.artista} ({self.duracion} min)"

class Artista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def lanzar_cancion(self, cancion):
        self.canciones.append(cancion)

    def __str__(self):
        return self.nombre

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.playlist = []
        self.artistas_seguidos = []
    def seguir_artista(self, artista):
        self.artistas_seguidos.append(artista)
    def agregar_cancion_playlist(self, cancion):
        self.playlist.append(cancion)
    def eliminar_cancion_playlist(self, cancion):
        if cancion in self.playlist:
            self.playlist.remove(cancion)
    def reproducir_cancion(self, cancion):
        if cancion in self.playlist:
            print(f"Reproduciendo {cancion}")
    def escuchar_artista(self, artista):
        if artista in self.artistas_seguidos:
            print(f"Escuchando todo de {artista.nombre}:")
            for cancion in artista.canciones:
                print(f"Reproduciendo {cancion}")

    def __str__(self):
        return self.nombre

class AppMusica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []
        self.artistas = []
        self.canciones = []
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
    def agregar_artista(self, artista):
        self.artistas.append(artista)
    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)
    def mostrar_artistas(self):
        for artista in self.artistas:
            print(artista)
    def mostrar_canciones(self):
        for cancion in self.canciones:
            print(cancion)

    def __str__(self):
        return self.nombre

# Crear instancia de AppMusica
app = AppMusica("MiAppDeMusica")

# ARTISTAS
artista1 = Artista("Led Zeppelin")
artista2 = Artista("Eagles")

# CANCIONES Led Zeppelin
cancion1 = Cancion("Stairway to Heaven", artista1, 8)
cancion2 = Cancion("Kashmir", artista1, 9)
cancion3 = Cancion("Immigrant Song", artista1, 2.5)

artista1.lanzar_cancion(cancion1)
artista1.lanzar_cancion(cancion2)
artista1.lanzar_cancion(cancion3)

# CANCIONES Eagles
cancion4 = Cancion("Hotel California", artista2, 6.5)
cancion5 = Cancion("Desperado", artista2, 4.5)
cancion6 = Cancion("Take It Easy", artista2, 3.5)

artista2.lanzar_cancion(cancion4)
artista2.lanzar_cancion(cancion5)
artista2.lanzar_cancion(cancion6)

# USUARIOS
usuario1 = Usuario("Juan")
usuario2 = Usuario("Maria")

# Agregar los artistas, usuarios y canciones a la aplicacion
app.agregar_artista(artista1)
app.agregar_artista(artista2)

app.agregar_usuario(usuario1)
app.agregar_usuario(usuario2)

app.agregar_cancion(cancion1)
app.agregar_cancion(cancion2)
app.agregar_cancion(cancion3)
app.agregar_cancion(cancion4)
app.agregar_cancion(cancion5)
app.agregar_cancion(cancion6)

# SEGUIR ARTISTA
usuario1.seguir_artista(artista1)
# AGREGAR CANCION A PLAYLIST POR EL USUARIO
usuario1.agregar_cancion_playlist(cancion1)
# REPRODUCIR CANCION
usuario1.reproducir_cancion(cancion1)
# ELIMINAR CANCION
usuario1.eliminar_cancion_playlist(cancion1)
# ESCUCHAR TODAS LAS CANCIONES
usuario1.escuchar_artista(artista1)
# MOSTRAR TODOS LOS USUARIOS, ARTISTAS Y CANCIONES
print("\nUsuarios en la aplicacion:")
app.mostrar_usuarios()

print("\nArtistas en la aplicacion:")
app.mostrar_artistas()

print("\nCanciones en la aplicacion:")
app.mostrar_canciones()
