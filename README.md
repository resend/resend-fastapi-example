# Resend with FastAPI

This example shows how to use Resend with [FastAPI](https://fastapi.tiangolo.com/).

## Prerequisites

To get the most out of this guide, you’ll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)
* Install `virtualenv` by running `pip install virtualenv`

## Instructions

1. Create and activate a new virtual env with:

```sh
virtualenv venv
source venv/bin/activate
```

2. Install dependencies:

```sh
pip install -r requirements.txt
```

3. Set your RESEND_API_KEY environment changing the RESEND_API_KEY environment variable inside `.env` file:

```sh
RESEND_API_KEY=re_123456789
```

3. Execute the following command:

```sh
uvicorn main:app --reload
```

4. Access the URL `http://127.0.0.1:8000/docs` and try it out.

## License

MIT License