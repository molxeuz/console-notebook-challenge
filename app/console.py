
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

        opcion = Prompt.ask("\n Seleccione una opcion: ", choices=["1", "2", "3", "4", "5", "6", "7", "8"])

        return opcion

    def ejecutar(self):
            while True:
                opcion = self.mostrar_menu()

                match opcion:

                    case "1":
                        title = Prompt.ask("Ingrese el título de la nota: ")
                        text = Prompt.ask("Ingrese el texto de la nota: ")
                        importance = Prompt.ask("Ingrese la importancia (HIGH, MEDIUM, LOW): ",
                                                choices=["HIGH", "MEDIUM", "LOW"])
                        self.notebook.add_note(title, text, importance)

                    case "2":
                        for note in self.notebook.notes:
                            print(note)

                    case "3":
                        code = Prompt.ask("Ingrese el código de la nota: ")
                        tag = Prompt.ask("Ingrese la etiqueta a agregar: ")
                        for note in self.notebook.notes:
                            if note.code == code:
                                note.add_tag(tag)

                    case "4":
                        important_notes = self.notebook.important_notes()
                        for note in important_notes:
                            print(note)

                    case "5":
                        code = int(Prompt.ask("Ingrese el código de la nota a eliminar: "))
                        self.notebook.delete_note(code)

                    case "6":
                        tag = Prompt.ask("Ingrese la etiqueta para filtrar notas: ")
                        notes_with_tag = self.notebook.notes_by_tag(tag)
                        for note in notes_with_tag:
                            print(note)

                    case "7":
                        most_common_tag = self.notebook.tag_with_most_notes()
                        print(f"La etiqueta con más notas es: {most_common_tag}")

                    case "8":
                        self.consola.print("Gracias por visitar!")
                        break