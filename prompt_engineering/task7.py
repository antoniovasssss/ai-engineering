""" 
Create the instructions for the prompt, asking the model to determine the language and generate a suitable title for the pre-loaded text excerpt that will be provided using triple backticks (```) delimiters.

Create the output_format with directions to include the text, language, and title, each on a separate line, using 'Text:', 'Language:', and 'Title:' as prefixes for each line.

Create the final_prompt by combining all parts and the delimited text to use.
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
    "Determine the language of the following text and generate a suitable title for it. "
    "Use the provided output format. The text will be delimited using triple backticks."
)

# Create the output format
output_format = (
    "Text:\n"
    "Language:\n"
    "Title:"
)


# Create the final prompt
prompt =f"""
{instructions}

Output format:
{output_format}

Text to analyze:
```{text}```
"""
response = get_response(prompt)
print(response)