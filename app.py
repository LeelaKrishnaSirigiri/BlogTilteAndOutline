import streamlit as st
import json
from model import generate_blog_outline

st.set_page_config(
    page_title="Blog Topic & Outline Generator",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Blog Topic & Outline Generator")
st.write("Generate a blog title, outline, target audience, and writing goal using Generative AI.")

topic = st.text_input(
    "Enter Blog Topic or Niche",
    placeholder="Example: Artificial Intelligence in Healthcare"
)

audience = st.text_input(
    "Target Audience",
    placeholder="Example: General readers interested in technology"
)

tone = st.selectbox(
    "Writing Tone",
    ["Informative", "Professional", "Casual", "SEO-Friendly", "Academic", "Persuasive"]
)

blog_length = st.selectbox(
    "Blog Length",
    ["Short", "Medium", "Long-form"]
)

if st.button("Generate Blog Outline"):
    try:
        with st.spinner("Generating your blog outline..."):
            result = generate_blog_outline(topic, audience, tone, blog_length)

        st.success("Blog outline generated successfully!")

        st.subheader("Blog Title")
        st.write(result.blog_title)

        st.subheader("Outline Sections")
        for section in result.outline_sections:
            st.markdown(f"- {section}")
        st.subheader("Target Audience")
        st.write(result.target_audience)

        st.subheader("Writing Goal")
        st.write(result.writing_goal)

        st.subheader("JSON Output")
        st.code(
            json.dumps(result.model_dump(), indent=2),
            language="json"
)
    except Exception as e:
        st.error(f"Error: {e}")