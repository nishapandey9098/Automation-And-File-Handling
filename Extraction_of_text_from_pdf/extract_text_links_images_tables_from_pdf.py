import PyPDF2
from PyPDF2 import PdfReader
import pdfplumber
import pymupdf
reader = PdfReader("coffee.pdf")
#print(len(reader.pages))
page = reader.pages[0]
#print(page.extract_text())

for i in range(len(reader.pages)):
    page = reader.pages[i]
    print(page.extract_text())

for i in  page.images:    
   with  open(i.name, 'wb') as f:
       f.write(i.data)

with pdfplumber.open('coffee.pdf') as f:
    for i in f.pages:
        print(i.extract_tables())
        
        
doc = pymupdf.open('coffee.pdf')
print(doc.page_count)

print (doc.metadata)


page = doc.load_page(0)
print(page.get_text())

pix = page.get_pixmap()
pix.save(f"page_{page.number}.png")

links = page.get_links()
print(links)