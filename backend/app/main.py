import fastapi
import sqlite3
from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException

origins = ["*"]

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Stock(BaseModel):
    date: str
    trans: str
    symbol: str
    qty: float
    price: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/stocks", response_model=List[Stock])
def get_stocks():
    conn = sqlite3.connect('C:\\aaa_programovai_kodovani\\python_a_databaze\\backend\\databases\\mydatabase.db')
    c = conn.cursor()

    c.execute('SELECT * FROM stocks')
    stocks = c.fetchall()

    conn.close()

    return [{"date": date, "trans": trans, "symbol": symbol, "qty": qty, "price": price} for date, trans, symbol, qty, price in stocks]

@app.post("/add_stocks", response_model=Stock)
async def add_stock(stock: Stock):
    conn = sqlite3.connect('C:\\aaa_programovai_kodovani\\python_a_databaze\\backend\\databases\\mydatabase.db')
    c = conn.cursor()

    try:
        c.execute('INSERT INTO stocks (date, trans, symbol, qty, price) VALUES (?, ?, ?, ?, ?)', 
                  (stock.date, stock.trans, stock.symbol, stock.qty, stock.price))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to add stock")

    conn.close()

    return stock