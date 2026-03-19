from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA
# from langchain_openai import ChatOpenAI            //If we're back using ChatGPT


# Build retriever
embeddings = HuggingFaceEmbeddings(model_name="paraphrase-multilingual-MiniLM-L12-v2")
vectorstore = Chroma(persist_directory="./nutrition_db", embedding_function=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# Build RAG chain
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key="")
# llm = ChatOpenAI(model="gpt-4o", api_key="sk-xxxxxxxxxxxxxxxx")      //If we're back using ChatGPT
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
detected_foods = ["chicken", "rice", "vegetables"]

# Run RAG chain
query = f"Analyze the nutrition of this meal: {', '.join(detected_foods)}"
answer = qa_chain.run(query)

print(answer)
