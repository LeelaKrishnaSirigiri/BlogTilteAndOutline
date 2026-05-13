# Blog Topic & Outline Generator

## Overview

The Blog Topic & Outline Generator is a Generative AI application that helps writers, marketers, students, and content creators generate engaging blog titles and logically structured article outlines from a given topic or niche.

The application uses Large Language Models (LLMs) to generate:
- A compelling blog title
- Structured blog outline sections
- Target audience
- Writing goal

This project is built using Streamlit, LangChain, Groq LLM, and Pydantic.

---

# Features

- Generate SEO-friendly blog titles
- Create structured blog outlines
- Support for broad and narrow topics
- Automatic audience inference if audience is not provided
- Multiple writing tone options
- Blog length customization
- Structured JSON output
- Clean and interactive Streamlit UI

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| Streamlit | Web Application UI |
| LangChain | Prompt Management & LLM Chaining |
| Groq API | Large Language Model Inference |
| Pydantic | Structured Output Validation |
| dotenv | Environment Variable Management |

---

# Project Structure

```text
blog-topic-generator/
│
├── app.py
├── model.py
├── prompt.py
├── parser.py
├── requirements.txt
├── .env
└── README.md
```

---

# How It Works

1. User enters:
   - Blog topic
   - Target audience
   - Writing tone
   - Blog length

2. Prompt Template sends structured instructions to the LLM.

3. Groq LLM generates:
   - Blog title
   - Outline sections
   - Audience
   - Writing goal

4. Pydantic validates and structures the output.

5. Results are displayed in JSON format using Streamlit.

---

# Expected Output Format

```json
{
  "blog_title": "How Artificial Intelligence is Transforming Healthcare",
  "outline_sections": [
    "Introduction to AI in Healthcare",
    "Major Applications of AI in Hospitals and Diagnosis",
    "Benefits of AI for Doctors and Patients",
    "Challenges and Ethical Concerns",
    "Future of AI in Healthcare",
    "Conclusion"
  ],
  "target_audience": "General readers interested in technology",
  "writing_goal": "Provide an informative overview of AI applications in healthcare."
}
```

---

# Installation

## Clone Repository

```bash
git clone <your-github-repo-link>
cd blog-topic-generator
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Deployment

This project can be deployed using:
- Streamlit Community Cloud
- Hugging Face Spaces
- Render

---

# Test Cases Covered

✅ Broad topic handling  
✅ Narrow topic handling  
✅ Missing audience handling  
✅ Structured JSON output  
✅ Error handling  

---

# Example Inputs

## Broad Topic

```text
Topic: Digital Marketing
Audience: Beginners
```

## Narrow Topic

```text
Topic: Benefits of Yoga for College Students During Exam Stress
Audience: Students
```

## Missing Audience

```text
Topic: Artificial Intelligence in Healthcare
Audience:
```

---

# Future Improvements

- Export blog outline as PDF
- Add multilingual support
- Generate complete blog articles
- Add SEO keyword suggestions
- Add dark mode UI
- Add downloadable JSON output

---

# Author

Leela Krishna Sirigiri

---

# License

This project is developed for educational and learning purposes.
