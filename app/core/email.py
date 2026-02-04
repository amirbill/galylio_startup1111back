from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from app.core.config import settings
from pathlib import Path

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS,
    VALIDATE_CERTS=settings.VALIDATE_CERTS
)

async def send_verification_email(email: str, code: str):
    message = MessageSchema(
        subject="Account Verification",
        recipients=[email],
        body=f"Your verification code is: {code}",
        subtype=MessageType.html
    )
    fm = FastMail(conf)
    await fm.send_message(message)

async def send_reset_password_email(email: str, code: str):
    message = MessageSchema(
        subject="Password Reset - Verification Code",
        recipients=[email],
        body=f"""\u003ch2\u003ePassword Reset Request\u003c/h2\u003e
        \u003cp\u003eYour 6-digit verification code is: \u003cstrong style="font-size: 24px; color: #8B5CF6;"\u003e{code}\u003c/strong\u003e\u003c/p\u003e
        \u003cp\u003eThis code will expire in 15 minutes.\u003c/p\u003e
        \u003cp\u003eIf you didn't request this, please ignore this email.\u003c/p\u003e""",
        subtype=MessageType.html
    )
    fm = FastMail(conf)
    await fm.send_message(message)
