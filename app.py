
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="AI Shopping Assistant",
    page_icon="🛍️",
    layout="wide"
)

# ======================================================
# TITLE
# ======================================================

st.title("🛍️ AI Shopping Assistant")

st.caption("Powered by OpenAI + LangChain + Streamlit")

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.title("Configuration")

api_key = st.sidebar.text_input(
    "Enter OpenAI API Key",
    type="password"
)

temperature = st.sidebar.slider(
    "Creativity",
    min_value=0.0,
    max_value=1.0,
    value=0.7
)

# ======================================================
# VALIDATE API KEY
# ======================================================

if not api_key:
    st.warning("Please enter your OpenAI API Key")
    st.stop()

# ======================================================
# SESSION STATE
# ======================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ======================================================
# LLM
# ======================================================

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=temperature,
    openai_api_key=api_key
)

# ======================================================
# PROMPT TEMPLATE
# ======================================================

prompt = ChatPromptTemplate.from_template("""
You are an expert AI shopping assistant.

Your responsibilities:
- Recommend products
- Compare products
- Suggest best value items
- Explain pros and cons
- Suggest latest technology products
- Give professional buying advice

User Question:
{question}

Instructions:
- Give detailed answer
- Mention important features
- Mention approximate pricing
- Compare alternatives if needed
- Keep response conversational
""")

# ======================================================
# OUTPUT PARSER
# ======================================================

parser = StrOutputParser()

# ======================================================
# CHAIN
# ======================================================

chain = prompt | llm | parser

# ======================================================
# DISPLAY CHAT HISTORY
# ======================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ======================================================
# USER INPUT
# ======================================================

query = st.chat_input(
    "Ask about any product..."
)

# ======================================================
# MAIN FLOW
# ======================================================

if query:

    # USER MESSAGE
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    with st.chat_message("user"):

        st.markdown(query)

    # ==================================================
    # GENERATE LLM RESPONSE
    # ==================================================

    try:

        response = chain.invoke({
            "question": query
        })

    except Exception as e:

        response = f"Error: {str(e)}"

    # ==================================================
    # STORE RESPONSE
    # ==================================================

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # ==================================================
    # DISPLAY RESPONSE
    # ==================================================

    with st.chat_message("assistant"):

        st.markdown(response)
