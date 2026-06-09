from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Тимчасова база даних у пам'яті
db_notes = {}
next_id = 1

# Модель даних для перевірки вхідного JSON
class NoteSchema(BaseModel):
    text: str

@app.post("/notes", status_code=201)
def create_note(note: NoteSchema):
    """Ендпоінт для створення нотатки."""
    global next_id
    note_id = next_id
    db_notes[note_id] = note.text
    next_id += 1
    return {"id": note_id, "text": note.text}

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """Ендпоінт для отримання нотатки за ID."""
    if note_id not in db_notes:
        raise HTTPException(status_code=404, detail="Нотатку не знайдено")
    return {"id": note_id, "text": db_notes[note_id]}