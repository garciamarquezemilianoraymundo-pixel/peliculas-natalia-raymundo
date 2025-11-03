from flask import Flask, render_template # Importa la clase Flask y la función render_template desde el paquete flask

app = Flask(__name__) # Crea la aplicación flask; __name__ ayuda a localizar recursos y plantillas

# Datos de ejemplo para las películas:
# Diccionario donde cada clave es una categoría y su valor es una lista de diccionarios (película)
peliculas = {
    'suspenso': [
        {'titulo': 'El Secreto de sus Ojos',
         'sinopsis': 'Un ex empleado judicial decide escribir una novela sobre un asesinato ocurrido años atrás.'},
        {'titulo': 'Donnie Darko',
         'sinopsis': 'Un adolescente tiene visiones de un conejo gigante que lo manipula para cometer crímenes.'},
    ],
    'terror': [
        {'titulo': 'It (Eso)',
         'sinopsis': 'Un grupo de niños debe enfrentarse a una entidad maligna que toma la forma de un payaso.'},
        {'titulo': 'Babadook',
         'sinopsis': 'Una madre soltera debe lidiar con la aparición de un monstruo de un libro infantil.'},
    ],
    'romance': [
        {'titulo': 'Antes del Amanecer',
         'sinopsis': 'Un joven americano y una estudiante francesa se conocen en un tren y pasan la noche juntos en Viena.'},
        {'titulo': 'Diario de una Pasión',
         'sinopsis': 'Un hombre lee a una mujer con Alzheimer la historia de un amor que se remonta a la Segunda Guerra Mundial.'},
    ],
    'infantil': [
        {'titulo': 'Coco',
         'sinopsis': 'Un niño que sueña con ser músico se embarca en un viaje a la Tierra de los Muertos.'},
        {'titulo': 'Cómo Entrenar a tu Dragón',
         'sinopsis': 'Un joven vikingo que no encaja entabla una amistad improbable con un dragón herido.'},
    ]
}

@app.route('/') # Define la ruta raíz (http://localhost:5000/)
def index():
    return render_template('index.html') # Renderiza la plantilla templates/index.html para la página principal

@app.route('/suspenso') # Define la ruta /suspenso
def suspenso():
    # Pasa la lista de películas de la categoría 'suspenso' a la plantilla suspenso.html
    return render_template('suspenso.html', peliculas=peliculas['suspenso'])

@app.route('/terror') # Define la ruta /terror
def terror():
    # Pasa la lista de películas de la categoría 'terror' a la plantilla terror.html
    return render_template('terror.html', peliculas=peliculas['terror'])

@app.route('/romance') # Define la ruta /romance
def romance():
    # Pasa la lista de películas de la categoría 'romance' a la plantilla romance.html
    return render_template('romance.html', peliculas=peliculas['romance'])

@app.route('/infantil') # Define la ruta /infantil
def infantil():
    # Pasa la lista de películas de la categoría 'infantil' a la plantilla infantil.html
    return render_template('infantil.html', peliculas=peliculas['infantil'])

if __name__ == '__main__': # Comprueba si se ejecuta este archivo directamente (no importado)
    app.run(debug=True) # Inicia el servidor de desarrollo con recarga automática y modo debug activado