from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404

# Datos: lista de diccionarios
PELICULAS = [
    {
        'id': 1,
        'titulo': 'El Padrino',
        'genero': 'Drama',
        'duracion': 175,
        'director': 'Francis Ford Coppola',
        'anio': 1972,
        'sala': 'Sala 1',
        'horario': '18:30',
        'sinopsis': 'La historia de la familia Corleone, una de las '
                    'sagas mas influyentes del cine sobre el poder y la lealtad.',
        'clasificacion': 'R',
        'puntuacion': 9.2,
    },
    {
        'id': 2,
        'titulo': 'Interestelar',
        'genero': 'Ciencia Ficcion',
        'duracion': 169,
        'director': 'Christopher Nolan',
        'anio': 2014,
        'sala': 'Sala 2',
        'horario': '20:00',
        'sinopsis': 'Un grupo de astronautas viaja a traves de un agujero '
                    'de gusano en busca de un nuevo hogar para la humanidad.',
        'clasificacion': 'PG-13',
        'puntuacion': 8.7,
    },
    {
        'id': 3,
        'titulo': 'Parasitos',
        'genero': 'Drama / Suspenso',
        'duracion': 132,
        'director': 'Bong Joon-ho',
        'anio': 2019,
        'sala': 'Sala 3',
        'horario': '19:15',
        'sinopsis': 'Una familia pobre se infiltra poco a poco en la vida '
                    'de una adinerada familia coreana.',
        'clasificacion': 'R',
        'puntuacion': 8.5,
    },
    {
        'id': 4,
        'titulo': 'El Viaje de Chihiro',
        'genero': 'Animacion / Fantasia',
        'duracion': 125,
        'director': 'Hayao Miyazaki',
        'anio': 2001,
        'sala': 'Sala 4',
        'horario': '16:45',
        'sinopsis': 'Una nina entra a un mundo magico donde debera trabajar '
                    'para liberar a sus padres convertidos en cerdos.',
        'clasificacion': 'PG',
        'puntuacion': 8.6,
    },
    {
        'id': 5,
        'titulo': 'Pulp Fiction',
        'genero': 'Crimen / Drama',
        'duracion': 154,
        'director': 'Quentin Tarantino',
        'anio': 1994,
        'sala': 'Sala 1',
        'horario': '21:30',
        'sinopsis': 'Historias entrelazadas de gangsters, boxeadores y '
                    'matones en el Los Angeles de los noventa.',
        'clasificacion': 'R',
        'puntuacion': 8.9,
    },
    {
        'id': 6,
        'titulo': 'Spider-Man: Un Nuevo Universo',
        'genero': 'Animacion / Accion',
        'duracion': 117,
        'director': 'Bob Persichetti',
        'anio': 2018,
        'sala': 'Sala 2',
        'horario': '15:00',
        'sinopsis': 'Miles Morales se convierte en Spider-Man y conoce a '
                    'versiones alternativas del heroe de otras dimensiones.',
        'clasificacion': 'PG',
        'puntuacion': 8.4,
    },
]


def inicio(request):
    """Portada: lista completa de peliculas."""
    contexto = {
        'peliculas': PELICULAS,
        'total': len(PELICULAS),
    }
    return render(request, 'cartelera/inicio.html', contexto)


def detalle(request, id):
    """Detalle de una pelicula por su id. Lanza 404 si no existe."""
    pelicula = next((p for p in PELICULAS if p['id'] == id), None)
    if pelicula is None:
        raise Http404('Pelicula no encontrada')
    return render(request, 'cartelera/detalle.html', {'p': pelicula})