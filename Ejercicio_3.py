class SistemaRecomendacion:
    def __init__(self):
        # Diccionario que guarda los productos comprados por cada usuario
        # Ejemplo: {"Ana": {"Pan", "Leche"}}
        self.compras_por_usuario = {}

        # Diccionario que guarda qué usuarios compraron cada producto
        # Ejemplo: {"Pan": {"Ana", "Juan"}}
        self.usuarios_por_producto = {}

    def agregar_compra(self, usuario, producto):
        # Si el usuario no existe en el diccionario, se crea
        if usuario not in self.compras_por_usuario:
            self.compras_por_usuario[usuario] = set()

        # Se agrega el producto al conjunto de compras del usuario
        self.compras_por_usuario[usuario].add(producto)

        # Si el producto no existe en el diccionario, se crea
        if producto not in self.usuarios_por_producto:
            self.usuarios_por_producto[producto] = set()

        # Se agrega el usuario al conjunto de usuarios que compraron ese producto
        self.usuarios_por_producto[producto].add(usuario)

    def obtener_recomendaciones(self, usuario):
        # Conjunto donde se guardarán los productos recomendados
        recomendaciones = set()

        # Si el usuario no existe, se devuelve el conjunto vacío
        if usuario not in self.compras_por_usuario:
            return recomendaciones

        # Se obtienen los productos que ya compró el usuario
        productos_usuario = self.compras_por_usuario[usuario]

        # Se recorren los productos del usuario
        for producto in productos_usuario:
            # Se obtienen los usuarios que también compraron ese producto
            usuarios_relacionados = self.usuarios_por_producto.get(producto, set())

            # Se recorren esos usuarios
            for otro_usuario in usuarios_relacionados:
                # Se evita comparar al usuario consigo mismo
                if otro_usuario != usuario:
                    # Se obtienen los productos del otro usuario
                    productos_otro = self.compras_por_usuario[otro_usuario]

                    # Se revisan esos productos
                    for prod in productos_otro:
                        # Si el usuario no lo ha comprado, se recomienda
                        if prod not in productos_usuario:
                            recomendaciones.add(prod)

        # Se devuelven las recomendaciones
        return recomendaciones


# ----------- PRUEBA DEL SISTEMA -----------

# Se crea el sistema de recomendación
sistema = SistemaRecomendacion()

# Se registran las compras de los usuarios
sistema.agregar_compra("Ana", "Pan")
sistema.agregar_compra("Ana", "Leche")

sistema.agregar_compra("Juan", "Pan")
sistema.agregar_compra("Juan", "Huevos")

sistema.agregar_compra("Luis", "Leche")
sistema.agregar_compra("Luis", "Huevos")

# Se muestran las recomendaciones
print("Recomendaciones para Ana:", sistema.obtener_recomendaciones("Ana"))
print("Recomendaciones para Juan:", sistema.obtener_recomendaciones("Juan"))
