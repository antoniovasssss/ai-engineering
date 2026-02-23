""" 
Create the instructions, with the directions to infer the language and the number of sentences of the given delimited text; then if the text contains more than one sentence, generate a suitable title for it, otherwise, write 'N/A' for the title.

Create the output_format, with directions to include the text, language, number of sentences, and title, each on a separate line,and ensure to use 'Text:', 'Language:', and 'Title:' as prefixes for each line.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY") # retieves the value of the OPENAI_... environment variableand stores it in the api_key variable

# Optional: check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# OpenAI client
client = OpenAI(api_key=api_key) 

def get_response(prompt):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content":prompt}]
    )
    return response.choices[0].message.content

text = """
Le réchauffement climatique est l'un des défis les plus pressants de notre époque. 
Les scientifiques du monde entier s'accordent à dire que les activités humaines, 
notamment la combustion des combustibles fossiles et la déforestation, contribuent 
de manière significative à l'augmentation des températures mondiales.
"""

# Create the instructions
instructions = (
    "Determine the language of the given text and count the number of sentences it contains. "
    "If the text has more than one sentence, generate a suitable title for it. "
    "If the text has only one sentence, write 'N/A' for the title. "
    "The text will be provided inside triple backticks.\n\n"
)

# Create the output format
output_format = (
    "Output format:\n"
    "Text:\n"
    "Language:\n"
    "Number of sentences:\n"
    "Title:\n\n"
)

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)