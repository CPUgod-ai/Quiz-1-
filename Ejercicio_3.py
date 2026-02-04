class SistemaRecomendacion:
    def __init__(self):
        self.compras_por_usuario = {} #La clave es el usuario 
        self.usuarios_por_producto = {} #la clave es el producto

    def agregar_compra(self, usuario, producto):
        #Verifica si el usuario no existe aun
        if usuario not in self.compras_por_usuario:
            self.compras_por_usuario[usuario] = set()  #Se crea un conjunto vacío para guardar los productos

        # Agrega el producto a las compras del usuario.
        self.compras_por_usuario[usuario].add(producto)

        # Verifica si el producto no existe en el diccionario.
        if producto not in self.usuarios_por_producto:
            self.usuarios_por_producto[producto] = set() #Se crea un conjunto vacio para guardar usuarios

        # Se agrega el usuario a las personas que compraron ese producto
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

       
        return recomendaciones

sistema = SistemaRecomendacion()

sistema.agregar_compra("Ana", "Pan")
sistema.agregar_compra("Ana", "Leche")

sistema.agregar_compra("Juan", "Pan")
sistema.agregar_compra("Juan", "Huevos")

sistema.agregar_compra("Luis", "Leche")
sistema.agregar_compra("Luis", "Huevos")

print("Recomendaciones para Ana:", sistema.obtener_recomendaciones("Ana"))
print("Recomendaciones para Juan:", sistema.obtener_recomendaciones("Juan"))
print("Recomendaciones para Luis:", sistema.obtener_recomendaciones("Luis"))

