import unittest
# Імпортуємо клас із нашого пакета src
from src.notes import NoteManager


class TestNoteManager(unittest.TestCase):

    def setUp(self):
        """Метод виконується перед кожним окремим тестом."""
        # Створюємо менеджер для кожного тесту,
        # щоб тести були ізольованими і не впливали один на одного.
        self.manager = NoteManager()

    def test_add_note_success(self):
        """Перевірка успішного додавання нотатки."""
        note_id = self.manager.add_note("Купити молоко")

        # Перевіряємо, що ID повернувся (1 для першої нотатки)
        self.assertEqual(note_id, 1)
        # Перевіряємо, чи текст зберігся правильно
        self.assertEqual(self.manager.get_note(note_id), "Купити молоко")

    def test_add_multiple_notes(self):
        """Перевірка додавання кількох нотаток. ID мають збільшуватися"""
        id1 = self.manager.add_note("Перша нотатка")
        id2 = self.manager.add_note("Друга нотатка")

        self.assertEqual(id1, 1)
        self.assertEqual(id2, 2)
        self.assertEqual(len(self.manager.notes), 2)

    def test_add_note_wrong_type_raises_error(self):

        with self.assertRaises(TypeError):
            self.manager.add_note(12345)  # Передаємо число замість рядка

    def test_get_non_existent_note_raises_error(self):
        """Перевірка запиту нотатки, якої немає в базі"""
        with self.assertRaises(ValueError):
            self.manager.get_note(999)  # Такого ID не існує

    def test_update_note_success(self):
        """Перевірка успішної зміни тексту нотатки"""
        note_id = self.manager.add_note("Старий текст")

        # Змінюємо текст
        self.manager.update_note(note_id, "Новий текст")

        # Перевіряємо, чи текст дійсно оновився
        self.assertEqual(self.manager.get_note(note_id), "Новий текст")

    def test_update_non_existent_note_raises_error(self):
        """Перевірка спроби змінити нотатку, якої немає"""
        with self.assertRaises(ValueError):
            self.manager.update_note(999, "Текст")


if __name__ == "__main__":
    unittest.main()