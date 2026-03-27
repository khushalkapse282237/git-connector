from fastapi import FastAPI, HTTPException
import github_client
from models import IssueRequest, PullRequestRequest

app = FastAPI(title="GitHub Connector")

@app.get("/")
def health_check():
    return {"status": "running", "message": "GitHub Connector is live"}

@app.get("/repos/{username}")
def get_repos(username: str):
    try:
        return github_client.fetch_repos(username)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/list-issues/{owner}/{repo}")
def list_issues(owner: str, repo: str):
    try:
        return github_client.list_issues(owner, repo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/create-issue")
def create_issue(data: IssueRequest):
    try:
        return github_client.create_issue(data.owner, data.repo, data.title, data.body)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/commits/{owner}/{repo}")
def get_commits(owner: str, repo: str):
    try:
        return github_client.fetch_commits(owner, repo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/create-pr")
def create_pull_request(data: PullRequestRequest):
    try:
        return github_client.create_pull_request(
            data.owner, data.repo, data.title, data.body, data.head, data.base
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))