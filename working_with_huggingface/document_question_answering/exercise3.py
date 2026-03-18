""" 
- Import the required class from `pypdf` and use it to load the PDF file.
- Access each page and extract its content using the correct method.
"""
from pypdf import PdfReader

# Extract text from the PDF
reader = PdfReader("US_Employee_Policy.pdf")

# Extract text from all pages
document_text = ""
for page in reader.pages: 
    document_text += page.extract_text()

print(document_text)