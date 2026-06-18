from fastapi import FastAPI

app = FastAPI()

all_customers = [
    {"id": "101", "name": "Karan", "city": "bengaluru", "risk": "low"},
    {"id": "102", "name": "Om", "city": "mumbai", "risk": "high"},
    {"id": "103", "name": "Jay", "city": "bengaluru", "risk": "low"},
    {"id": "104", "name": "Krutik", "city": "mumbai", "risk": "high"},
    {"id": "105", "name": "Yash", "city": "delhi", "risk": "low"},
]

@app.get("/customers")
def get_customers(city:str, risk : str):
    filtered = [
        c for c in all_customers
            if c["city"] == city and c["risk"] == risk
        ]

    return {
        "city" : city,
        "risk" : risk,
        "count":len(filtered),
        "results" : filtered
}