import requests
from config import GITHUB_TOKEN, GITHUB_BASE_URL

def get_headers():
    return {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

def fetch_repos(username: str):
    url = f"{GITHUB_BASE_URL}/users/{username}/repos"
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()

def list_issues(owner: str, repo: str):
    url = f"{GITHUB_BASE_URL}/repos/{owner}/{repo}/issues"
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()

def create_issue(owner: str, repo: str, title: str, body: str):
    url = f"{GITHUB_BASE_URL}/repos/{owner}/{repo}/issues"
    payload = {"title": title, "body": body}
    response = requests.post(url, headers=get_headers(), json=payload)
    response.raise_for_status()
    return response.json()

def fetch_commits(owner: str, repo: str):
    url = f"{GITHUB_BASE_URL}/repos/{owner}/{repo}/commits"
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()

def create_pull_request(owner: str, repo: str, title: str, body: str, head: str, base: str):
    url = f"{GITHUB_BASE_URL}/repos/{owner}/{repo}/pulls"
    payload = {
        "title": title,
        "body": body,
        "head": head,
        "base": base
    }
    response = requests.post(url, headers=get_headers(), json=payload)
    response.raise_for_status()
    return response.json()