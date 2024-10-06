from pptx import Presentation
import docx
from PyPDF2 import PdfReader
import os

class InputParser:
    def __init__(self):
        None

    
    def process_file(self, file):
        None

    
    def parse_ppt(self, powerpoint_path):
        ppt = Presentation(powerpoint_path) 

        text = ""
        
        # write text from powerpoint file into .txt file 
        for slide in ppt.slides:  
            for shape in slide.shapes:  
                if not shape.has_text_frame:  
                    continue 
                for paragraph in shape.text_frame.paragraphs:  
                    for run in paragraph.runs:  
                        text += run.text
        
        return text


    def parse_word(self, word_path):
        doc = docx.Document(word_path)

        text = ""

        for para in doc.paragraphs:
            text += para.text

        return text
    

    def parse_pdf(self, pdf_path):
        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text


if __name__ == "__main__":
    file = r"C:\Users\andre\OneDrive\Documents\Programming Projects\MruHacksSmartQuiz\Smart-Quiz\Academic Transcript 2024.pdf"

    input_parser = InputParser()
    
    print(input_parser.parse_pdf(file))
