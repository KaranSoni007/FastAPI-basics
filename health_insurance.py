from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class HealthInsurance(BaseModel):
    name: str
    age: int
    income: float
    insured_amount: float


@app.post("/insurance")
def insurance(application: HealthInsurance):
    approved = (
        18 <= application.age <= 65
        and application.income >= 15000
        and application.insured_amount <= 500000
    )

    return {
        "name": application.name,
        "age": application.age,
        "income": application.income,
        "insured amount": application.insured_amount,
        "decision": "approved" if approved else "rejected",
    }
