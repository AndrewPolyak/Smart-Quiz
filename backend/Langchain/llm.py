from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Optional

API_KEY = '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'
model = 'llama3-70b-8192'

class MultipleChoiceQuestion(BaseModel):
    question1: Optional[str] = Field(default=None, description="a question based on the context of the input and 4 answers")
    question2: Optional[str] = Field(default=None, description="a question based on the context of the input and 4 answers")
    question3: Optional[str] = Field(default=None, description="a question based on the context of the input and 4 answers")
    question4: Optional[str] = Field(default=None, description="a question based on the context of the input and 4 answers")
    question5: Optional[str] = Field(default=None, description="a question based on the context of the input and 4 answers")
    question6: Optional[str] = Field(default=None, description="a question based on the context of the input and 4 answers")
    question7: Optional[str] = Field(default=None, description="a question based on the context of the input and 4 answers")
    question8: Optional[str] = Field(default=None, description="a question based on the context of the input and 4 answers")
    question9: Optional[str] = Field(default=None, description="a question based on the context of the input and 4 answers")
    question10: Optional[str] = Field(default=None, description="a question based on the context of the input and 4 answers")


class LLM:
    def __init__ (self, api_key, model):
        self.api_key = api_key
        self.model = model
        self.llm = ChatGroq(api_key=api_key, model=model)

    def generate_questions(self, content):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert quiz compiler. You will ingest a massive amount of text representing a student's lecture. You will critically examine all of the text and then generate a multiple choice quiz that will assess the user's knowledge of the provided subject matter."
                    "Generate 10 questions for the user and provide 4 multiple choice questions, with only one of the answers being correct."
                    "Format the response as follows: create a JSON that contains questions, and for each question 4 answers, and for each answer a true or false value for whether it is correct or not. Generate this JSON only with no other text response attached to your output. I am only intereted in your JSON output."
                    "The information in the questions - and the answer - should exclusively be based on "
                    '''
                    "questions":\n
                    "question": "What is the capital of France?",\n
                    "answers":\n
                    "answer": "Paris",\n
                    "is_correct": true\n
                    "answer": "London",\n
                    "is_correct": false\n
                    "answer": "Berlin",\n
                    "is_correct": false\n
                    "answer": "Madrid",\n
                    "is_correct": false\n
                    '''
                ), 
                (
                    "human", "{text}"
                ),
            ]
        )

        # Create a JSON output parser
        parser = JsonOutputParser(pydantic_object=MultipleChoiceQuestion)

        # Create a chain to prompt the LLM with the template
        chain = prompt | self.llm | parser

        # Recieve an output from the LLM
        output = chain.invoke({"text": content}, )
        return output
    

if __name__=="__main__":
    llm = LLM(api_key=API_KEY, model=model)

    content = """
HTML (HyperText Markup Language) is the standard language used to create and structure content on the web. It provides the basic building blocks for designing web pages by defining the structure of the content, such as headings, paragraphs, links, images, and multimedia elements. HTML uses a system of tags, which are enclosed in angle brackets (e.g., <h1>, <p>, <a>), to specify how different parts of a webpage should be displayed. It works in combination with CSS (Cascading Style Sheets) to control the appearance and JavaScript for interactive behavior. As the backbone of web development, HTML ensures that webpages are readable and accessible across all browsers and devices.
"""

    print(llm.generate_questions(content=content))