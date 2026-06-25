from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma


embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

loader = DirectoryLoader(
    "documents",
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

vector_db = Chroma.from_documents(
    docs,
    embedding,
    persist_directory="chroma_db"
)


def retrieve(query):
    results = vector_db.similarity_search(query, k=2)
    return "\n".join([doc.page_content for doc in results])