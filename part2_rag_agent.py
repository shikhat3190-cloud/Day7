!pip install -U "langchain>=0.3.12" \
               "langchain-core>=0.3.30" \
               "langchain-community>=0.3.12" \
               "langchain-google-genai>=2.0.0" \
               "pypdf" \
               "langchain-text-splitters" \
               "chromadb"

# Get API keys from environment variables
from google.colab import userdata
import google.generativeai as genai
GEMINI_API_KEY = userdata.get("GOOGLE_API_KEY")
if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY not found. Gemini model will not run.")


## Loading PDF
from langchain_community.document_loaders import PyPDFLoader

def load_documents(pdf_paths: list):
    """Loads PDFs and returns LangChain Document objects."""
    docs = []
    for path in pdf_paths:
        loader = PyPDFLoader(path)
        docs.extend(loader.load())
    return docs

# Example usage:
#pdf_files = ["/content/Data_Analysis_FAQ_20_QA.pdf"]  # upload PDF in Colab first
pdf_files = ["/content/oci-faq.pdf"]
documents = load_documents(pdf_files)
print(f"Loaded documents: {len(documents)} pages")
print(documents)
