# My First Python Project

A minimal Python project demonstrating environment variable configuration, secret handling, and dependency management.

## Features

- Loads configuration from a `.env` file.
- Checks that required environment variables are set.
- Reports whether an API key is configured without printing the key.
- Uses `python-dotenv` and `requests`.

## Requirements

- Python 3.10 or newer
- pip

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/stylerok/test.git
   cd test
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment.

   **Windows PowerShell:**

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**

   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Create your local `.env` file by copying `.env.example`.

   **Windows PowerShell:**

   ```powershell
   Copy-Item .env.example .env
   ```

   **macOS/Linux:**

   ```bash
   cp .env.example .env
   ```

6. Open `.env` and set the required values:

   ```dotenv
   APP_NAME=My First Python Project
   API_KEY=your_api_key_here
   ```

   Replace the placeholder with your actual API key if you have one. Never commit `.env` or share real API keys publicly.

## Usage

Run the application:

```bash
python main.py
```

Expected output:

```text
Application: My First Python Project
API key configured: True
```

The application displays whether the API key is configured, but never prints the key itself.

## Environment Variables

| Variable | Description | Required |
|---|---|---|
| `APP_NAME` | Name of the application | Yes |
| `API_KEY` | API key or test value | Yes |

## Security

- `.env` contains local configuration and must not be committed.
- `.env.example` documents the required variables using placeholder values.
- `.venv/` and Python cache files are excluded through `.gitignore`.