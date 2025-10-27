from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI(
    title="FastAPI REST APIs - Starter",
    description="A small starter app for building CRUD endpoints with FastAPI",
    version="0.1.0",
)

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

class Item(ItemCreate):
    id: int

# Simple in-memory store
_items: Dict[int, Item] = {}
_next_id = 1

@app.get("/", summary="Root")
def root():
    return {"message": "FastAPI starter app. See /docs for interactive API docs."}

@app.get("/items", response_model=list[Item])
def list_items():
    return list(_items.values())

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", status_code=201, response_model=Item)
def create_item(item: ItemCreate):
    global _next_id
    new_item = Item(id=_next_id, **item.dict())
    _items[_next_id] = new_item
    _next_id += 1
    return new_item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate):
    existing = _items.get(item_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = Item(id=item_id, **item.dict())
    _items[item_id] = updated
    return updated

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    del _items[item_id]
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

