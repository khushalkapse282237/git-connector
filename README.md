# GitHub Connector API

A REST API built with **FastAPI** and **Python** that connects to GitHub and lets you perform real actions — fetch repositories, manage issues, view commits, and create pull requests — all through clean, documented endpoints.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Language | Python 3.11+ |
| Auth | GitHub Personal Access Token (PAT) |
| HTTP Client | Requests |
| Server | Uvicorn |
| Config | python-dotenv |

---

## Project Structure

```
github-connector/
├── main.py             # FastAPI app and all route definitions
├── github_client.py    # All GitHub API call functions
├── models.py           # Pydantic request models
├── config.py           # Loads environment variables
├── .env                # Your secret token (never commit this)
├── .env.example        # Template showing required variables
├── .gitignore          # Excludes .env, venv, pycache
├── requirements.txt    # All dependencies
└── README.md           # This file
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/khushalkapse282237/git-connector.git
cd git-connector
```

### 2. Create and activate virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your GitHub Token

Create a `.env` file in the root folder:

```bash
cp .env.example .env
```

Then open `.env` and add your token:

```
GITHUB_TOKEN=your_personal_access_token_here
```

**How to get a GitHub Personal Access Token:**
1. Go to [github.com](https://github.com) → Profile → Settings
2. Scroll to bottom → Developer Settings
3. Personal Access Tokens → Tokens (classic)
4. Generate new token → select `repo` scope
5. Copy and paste into `.env`

---

## How to Run

```bash
uvicorn main:app --reload
```

Server starts at: `http://localhost:8000`

Interactive API docs at: `http://localhost:8000/docs`

Alternative docs at: `http://localhost:8000/redoc`

---

## API Endpoints

### Health Check

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check if server is running |

**Response:**
```json
{
  "status": "running",
  "message": "GitHub Connector is live"
}
```

---

### Repositories

| Method | Endpoint | Description |
|---|---|---|
| GET | `/repos/{username}` | Fetch all public repositories for a GitHub user |

**Example:**
```
GET http://localhost:8000/repos/khushalkapse282237
```

---

### Issues

| Method | Endpoint | Description |
|---|---|---|
| GET | `/list-issues/{owner}/{repo}` | List all issues in a repository |
| POST | `/create-issue` | Create a new issue in a repository |

**List issues example:**
```
GET http://localhost:8000/list-issues/khushalkapse282237/AdmitEase
```

**Create issue payload:**
```json
{
  "owner": "khushalkapse282237",
  "repo": "AdmitEase",
  "title": "Bug: login page not loading",
  "body": "The login page throws a 500 error on submit."
}
```

---

### Commits

| Method | Endpoint | Description |
|---|---|---|
| GET | `/commits/{owner}/{repo}` | Fetch all commits from a repository |

**Example:**
```
GET http://localhost:8000/commits/khushalkapse282237/AdmitEase
```

---

### Pull Requests *(Bonus)*

| Method | Endpoint | Description |
|---|---|---|
| POST | `/create-pr` | Create a pull request in a repository |

**Payload:**
```json
{
  "owner": "khushalkapse282237",
  "repo": "AdmitEase",
  "title": "Feature: add dark mode",
  "body": "This PR adds dark mode support to the app.",
  "head": "dev",
  "base": "main"
}
```

> Note: `head` branch must have at least one commit ahead of `base` branch for PR creation to succeed.

---

## Authentication

This connector uses **GitHub Personal Access Token (PAT)** for authentication.

- The token is stored securely in a `.env` file
- It is never hardcoded in the source code
- It is excluded from version control via `.gitignore`
- All API requests send the token via the `Authorization` header:

```
Authorization: token <your_token>
```

---

## Error Handling

All endpoints return structured error responses:

| Status Code | Meaning |
|---|---|
| 200 | Success |
| 400 | Bad request or GitHub API error |
| 401 | Unauthorized — invalid or missing token |
| 403 | Forbidden — token lacks required permissions |
| 404 | Resource not found |
| 422 | Unprocessable — e.g. PR branches have no difference |

**Example error response:**
```json
{
  "detail": "404 Client Error: Not Found for url: https://api.github.com/repos/..."
}
```

---

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GITHUB_TOKEN` | Yes | Your GitHub Personal Access Token with `repo` scope |

---

## Requirements

```
fastapi
uvicorn
requests
python-dotenv
pydantic
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## Security Notes

- Never commit your `.env` file
- Never hardcode tokens in source code
- Regenerate your token immediately if accidentally exposed
- Use `.env.example` to show others what variables are needed without exposing values

---

## Author

**Khushal Kapse**
- GitHub: [@khushalkapse282237](https://github.com/khushalkapse282237)
- LinkedIn: [khushal-kapse](https://linkedin.com/in/khushal-kapse)
