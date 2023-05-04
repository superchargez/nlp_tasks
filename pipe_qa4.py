from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

# loader = TextLoader('sotu.txt')
loader = UnstructuredFileLoader("sotu.txt")
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
db = FAISS.from_documents(docs, embeddings)
query = "What did the president say about Ketanji Brown Jackson"
docs = db.similarity_search(query)
print(docs[0].page_content)
