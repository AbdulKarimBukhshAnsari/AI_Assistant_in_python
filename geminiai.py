import pathlib
import textwrap
import os

import google.generativeai as genai

from IPython.display import Markdown


def to_markdown(text):
    
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def main_gimini(text):
    os.environ['GOOGLE_API_KEY'] = "AIzaSyAfxRvgAy1z9D0MLWyXZ6b1RHFYqg0izcw"

    genai.configure(api_key="AIzaSyAfxRvgAy1z9D0MLWyXZ6b1RHFYqg0izcw")

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text)

    # Store the text of the response
    response_text = response.text

    # Display the response
    to_markdown(response_text)

    # Save the response text to a text file
    text_exp = text.split("intelligence")
    text_exp_1 = text.split("intelligence")[1]
    with open(f"geminidata\{text_exp_1}.txt", 'w') as file:
        file.write(response_text)

    print(f"Generated text saved to geminidata folder as {text_exp_1}")

