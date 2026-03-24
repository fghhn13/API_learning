from fastapi import FastAPI
import uuid

app = FastAPI()

notes = []

@app.post("/notes")
def create_note(note: dict):
    content = note.get("content")    # 1. 从请求里拿 content
    note_id = str(uuid.uuid4())   # 2. 生成 id
    new_note = {
        "id": note_id,
        "content": content
    }
    notes.append(new_note)   # 3. 存到 notes
    return {"status": "success", "data": new_note}   # 4. 返回结果

