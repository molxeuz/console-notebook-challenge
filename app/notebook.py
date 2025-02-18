from datetime import datetime

class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str):
        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: datetime = datetime.now()
        self.tags: list[str] = []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"

class Notebook:

    def __init__(self):
        self.notes: list[str] = []

    def add_note(self, title: str, text: str, importance: str) -> int:

        existing_codes = {note.code for note in self.notes}
        new_code = 1
        while new_code in existing_codes:
            new_code += 1

        new_note = Note(new_code, title, text, importance)

        self.notes.append(new_note)

        return new_code

    def delete_note(self, code: int):

        for note in self.notes:
            if note.code == code:
                self.notes.remove(note)
                break

    def important_notes(self) -> list[Note]:

        important_notes_list = []

        for note in self.notes:

            if note.importance == "HIGH" or note.importance == "MEDIUM":
                important_notes_list.append(note)

        return important_notes_list

    def notes_by_tag(self, tag: str) -> list[Note]:

        notes_with_tag = []

        for note in self.notes:
            if tag in note.tags:
                notes_with_tag.append(note)

        return notes_with_tag

    def tag_with_most_notes(self) -> str:

        tag_counts = {}

        for note in self.notes:
            for tag in note.tags:
                if tag in tag_counts:
                    tag_counts[tag] += 1
                else:
                    tag_counts[tag] = 1

        if not tag_counts:
            return ""

        most_common_tag = max(tag_counts, key=tag_counts.get)

        return self.consola.print(f"[green] Etiqueta mas comun {most_common_tag} [/green]")
