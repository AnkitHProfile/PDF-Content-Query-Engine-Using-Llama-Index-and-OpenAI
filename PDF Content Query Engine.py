%%capture
!pip install llama-index openai
!pip install --upgrade llama-index

import os
os.environ["OPENAI_API_KEY"] = "[Insert your API key here.]"

from llama_index.llms import openai
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from IPython.display import Markdown, display

from google.colab import files
import os
import subprocess

# Upload the PDF file
uploaded = files.upload()

# Specify the directory where you want to save the PDF file
download_dir = "data"

# Specify the desired new name for the downloaded PDF file
new_filename = "Thoughts.pdf"

# Create the directory if it doesn't exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Iterate over the uploaded files dictionary
for filename, file_content in uploaded.items():
    # Write the content to a local file
    local_filepath = os.path.join(download_dir, filename)
    with open(local_filepath, 'wb') as f:
        f.write(file_content)
    print(f"File '{filename}' uploaded and saved as '{local_filepath}'")

    # Rename the downloaded file to the desired name
    new_filepath = os.path.join(download_dir, new_filename)
    os.rename(local_filepath, new_filepath)
    print(f"File '{local_filepath}' renamed to '{new_filepath}'")

print(f"PDF downloaded and renamed successfully to {new_filename} in {download_dir}")

%%capture
!pip install pypdf

#document loader
documents = SimpleDirectoryReader("data").load_data()

len(documents)

documents[0]

# build index/vectorstore (document splitting, embedding, storing embeddings + chunks)
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

response = query_engine.query("Insert your question here.")

response

display(Markdown(f"{response}"))

index.storage_context.persist()

from llama_index.core import StorageContext, load_index_from_storage

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context=storage_context)
