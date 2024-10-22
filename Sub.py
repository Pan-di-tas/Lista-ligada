class Postres:
    
    def __init__(self):
        self.postres = {}
    
    def agregar_postre(self, nombre_postre, ingredientes):
        if nombre_postre in self.postres:
            print(f"El postre {nombre_postre} ya existe.")
        else:
            self.postres[nombre_postre] = ingredientes
            print(f"Postre {nombre_postre} agregado con sus ingredientes.")
    
    def eliminar_duplicados(self):
        for postre, ingredientes in self.postres.items():
            ingredientes_unicos = list(set(ingredientes))
            self.postres[postre] = ingredientes_unicos
            print(f"Duplicados eliminados en {postre}: {', '.join(ingredientes_unicos)}")

    def mostrar_todos_postres(self):
        if self.postres:
            print("Lista de postres y sus ingredientes:")
            for postre, ingredientes in self.postres.items():
                print(f"{postre}: {', '.join(ingredientes)}")
        else:
            print("No hay postres en la lista.")
    
    #etc
key = Postres()
key.agregar_postre("Tarta de Manzana", ["Manzana", "Harina", "Azúcar", "Manzana", "Canela", "Azúcar"])
key.agregar_postre("Cheesecake", ["Queso crema", "Galletas", "Queso crema", "Azúcar", "Mantequilla", "Azúcar"])
key.mostrar_todos_postres()

# Eliminar duplicados
key.eliminar_duplicados()
key.mostrar_todos_postres()
