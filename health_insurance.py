from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class HealthInsurance(BaseModel):
    name: str
    age: int
    income: int
    insured_amount: int


@app.post("/insurance")
def insurance(application: HealthInsurance):
    approved = (
        application.age > 50
        and application.income < 10000
        and application.insured_amount < 100000
    )

    return {
        "name": application.name,
        "age": application.age,
        "income": application.income,
        "insured amount": application.insured_amount,
        "decision": "approved" if approved else "rejected",
    }
