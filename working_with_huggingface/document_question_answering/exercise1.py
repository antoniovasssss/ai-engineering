from pypdf import PdfReader

reader=PdfReader("/Downloads/US-Employee_Policy.pdf") # Replace with the path to your PDF file

document_text=""
for page in reader.pages:
    document_text += page.extract_text()
