from pptx import Presentation

class InputParser:
    def __init__(self):
        None

    def parse_ppt(self, powerpoint_path):
        ppt = Presentation(powerpoint_path) 
  
        # open file in write mode 
        writable_file = open("results.txt", "w") 
        
        # write text from powerpoint file into .txt file 
        for slide in ppt.slides:  
            for shape in slide.shapes:  
                if not shape.has_text_frame:  
                    continue 
                for paragraph in shape.text_frame.paragraphs:  
                    for run in paragraph.runs:  
                        writable_file.write(run.text) 
        
        # close the file                
        writable_file.close() 



if __name__ == "__main__":
    file = r"C:\Users\andre\OneDrive\Documents\Programming Projects\MruHacksSmartQuiz\Smart-Quiz\Hello world.pptx"

    input_parser = InputParser()
    input_parser.parse_ppt(powerpoint_path=file)
