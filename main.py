from flask import Flask, request, jsonify
from Datos.usuario import Usuario
from Datos.receta import Receta
from Datos.comentario import Comentario
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

Usuarios = [] 
Recetas = []
Comentarios = []
cont_recetas = 5

Usuarios.append(Usuario("Usuario", "Maestro", "admin", "admin", "administrador"))
Usuarios.append(Usuario("Jose", "Choc", "josec", "12345678", "cliente"))
Recetas.append(Receta("1", "admin", "Flan Casero", "Descubre una receta tradicional con el dulzor y la cremosidad de la leche condensada", "3/4 taza de azúcar morena(250 g.) - 5 huevos medianos - 1 lata de Leche Condensada -  1 lata de Leche Evaporada - 2 cucharaditas de extracto de vainilla", "En una cacerola a fuego bajo colocar el azúcar y calentar hasta que tome una tonalidad dorada. Mantener el sartén a temperatura baja para evitar que se queme el caramelo. Verter el caramelo en el fondo de un molde refractario redondo de 9″ de diámetro y reservar. Licuar por 2 minutos los demás ingredientes y verter sobre el molde con el caramelo. Colocar el molde con la mezcla dentro de otro molde con agua (baño María) y hornear a 180 °C por 1 hora o hasta que firme. Retirar del horno dejar enfriar a temperatura ambiente por 30 minutos o hasta que este fresco. Refrigerar por 1 hora antes de desmoldar (esto permitirá que sea más fácil y que tome un poco más de firmeza). Servir y disfrutar.", "160 minutos", "https://d1uz88p17r663j.cloudfront.net/original/14899b7a23698c325447f59a27fd45bc_Resultado_Flan___La_Lechera.jpg"))
Recetas.append(Receta("2", "admin", "Pasta con Atún", "Prepara un almuerzo delicioso, fácil y rápido con esta receta de Pasta con Atún.", "5 tazas pasta penne cruda - 1 litro de agua - 1/3 taza de apio cortado finamente - 1/2 taza de cebolla cortada finamente - 1/4 taza de cilantro cortado finamente - 1/2 taza de Mayonesa - 1 taza de atún enlatado en agua escurrido - Sal y pimienta al gusto", "En una cacerola a fuego alto colocar la pasta y cocinar hasta que esté al dente. En una taza, colocar el apio, la cebolla, el cilantro, la Mayonesa MAGGI® y el atún. Mezclar de forma envolvente y ajustar el punto de sal y pimienta al gusto. Añadir la pasta cocida de poco a poco. Ajustar el punto de sal y pimienta si es necesario y disfrutar.", "25 minutos", "https://d1uz88p17r663j.cloudfront.net/original/46bfb7475d5f5061bcbf0e44bb72d0a6_at_.png"))
Recetas.append(Receta("3", "admin", "Pollo Guisado", "Aprende a preparar la tradicional receta del pollo guisado de una forma sencilla.", "1 Libra Pechuga De Pollo sin hueso ni piel cortada en cubos - 1 Sobre Consomé De Pollo - 1 Cucharada Aceite De Oliva - 4 Dientes Ajo cortados finamente - 1 Taza Cebolla cortada finamente - 1 3/4 Taza Papas cortadas en dados - 1 3/4 Taza Zanahorias cortadas en dados - 1 1/2 Taza Tomate sin piel - 1 Pizca Pimienta Negra Molida", "En un tazón colocar el pollo, marinar con el Consomé de Pollo. Reservar. En una cacerola a fuego alto, verter el aceite sofreír el ajo y la cebolla por 2 minutos. Añadir la papa y la zanahoria cocinar por 5 minutos. Agregar el pollo, cocinar por 10 minutos, añadir el tomate bajar el nivel del fuego, cocinar por 10 minutos más, añade pimienta al gusto. Apagar el fuego.", "32 minutos", "https://d1uz88p17r663j.cloudfront.net/original/89c8e2434ec8482972f0c2a7953c37c3_polloooo_.png"))
Recetas.append(Receta("4", "admin", "Albóndigas en salsa boloñesa", "Albóndigas en salsa boloñesa, perfectas para acompañar con arroz, pasta o vegetales.", "30 Gramos Caldo Casero Sabor Res MAGGI® - 2 Piezas Huevo - Cebolla Blanca - Carne Molida De Res - Pan Francés - Pan molido - Cilantro Cortado finamente - Aceite De Oliva - Salsa De Tomate Bolognesa - Agua - sal - Pimienta Negra Molida Al gusto", "Precalentar el horno a 250°C. En un recipiente, marinar la carne molida con Sal de Ajo, Caldo Casero MAGGI® sabor res, huevos, cebolla rallada y pan molido. Revolver con la mano hasta que quede bien mezclado. Dejar reposar por 5 minutos. Formar las bolitas de carne con pequeñas porciones, colocarlas en una bandeja para horno con aceite de oliva y cubrirlas con papel aluminio. Llevar al horno y cocinar a 200°C por 20 minutos. Retirar del horno. Colocar las albóndigas cocidas en una cacerola mediana, agregar la Salsa de Tomate MAGGI® estilo boloñesa, agua y cocinar a fuego medio por 15 minutos con la cacerola tapada. Apagar y ajustar el punto de sal y pimienta necesario.", "43 minutos", "https://d1uz88p17r663j.cloudfront.net/original/80938383d8e309b0dd6fc32817c1b2e3_alal.png"))


