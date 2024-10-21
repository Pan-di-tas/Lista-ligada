class Postres:
    
    def __init__(self):
        self.postres = {}
    
    def agregar_postre(self, nombre_postre, ingredientes):
        if nombre_postre in self.postres:
            print(f"El postre {nombre_postre} ya existe.")
        else:
            self.postres[nombre_postre] = ingredientes
            print(f"Postre {nombre_postre} agregado con sus ingredientes.")
    
    def eliminar_postre(self, nombre_postre):
        if nombre_postre in self.postres:
            del self.postres[nombre_postre]
            print(f"Postre {nombre_postre} eliminado.")
        else:
            print(f"El postre {nombre_postre} no se encuentra.")
    
    def mostrar_ingredientes(self, nombre_postre):
        if nombre_postre in self.postres:
            ingredientes = self.postres[nombre_postre]
            print(f"Ingredientes de {nombre_postre}: {', '.join(ingredientes)}")
        else:
            print(f"El postre {nombre_postre} no se encuentra.")
    
    def agregar_ingredientes(self, nombre_postre, nuevos_ingredientes):
        if nombre_postre in self.postres:
            self.postres[nombre_postre].extend(nuevos_ingredientes)
            print(f"Ingredientes agregados a {nombre_postre}.")
        else:
            print(f"El postre {nombre_postre} no se encuentra.")
    
    def eliminar_ingrediente(self, nombre_postre, ingrediente):
        if nombre_postre in self.postres:
            if ingrediente in self.postres[nombre_postre]:
                self.postres[nombre_postre].remove(ingrediente)
                print(f"Ingrediente {ingrediente} eliminado de {nombre_postre}.")
            else:
                print(f"El ingrediente {ingrediente} no se encuentra en {nombre_postre}.")
        else:
            print(f"El postre {nombre_postre} no se encuentra.")
    
    def mostrar_todos_postres(self):
        if self.postres:
            print("Lista de postres y sus ingredientes:")
            for postre, ingredientes in self.postres.items():
                print(f"{postre}: {', '.join(ingredientes)}")
        else:
            print("No hay postres en la lista.")

    def Menu(self):
        while True:
            print("""\n
            AGREGAR POSTRES      (1)
            ELIMINAR POSTRES     (2)
            AGREGAR INGREDIENTES N (3)                        
            ELIMINAR INGREDIENTES (4)
            ELIMINAR POSTRE      (5)
            MOSTRAR TODOS LOS POSTRES (6)
            SALIR                (7)
            """)
            
            opcion = input("Elija una opción: ")
            
            if opcion == "1":
                nombre = input("Ingrese el nombre del postre: ")
                ingredientes = input("Ingrese los ingredientes separados por coma: ").split(',')
                self.agregar_postre(nombre.strip(), [ing.strip() for ing in ingredientes])
            
            elif opcion == "2":
                nombre = input("Ingrese el nombre del postre: ")
                self.mostrar_ingredientes(nombre.strip())
            
            elif opcion == "3":
                nombre = input("Ingrese el nombre del postre: ")
                nuevos_ingredientes = input("Ingrese los nuevos ingredientes separados por coma: ").split(',')
                self.agregar_ingredientes(nombre.strip(), [ing.strip() for ing in nuevos_ingredientes])
            
            elif opcion == "4":
                nombre = input("Ingrese el nombre del postre: ")
                ingrediente = input("Ingrese el ingrediente a eliminar: ").strip()
                self.eliminar_ingrediente(nombre.strip(), ingrediente)
            
            elif opcion == "5":
                nombre = input("Ingrese el nombre del postre: ")
                self.eliminar_postre(nombre.strip())

            elif opcion == "6":
                self.mostrar_todos_postres()
            
            elif opcion == "7":
                print("Saliendo del menú.")
                break
            
            else:
                print("Opción no válida, por favor elija una opción del 1 al 7.")

key = Postres()
key.Menu()
