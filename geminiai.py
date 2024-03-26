import pathlib
import textwrap
import os

import google.generativeai as genai

from IPython.display import Markdown


def to_markdown(text):
    
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def main_gimini(text):
    os.environ['GOOGLE_API_KEY'] = "Enter your API"

    genai.configure(api_key="Enter your API")

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text)

    # Store the text of the response
    response_text = response.text

    # Display the response
    to_markdown(response_text)

    # Save the response text to a text file
    with open('generated_text.txt', 'w') as file:
        file.write(response_text)

    print("Generated text saved to generated_text.txt")

