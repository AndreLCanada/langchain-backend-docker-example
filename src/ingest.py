import pickle
from langchain.document_loaders import SeleniumURLLoader
from langchain.document_loaders import ReadTheDocsLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def read_from_file(file_path):
    with open(file_path, 'r') as file:
        raw_documents = file.read().splitlines()
    return raw_documents


def ingest_docs():
    """Get documents from web pages."""
    file_path = 'src/document.txt'
    raw_documents = read_from_file(file_path)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    documents = text_splitter.split_text(raw_documents)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(documents, embeddings)

    # Save vectorstore
    with open("vectorstore.pkl", "wb") as f:
        pickle.dump(vectorstore, f)


if __name__ == "__main__":
    ingest_docs()
