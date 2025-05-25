import os
import streamlit as st
from dotenv import load_dotenv
from langchain.schema import HumanMessage
from models.model_factory import get_llm
from openai_key import OPENAI_API_KEY  # Your own OpenAI key module




# 🔐 2. Load OpenAI API Key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Streamlit app setup
st.set_page_config(page_title="Pick-n(LLM)-Summarize", layout="centered")

st.title("🗞️ Pick-n(LLM)-Summarize")
st.markdown("Created by **Sivaprasath Munusamy**")
# Model choice
st.subheader("🧠 Choose your model")

model_choice = st.selectbox("", [
    "OpenAI (GPT-3.5)",
    "Claude (Anthropic)",
    "LLaMA (HuggingFace)"
])

# Article input
article_text = st.text_area("Paste your news article text here:", height=300)

# Generate summary
if st.button("Get Curated Summary"):
    if not article_text.strip():
        st.error("Please paste some article text first!")
    else:
        with st.spinner("Generating summary..."):
            llm = get_llm(model_choice)

            prompt = f"Summarize the following news article into 5-6 concise bullet points:\n\n{article_text}"

            # Handle chat vs non-chat models
            if hasattr(llm, "invoke"):
                response = llm([HumanMessage(content=prompt)])
                summary = response.content
            else:
                summary = llm(prompt)

            st.subheader("📝 Curated Summary")
            st.markdown(summary)
