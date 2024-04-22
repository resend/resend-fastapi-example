from typing import Dict, Union, List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict
import resend

class Settings(BaseSettings):
    RESEND_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
app = FastAPI()


resend.api_key = settings.RESEND_API_KEY


class AttachmentParams(BaseModel):
    content: Union[List[str], str]
    filename: str
    path: Optional[str] = None

class TagParams(BaseModel):
    name: str
    value: Optional[str] = None

class SendParams(BaseModel):
    sender: EmailStr
    to: Union[EmailStr, List[EmailStr]]
    subject: str
    bcc: Optional[Union[EmailStr, List[EmailStr]]] = None
    cc: Optional[Union[EmailStr, List[EmailStr]]] = None
    reply_to: Optional[Union[EmailStr, List[EmailStr]]] = None
    html: Optional[str] = None
    text: Optional[str] = None
    headers: Optional[Dict[str, str]] = None
    attachments: Optional[List[AttachmentParams]] = None
    tags: Optional[List[TagParams]] = None


class EmailResponse(BaseModel):
    id: str


@app.post("/")
def send_mail(params: SendParams) -> EmailResponse:
    dict_params = params.model_dump()
    dict_params['from'] = dict_params.pop('sender')
    resp = resend.Emails.send(dict_params)
    return resp

