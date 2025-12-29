# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types

def generate():
    client = genai.Client(
        api_key="API_KEY"
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0.25,
        thinking_config=types.ThinkingConfig(
            thinking_level="Medium",
        ),
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")


import streamlit as st
from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyBG0lk7Sufde79OBWS2eyYHBSKR_LY5ndw")  # put your key

st.title("Analysis Machine Health")

query = st.text_input("Ask a question:")

if st.button("Ask"):
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=query)]
        )
    ]

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=contents
    )


    st.write(response.text)
