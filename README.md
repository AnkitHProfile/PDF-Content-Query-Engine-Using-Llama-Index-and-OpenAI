# PDF-Content-Query-Engine-Using-Llama-Index-and-OpenAI
This Python script leverages the power of Llama-Index and OpenAI to create a robust PDF content query engine. The code automates the process of uploading a PDF, renaming it, and extracting its content for querying.

The script begins by installing necessary packages and setting up the OpenAI API key for authentication. It then handles the file upload and storage, ensuring the PDF is saved in a specified directory with a specific filename. Using the SimpleDirectoryReader from Llama-Index, the PDF content is loaded and processed into documents.

The core functionality revolves around creating a VectorStoreIndex from these documents, which allows for efficient querying of the PDF content. A query engine is instantiated to handle user queries, providing detailed responses. The index is then persisted for future use, ensuring that the data is stored and can be reloaded efficiently.

The script concludes by demonstrating how to reload the stored index, making the solution both scalable and reusable. This approach ensures that users can easily extract and query information from PDFs, making it a valuable tool for researchers, students, and professionals.
