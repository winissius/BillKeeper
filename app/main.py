from fastapi import FastAPI, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from models import Bill

app = FastAPI()


@app.get("/hello")
async def root():
    return {"message": "Hello World!!!2"}


@app.get("/", response_class=HTMLResponse)
async def show_form():
    return """
        <form action="/addBill" method="post">
            Description: <input type="text" name="description"><br>
            Cost: <input type="text" name="cost"><br>
            Payment date: <input type="date" name="payment_date"><br>
            <label for="cars">Payment type:</label>
              <select name="payment_type">
                <option value="credit_card">Credit Card</option>
                <option value="debit_card">Debit Card</option>
                <option value="money">Money</option>
                <option value="bank_transfer">Bank Transfer</option>
              </select><br>
            Is it a recurring payment? <input type="checkbox" name="payment_recurring"><br>
            <input type="submit" value="Add">
        </form>
        """


@app.post("/addBill")
async def add_bill_to_db(
    description: str = Form(...),
    cost: float = Form(...),
    payment_date: str = Form(...),
    payment_type: str = Form(...),
    payment_recurring: bool = Form(...)

):
    bill = Bill(description, cost, payment_date, payment_type, payment_recurring)

    return {
        'message': 'Added Bill',
        'json': bill.json_bill()
    }


