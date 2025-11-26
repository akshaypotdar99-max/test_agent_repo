import streamlit as st
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA

# Step 1: Load your OrangeHRM project
project_path = r"C:\Users\BismaMajid(Annalect)\PycharmProjects\OrangeHRM"

@st.cache_resource
def load_framework_store():
    loader = DirectoryLoader(project_path, glob="**/*.py")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    store = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory="chroma_store"
    )
    return store

# Load once
framework_store = load_framework_store()

# Step 2: Initialize Ollama
llm = OllamaLLM(model="gemma:2b")  # small enough for your system

# Step 3: Retrieval QA
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=framework_store.as_retriever()
)

# ----------------- Streamlit UI -----------------
st.title("🧪 AI Selenium Test Generator")
st.write("Enter your requirement and generate pytest + Selenium test cases from your OrangeHRM framework.")

# Text input
user_input = st.text_area("Enter requirement:", placeholder="e.g., Generate a pytest test case for Forgot Password page")

if st.button("Generate Test Case"):
    if user_input.strip():
        with st.spinner("Generating test case..."):
            answer = qa.run(user_input)
        st.subheader("✅ Generated Test Code")
        st.code(answer, language="python")
    else:
        st.warning("Please enter a requirement first!")
