from pptx import Presentation
import docx
from PyPDF2 import PdfReader
import os

class InputParser:
    def __init__(self):
        None

    
    def parse_ppt(self, powerpoint_path):
        '''
        Defines a method called "parse_ppt".
        '''
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
        '''
        Defines a method called "parse__pdf".
        '''
        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text


def process_file(file):
        text = ""
        
        file_name, extension = os.path.splitext(file)
        extension = extension[1:]

        parser = InputParser()

        if (extension == "pdf"):
            text = parser.parse_pdf(file)
        
        elif (extension == "docx"):
            text = parser.parse_word(file)

        elif (extension == "pptx"):
            text = parser.parse_ppt(file)

        return text
        
