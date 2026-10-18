# Packages to be installed for this RAG
    Have below libraries specified in requirements.tx
    pypdf
    openai
    pinecone
    dotenv


# Install Dependencies

    install the dependencies using below command
        'uv add -r requirements.txt'


# Run the Program

    Since UV is the package manager that has all dependencies, to run the program
    uv run main.py , insead of python main.py

# PineCone Vector

    Need to create index, have model chosen as 'text-embeddding-3-small' and dimension as '1536'
        - PINECONE_API_KEY
        - PINECONE_INDEX_NAME
