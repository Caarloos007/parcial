class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros
        self.historial_lecturas = {}  # Historial de lecturas por usuario
        self.popularidad = {}  # Registro de popularidad de libros

    def agregar_libro(self, titulo, autor, cantidad):
        """Agrega un libro a la biblioteca."""
        if titulo in self.libros:
            self.libros[titulo]['cantidad'] += cantidad
        else:
            self.libros[titulo] = {'autor': autor, 'cantidad': cantidad}
            self.popularidad[titulo] = 0
        print(f"Libro '{titulo}' agregado exitosamente.")

    def prestar_libro(self, titulo, usuario):
        """Presta un libro a un usuario, reduciendo su cantidad disponible."""
        if titulo in self.libros and self.libros[titulo]['cantidad'] > 0:
            self.libros[titulo]['cantidad'] -= 1
            self.popularidad[titulo] += 1
            if usuario not in self.historial_lecturas:
                self.historial_lecturas[usuario] = []
            self.historial_lecturas[usuario].append(titulo)
            print(f"Libro '{titulo}' prestado a {usuario}.")
        else:
            print(f"El libro '{titulo}' no está disponible.")

    def devolver_libro(self, titulo):
        """Devuelve un libro, aumentando su cantidad disponible."""
        if titulo in self.libros:
            self.libros[titulo]['cantidad'] += 1
            print(f"Libro '{titulo}' devuelto exitosamente.")
        else:
            print(f"El libro '{titulo}' no pertenece a esta biblioteca.")

    def consultar_disponibilidad(self, titulo):
        """Consulta si un libro está disponible y cuántos ejemplares hay."""
        if titulo in self.libros:
            cantidad = self.libros[titulo]['cantidad']
            if cantidad > 0:
                print(f"El libro '{titulo}' está disponible. Ejemplares disponibles: {cantidad}.")
                return True
            else:
                print(f"El libro '{titulo}' no está disponible. Ejemplares disponibles: {cantidad}.")
                return False
        else:
            print(f"El libro '{titulo}' no existe en la biblioteca.")
            return False

    def sugerir_libro(self, usuario):
        """Sugiere el siguiente libro a leer basado en lecturas anteriores."""
        if usuario in self.historial_lecturas and self.historial_lecturas[usuario]:
            ultimo_libro = self.historial_lecturas[usuario][-1]
            autor = self.libros[ultimo_libro]['autor']
            print(f"Basado en tu última lectura '{ultimo_libro}', te sugerimos explorar otros libros del autor '{autor}'.")
        else:
            print("No hay suficientes datos para sugerir un libro.")

    def recomendar_colaborativo(self, usuario):
        """Recomienda un libro basado en preferencias de usuarios similares."""
        if usuario not in self.historial_lecturas or not self.historial_lecturas[usuario]:
            print("No hay suficientes datos para realizar una recomendación colaborativa.")
            return

        # Encuentra usuarios similares
        usuarios_similares = {}
        for otro_usuario, libros_leidos in self.historial_lecturas.items():
            if otro_usuario != usuario:
                # Calcula la similitud como la intersección de libros leídos
                similitud = len(set(self.historial_lecturas[usuario]) & set(libros_leidos))
                if similitud > 0:
                    usuarios_similares[otro_usuario] = similitud

        if not usuarios_similares:
            print("No se encontraron usuarios similares para realizar una recomendación.")
            return

        # Ordena usuarios similares por mayor similitud
        usuarios_similares = sorted(usuarios_similares.items(), key=lambda x: x[1], reverse=True)

        # Busca libros leídos por usuarios similares que el usuario actual no haya leído
        for similar, _ in usuarios_similares:
            for libro in self.historial_lecturas[similar]:
                if libro not in self.historial_lecturas[usuario]:
                    print(f"Recomendación colaborativa: Te sugerimos leer '{libro}', basado en usuarios con gustos similares.")
                    return

        print("No se encontraron libros nuevos para recomendar basados en usuarios similares.")

def menu():
    biblioteca = Biblioteca()
    usuario = input("Introduce tu nombre de usuario: ")

    while True:
        print("\n--- Menú de Biblioteca ---")
        print("1. Agregar libro")
        print("2. Tomar prestado un libro")
        print("3. Devolver un libro")
        print("4. Consultar disponibilidad de un libro")
        print("5. Ver recomendaciones de lectura")
        print("6. Recomendación colaborativa")
        print("7. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Introduce el título del libro: ")
            autor = input("Introduce el autor del libro: ")
            cantidad = int(input("Introduce la cantidad disponible: "))
            biblioteca.agregar_libro(titulo, autor, cantidad)
        elif opcion == "2":
            titulo = input("Introduce el título del libro que quieres tomar prestado: ")
            biblioteca.prestar_libro(titulo, usuario)
        elif opcion == "3":
            titulo = input("Introduce el título del libro que quieres devolver: ")
            biblioteca.devolver_libro(titulo)
        elif opcion == "4":
            titulo = input("Introduce el título del libro que quieres consultar: ")
            biblioteca.consultar_disponibilidad(titulo)
        elif opcion == "5":
            biblioteca.sugerir_libro(usuario)
        elif opcion == "6":
            biblioteca.recomendar_colaborativo(usuario)
        elif opcion == "7":
            print("¡Gracias por usar la biblioteca! Hasta pronto.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

# Ejecutar el menú
menu()