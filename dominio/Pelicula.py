class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'El nombre de la pelicula es: {self.nombre}'

if __name__ == '__main__':

    pelicula1 = Pelicula('Spiderman3')
    print(pelicula1)