class NoteManager:
    def __init__(self):
        # Нотатки у вигляді словника: {note_id: text}
        self.notes = {}
        self._next_id = 1

    def add_note(self, text: str) -> int:
        """Додає нову нотатку та повертає її ID"""
        if not isinstance(text, str):
            raise TypeError("Текст нотатки має бути рядком (string)")

        note_id = self._next_id
        self.notes[note_id] = text
        self._next_id += 1
        return note_id

    def get_note(self, note_id: int) -> str:
        """Повертає текст нотатки за її ID. Якщо не знайдено — ValueError"""
        if note_id not in self.notes:
            raise ValueError(f"Нотатку з ID {note_id} не знайдено.")
        return self.notes[note_id]

    def update_note(self, note_id: int, new_text: str) -> None:
        """Змінює текст існуючої нотатки"""
        if note_id not in self.notes:
            raise ValueError(f"Неможливо оновити. Нотатку з ID {note_id} не знайдено.")
        if not isinstance(new_text, str):
            raise TypeError("Новий текст має бути рядком (string)")

        self.notes[note_id] = new_text