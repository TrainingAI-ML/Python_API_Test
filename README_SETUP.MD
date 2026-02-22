# Create Virtual Environment
|-- python -m venv venv
## Activate Virtual Environment
|--|--venv\Scripts\activate
### Install Dependencies
|--|--|-- pip install -r requirements.txt

# Run the Application
|--uvicorn app.main:app --reload --port 8001 (with your specific ports)
|--uvicorn app.main:app --reload (with your default ports)


# Summary (One Line Each)
|-- venv → Isolated environment
|--|-- activate → Use that environment
|--|--|-- pip install → Install dependencies
|--|--|--|-- uvicorn → Run the API server