@app.route('/', methods =['GET'])
def rutaIniciao():
    return("<h1>Api de Proyecto 2 - 201905743</h1>")

@app.route('/Personas', methods=['GET'])
def obtenerPersonas():
    global Usuarios
    Datos = []
    for usuario in Usuarios:
        Dato = {
            'nombre': usuario.getNombre(), 
            'apellido': usuario.getApellido(), 
            'usuario': usuario.getUsuario(),
            'tipo': usuario.getTipo()
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Personas/<string:nombre>', methods=['GET'])
def ObtenerPersona(nombre):
    global Usuarios
    for usuario in Usuarios:
        if usuario.getUsuario() == nombre:
            Dato = {
                'nombre': usuario.getNombre(), 
                'apellido': usuario.getApellido(), 
                'usuario': usuario.getUsuario(),
                'tipo': usuario.getTipo(),
                'contrasena': usuario.getContrasena()
                }
            break
    respuesta = jsonify(Dato)
    return(respuesta)
        

@app.route('/Personas/<string:nombre>', methods=['PUT'])
def ActualizarPersona(nombre):
    global Usuarios
    a = 0
    encontrado = False
    username1 = request.json['usuario']
    encontrado2 = False
    print(username1)
    
    for i in range(len(Usuarios)):
        a = i
        if nombre == Usuarios[i].getUsuario():
            encontrado = True
            break
        
        print(a)

    if encontrado:
        for user in Usuarios:
            if username1 == user.getUsuario():
                if username1 == nombre:
                    encontrado2 = True
                else:
                    encontrado2 = False
                    break
            encontrado2 = True
                    
                
    print(a)  

    if encontrado2:
        Usuarios[a].setNombre(request.json['nombre'])
        Usuarios[a].setApellido(request.json['apellido'])
        Usuarios[a].setUsuario(request.json['usuario'])
        Usuarios[a].setContrasena(request.json['contrasena'])
        return jsonify({
            'message':'Success',
            'reason':'Se ha registrado el usuario'
            })
    return jsonify({
            'message':'Failed',
            'reason':'El usuario ya esta registrado'
            })

    

@app.route('/Personas/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    global Usuarios
    for i in range(len(Usuarios)):
        if nombre == Usuarios[i].getNombre():
            del Usuarios[i]
            break
    return jsonify({'message':'Se elimino el dato exitosamente'})

@app.route('/Personas', methods=['POST'])
def AgregarUsuario():
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    usuario = request.json['usuario']
    contrasena = request.json['contrasena']
    tipo = request.json['tipo']
    encontrado = False
    for user in Usuarios:
        if user.getUsuario() == usuario:
            encontrado = True
            break
    if encontrado:
        return jsonify({
            'message':'Failed',
            'reason':'El usuario ya esta registrado'
            })
    else:
        nuevo = Usuario(nombre, apellido, usuario, contrasena, tipo)
        Usuarios.append(nuevo)
        return jsonify({
            'message':'Success',
            'reason':'Se ha registrado el usuario'
            })

@app.route('/Login', methods=['POST'])
def Login():
    global Usuarios
    username = request.json['usuario']
    password = request.json['contrasena']

    for user in Usuarios:
        if user.getUsuario() == username and user.getContrasena() == password:
            Dato = {
                'message':'Success',
                'usuario': user.getUsuario(),
                'tipo': user.getTipo()
                }
            break
        else:
            Dato = {
                'message':'Failed',
                'usuario': ''
                }
    respuesta = jsonify(Dato)
    return(respuesta)


@app.route('/Recetas', methods=['GET'])
def ObtenerReceta():
    global Recetas, cont_recetas
    Datos = []
    for receta in Recetas:
        Dato ={
            'id': receta.getId(),
            'autor': receta.getAutor(),
            'titulo': receta.getTitulo(),
            'resumen': receta.getResumen(),
            'ingredientes': receta.getIngredientes(),
            'preparacion': receta.getPreparacion(),
            'tiempo':  receta.getTiempo(),
            'imagen': receta.getImagen()
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Recetas', methods=['POST'])
def AgregarReceta():
    global Recetas, cont_recetas
    id = str(cont_recetas)
    autor = request.json['autor']
    titulo = request.json['titulo']
    resumen = request.json['resumen']
    ingredientes = request.json['ingredientes']
    preparacion = request.json['preparacion']
    tiempo = request.json['tiempo']
    imagen = request.json['imagen']
    nuevo = Receta(id,autor,titulo, resumen, ingredientes, preparacion, tiempo, imagen)
    Recetas.append(nuevo)
    cont_recetas += 1
    return jsonify({
        'message':'Success',
        'reason':'Se ha agregado la receta'
        })
        
@app.route('/Comentarios', methods=['POST'])
def AgregarComentario():
    global Comentarios
    id = request.json['id']
    autor = request.json['autor']
    texto = request.json['texto']
    nuevo = Comentario(id,autor, texto)
    Comentarios.append(nuevo)
    return jsonify({
        'message':'Success',
        'reason':'Se ha agregado el comentario'
        })


@app.route('/Comentarios', methods=['GET'])
def ObtenerComentarios2():
    global Comentarios
    Datos = []
    for comentario in Comentarios:
        Dato ={
            'id': comentario.getId(),
            'autor': comentario.getAutor(),
            'fecha': comentario.getFecha(),
            'texto': comentario.getTexto()
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)


@app.route('/Comentarios/<string:id>', methods=['GET'])
def ObtenerComentario(id):
    global Comentarios
    Datos = []
    for comentario in Comentarios:
        if id == comentario.getId():
            Dato ={
                'id': comentario.getId(),
                'autor': comentario.getAutor(),
                'fecha': comentario.getFecha(),
                'texto': comentario.getTexto()
                }
            Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Olvido', methods=['POST'])
def ObtenerContrasena():
    global Usuarios
    username = request.json['usuario']

    for user in Usuarios:
        if user.getUsuario() == username:
            Dato = {
                'message':'Success',
                'usuario': user.getContrasena()
                }
            break
        else:
            Dato = {
                'message':'Failed',
                'usuario': ''
                }
    respuesta = jsonify(Dato)
    return(respuesta)

@app.route('/Recetas/<string:id>', methods=['GET'])
def ObtenerRecetaId(id):
    global Recetas
    for receta in Recetas:
        if receta.getId() == id:
            Dato1 = {
                'id': receta.getId(),
                'autor': receta.getAutor(),
                'titulo': receta.getTitulo(),
                'resumen': receta.getResumen(),
                'ingredientes': receta.getIngredientes(),
                'preparacion': receta.getPreparacion(),
                'tiempo':  receta.getTiempo(),
                'imagen': receta.getImagen()
                }
            break

    respuesta = jsonify(Dato1)
    return(respuesta)
        

@app.route('/Recetas/<string:id>', methods=['PUT'])
def ActualizarReceta(id):
    global Recetas
    
    for i in range(len(Recetas)):
        if id == Recetas[i].getId():
            Recetas[i].setTitulo(request.json['titulo'])
            Recetas[i].setResumen(request.json['resumen'])
            Recetas[i].setIngredientes(request.json['ingredientes'])
            Recetas[i].setPreparacion(request.json['preparacion'])
            Recetas[i].setTiempo(request.json['tiempo'])
            Recetas[i].setImagen(request.json['imagen'])
            break
    return jsonify({
        'message':'Success',
        'reason':'Se ha modificado la receta'
    })

   

    

@app.route('/Recetas/<string:id>', methods=['DELETE'])
def EliminarReceta(id):
    global Recetas
    for i in range(len(Recetas)):
        if id == Recetas[i].getId():
            del Recetas[i]
            break
    return jsonify({'message':'Se elimino la receta exitosamente'})

    

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0",port=5000, debug=True)