from pydantic import BaseModel, Field
from typing import List


class BlogOutline(BaseModel):
    blog_title: str = Field(description="A strong and engaging blog title")
    outline_sections: List[str] = Field(description="A logical list of blog outline sections")
    target_audience: str = Field(description="The intended audience for the blog")
    writing_goal: str = Field(description="The main purpose of the blog article")