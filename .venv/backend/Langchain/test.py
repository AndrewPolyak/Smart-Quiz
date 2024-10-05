# Make a quiz from a pdf using AI 
# How to import a file into the code
# Feed the imported file into an AI
# Get AI to quiz you based on this file

# Import required files
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import Groq
from langchain.chains import LLMChain

# Load your file (change 'your_file.txt' to your actual file path)
loader = TextLoader('notes.txt')
documents = loader.load()

# Split the text into manageable chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Initialize the Groq language model (make sure to set your API key and endpoint if required)
llm = Groq(api_key=os.getenv('GROQ_API_KEY'), model='THE KEY')

# # Create a function to generate quiz questions
# def generate_quiz_questions(docs):
#     questions = []
#     for doc in docs:
#         # Prepare the prompt for the Groq model
#         prompt = f"Based on the following text, generate 3 quiz questions with answers:\n\n{doc.page_content}"
#         chain = LLMChain(llm=llm, prompt=prompt)
#         response = chain.run()
#         questions.append(response)
#     return questions

# # Generate quiz questions
# quiz_questions = generate_quiz_questions(docs)

# # Print out the quiz questions
# for idx, questions in enumerate(quiz_questions):
#     print(f"Questions from document chunk {idx + 1}:\n{questions}\n")