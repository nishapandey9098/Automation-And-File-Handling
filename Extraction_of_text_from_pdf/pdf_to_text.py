import re
import PyPDF2
from PyPDF2 import PdfReader
def extract_text_from_pdf(pdf_file: str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict = False)
        pdf_text = []
        
        
        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
            
        return pdf_text


if __name__ == '__main__':
    extracted_text = extract_text_from_pdf('coffee.pdf')
    for text in extracted_text:
        print(text)
    
    coffee_count = 0
    for text in extracted_text:
        split_message = re.split(r'\s+|[,;?!.-]\s*', text.lower())
        
        if 'medimate' in split_message:
            coffee_count += 1
            
        print("medimate found:", coffee_count)
    
    
    

