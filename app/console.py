
from rich.prompt import Prompt

class Console:

    def mostrar_menu(self):

        self.consola.print("\n[bold green]Tienda virtual[/bold green]")
        self.consola.print("\n 1. Agregar nota ")
        self.consola.print(" 2. Listar notas")
        self.consola.print(" 3. Agregar etiqueta a nota")
        self.consola.print(" 4. Listar notas importantes")
        self.consola.print(" 5. Eliminar nota")
        self.consola.print(" 6. Mostrar notas por etiqueta")
        self.consola.print(" 7. Mostrar etiqueta con más notas")
        self.consola.print(" 8. Salir")

        opcion = Prompt.ask("\n Seleccione una opcion: ", choices=["1", "2", "3", "4", "5", "6"])

        return opcion

    def ejecutar(self):
            while True:
                opcion = self.mostrar_menu()

                match opcion:

                    case "1":
                        
                    case "2":

                    case "3:

                    case "4":

                    case "5":

                    case "6":

                    case "7":

                    case "8":

