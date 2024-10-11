
class Biblioteca:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.libros = []

    def buscar_libro(self, isbn):
        return next((libro for libro in self.libros if libro.isbn == isbn), None)

    def prestar_libro(self, isbn, usuario):
        libro = self.buscar_libro(isbn)
        if libro and libro.n_copias > 0:
            libro.n_copias -= 1
            return (libro.isbn, usuario.n_identific)
        return None

    def devolver_libro(self, prestamo):
        libro = self.buscar_libro(prestamo.isbn)
        if libro:
            libro.n_copias += 1
            prestamo.entregado = True

