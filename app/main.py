from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from models import Bill
import controllers

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/addBill")
async def add_bill_to_db(
    request: Request,
    description: str = Form(...),
    cost: float = Form(...),
    payment_date: str = Form(...),
    payment_type: str = Form(...),
    payment_recurring: bool = Form(False)

):
    bill = Bill(description, cost, payment_date, payment_type, payment_recurring)
    controllers.add_bill(bill.json_bill())

    return templates.TemplateResponse(
        "bill_added.html",
        {"request": request, "description": description},
        status_code=200
    )


