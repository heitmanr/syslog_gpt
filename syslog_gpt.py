#
def llm_setup():
    import openai
    from langchain.chat_models import ChatOpenAI
    #
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # Environment-Variable 'OPENAI_API_KEY' needs to be prepared
    #
    llm = ChatOpenAI(temperature=0.5, model="gpt-4")
    #
    return llm
#   
#

def get_docs():
    from langchain.document_loaders import TextLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    #
    # read text from file
    #
    loader = TextLoader('syslog.txt')
    #
    pages = loader.load_and_split()
    #
    text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            length_function=len,
        )
    docs = text_splitter.split_documents(pages)
    #
    return docs
#  
#

def get_vectordb(docs):
    from langchain.vectorstores import Chroma
    from langchain.embeddings.openai import OpenAIEmbeddings
    #
    # Store both the embeddings and the docs in ChromaDB vector store
    #
    embeddings = OpenAIEmbeddings()
    #
    vectordb = Chroma.from_documents(docs, embedding=embeddings)
    vectordb.persist()
    #
    return vectordb
#
#

#
# qa = Question & Answer ~ interactive chat
#
def get_qa(llm, vectordb):
    from langchain.memory import ConversationBufferMemory
    from langchain.chains import ConversationalRetrievalChain
    #
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    #
    qa = ConversationalRetrievalChain.from_llm(llm, vectordb.as_retriever(search_kwargs={"k": 25}), memory=memory)
    #
    return qa
#
#

def init():
    print("***\n*** Init\n***")
    print("(1) Initialze AI Language Model")
    llm = llm_setup()
    #
    print("(2a) prepare (syslog-)data")
    docs = get_docs()
    #
    print("(2b) store data in DB")
    vectordb = get_vectordb(docs)
    #
    print("(3) Setup a Conversational Retreival Chain from LLM, using the DB, with K Values of 25, and the memory")
    #
    qa = get_qa(llm, vectordb)  
    #
    return qa
#
#

#    
def loop(qa, question):
    #
    print("***\n*** Loop")
    print("***\n*** Exit at \"Further Questions?\"-Prompt by pressing [RETURN]\n***\n")
 
    #
    print("Question:",question)
 
    # process question(s)
    # - exit if no further questions
    #
    while (question!=""):
        #
        answer = qa.run(question)
        #
        print("Answer:",answer)
        #
        question = str(input("\nFurther Questions? "))
#
#

#
def main():
    qa = init()
    #    
    # prepopulate initial Question
    #
    question = "Please analyze the syslog output and provide me a summary and highlight anything important. I have been away from the office a few days and need to catch up."
    #
    # ask questions
    #
    loop(qa, question)    
#    
#

#    
if __name__ == "__main__":      
    main()  
        
        



    
    
