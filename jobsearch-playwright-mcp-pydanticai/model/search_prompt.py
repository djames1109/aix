from pydantic import BaseModel


class JobSearchPrompt(BaseModel):
    query: str
    skills: list[str]
    preferred_location: list[str]
    job_titles: list[str]
    preferred_job_types: list[str]


