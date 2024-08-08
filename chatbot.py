import google.generativeai as genai
import streamlit as st
import os
GOOGLE_API_KEY="AIzaSyDu_TOBOB2DUb3R4DiWqxh6PZclK5WYXLY"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
def getResponseFromModel(user_input):
    response=model.generate_content(user_input)
    return response.text
user_input=input("Enter your Query :")
print(getResponseFromModel(user_input))

