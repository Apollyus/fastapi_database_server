import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [stocks, setStocks] = useState([]);
  const [newStock, setNewStock] = useState({ date: '', trans: '', symbol: '', qty: '', price: '' });


  const fetchStocks = async () => {
    const response = await fetch('http://localhost:8000/stocks');
    const data = await response.json();
    setStocks(data);
  }

  const handleInputChange = (event) => {
    setNewStock({ ...newStock, [event.target.name]: event.target.value });
  }

  const addStock = async (event) => {
    event.preventDefault();
  
    const response = await fetch('http://localhost:8000/add_stocks', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newStock),
    });
  
    const data = await response.json();
  
    // If the request was successful, add the new stock to your state
    if (response.ok) {
      setStocks([...stocks, data]);
    } else {
      // Handle error
      console.error(data);
    }
  
    // Clear the form
    setNewStock({ date: '', trans: '', symbol: '', qty: '', price: '' });
  }

  return (
    <div>
      <h1 className='font-serif'>Hello world!</h1>
      <button onClick={fetchStocks}>Fetch Stocks</button>
      {stocks && stocks.map((stock, index) => (
        <div key={index}>
          <p>Date: {stock.date}</p>
          <p>Transaction: {stock.trans}</p>
          <p>Symbol: {stock.symbol}</p>
          <p>Quantity: {stock.qty}</p>
          <p>Price: {stock.price}</p>
        </div>
      ))}
      <form onSubmit={addStock}>
  <input name="date" value={newStock.date} onChange={handleInputChange} placeholder="Date" />
  <input name="trans" value={newStock.trans} onChange={handleInputChange} placeholder="Transaction" />
  <input name="symbol" value={newStock.symbol} onChange={handleInputChange} placeholder="Symbol" />
  <input name="qty" value={newStock.qty} onChange={handleInputChange} placeholder="Quantity" />
  <input name="price" value={newStock.price} onChange={handleInputChange} placeholder="Price" />
  <button type="submit">Add Stock</button>
</form>
    </div>
  )
}

export default App