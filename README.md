HVAC Symbol Backend 

This project is a small backend that allows uploading an HVAC drawing (PDF or image)
and returns a JSON response with detected HVAC symbols (mock data).

How it works:
1. Upload a file
2. The backend receives it
3. The backend returns JSON with detected symbols

Requirements:
Python 3.10 or newer (Python 3.13 works for me)

How to run:

1. Open terminal inside the project folder (HVAC-SYMBOL-BACKEND)

2. Activate virtual environment

Windows:
venv\Scripts\activate

Mac or Linux:
source venv/bin/activate

3. Install packages
pip install -r requirements.txt

4. Start the server
uvicorn app.main:app --reload

Open this link in your browser:
http://127.0.0.1:8000/docs

How to test:
1. Open /docs
2. Click POST /detect
3. Click Try it out
4. Upload any image or PDF
5. Click Execute
6. You will get JSON with detected symbols




