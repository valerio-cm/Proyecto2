from datetime import date
from datetime import datetime

class Comentario:
    def __init__(self, id, autor, texto):
        now = datetime.now()
        format = now.strftime('%d/%m/%Y - %H:%M:%S')
        self.fecha = format
        self.id = id
        self.autor = autor
        self.texto = texto

    def getId(self):
        return self.id
    
    def getAutor(self):
        return self.autor
    
    def getFecha(self):
        return self.fecha

    def getTexto(self):
        return self.texto

    def setId(self, id):
        self.id = id
    
    def setAutor(self, autor):
        self.autor = autor
    
    def setFecha(self, fecha):
        self.fecha = fecha

    def setTexto(self, texto):
        self.texto = texto