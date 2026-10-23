import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")

if not app_name or not api_key:
    raise ValueError("APP_NAME and API_KEY must be set in .env")

print(f"Application: {app_name}")
print(f"API key configured: {bool(api_key)}")