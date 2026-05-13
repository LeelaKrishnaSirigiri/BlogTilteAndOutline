import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser

from parser import BlogOutline
from prompt import blog_prompt

load_dotenv()


def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found. Please add it to your .env file."
        )

    return ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0.7
    )


def generate_blog_outline(topic, audience, tone, blog_length):

    if not topic.strip():
        raise ValueError("Topic cannot be empty.")

    parser = PydanticOutputParser(
        pydantic_object=BlogOutline
    )

    chain = blog_prompt | get_llm() | parser

    result = chain.invoke({
        "topic": topic,
        "audience": audience if audience else "General readers",
        "tone": tone,
        "blog_length": blog_length
    })

    return result