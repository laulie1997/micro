from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change as needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Calculator endpoint
@app.get("/calculate/{operation}")
def calculate(operation: str, num1: float, num2: float):
    result = None

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return {"operation": operation, "result": result}


# http://127.0.0.1:8001
# uvicorn main:app --reload --port 8001
