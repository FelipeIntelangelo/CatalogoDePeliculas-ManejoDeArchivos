from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas


opcion = None

while opcion != 4:
    try:
        print('1. Agregar Pelicula')
        print('2. Listar Peliculas')
        print('3. Eliminar Peliculas')
        print('4. Salir')
        opcion = int(input('Elegir una opcion: '))

        if opcion == 1:
            nombre_pelicula = input('Ingrese una pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_pelicula(pelicula)
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()
        elif opcion ==3:
            CatalogoPeliculas.eliminar_peliculas()
    except Exception as e:
        print(f'Introduzca un numero del 1 al 4 ')
        opcion = None
else:
    print('Aplicacion finalizada')