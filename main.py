import os
import sys
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")

if not app_name:
    print("Error: APP_NAME is missing in .env")
    sys.exit(1)

if not api_key:
    print("Error: API_KEY is missing in .env")
    sys.exit(1)

print(f"Application: {app_name}")
print(f"API key configured: {bool(api_key)}")