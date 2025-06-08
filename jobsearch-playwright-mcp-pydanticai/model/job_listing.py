from pydantic import BaseModel


class JobListing(BaseModel):
    title: str
    company: str
    location: str
    description: str
    skills: list[str]
    job_type: str
    date_posted: str
    link: str
