import resend
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():

    params = {
        "from": "onboarding@resend.dev",
        "to": "delivered@resend.dev",
        "subject": "hello world",
        "html": "<strong>it works!</strong>",
    }

    r = resend.Emails.send(params)
    return r