from pydantic import BaseModel

class IssueRequest(BaseModel):
    owner: str
    repo: str
    title: str
    body: str = ""

class PullRequestRequest(BaseModel):
    owner: str
    repo: str
    title: str
    body: str = ""
    head: str
    base: str = "main"