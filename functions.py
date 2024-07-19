# Load required libraries

import json
import requests
import PyPDF2
#import pytesseract
import easyocr
import gradio as gr
import os

#########################################################################
############################### FUNCTIONS ###############################
#########################################################################

def read_pdf(file_path):
    '''It extracts text from a pdf file. It takes as an input a pdf file and using PyPDF2
    library it outputs the text in string.'''

    # Create a pdf reader object and to extract text
    reader = PyPDF2.PdfReader(file_path)

    # Initialize an empty string to store the combined text
    full_text = ""

    # Iterate through all pages and extract text
    for page in reader.pages:
        full_text += page.extract_text() # extracting the text per pages
    
    return full_text


def read_Img(image_path):
    '''It extracts text from an image. It takes as an input an image and using OCR
    it outputs the text in string.'''

    # Initialize OCR object
    reader = easyocr.Reader(['en', 'es', 'fr'])
    
    # Apply OCR
    text = reader.readtext(image_path, detail=0)

    # Put together all the text
    full_text = " ".join(text)

    return full_text


def summarize_pdf(path): 
    '''It summarizes the content found in the image given.'''
    
    # Extract the text from the given file
    full_text = read_pdf(path)
       
    # Use a chatbot with an API key
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzk2Y2QzNzgtZDhlZS00MzkxLWJmYmMtNzg1N2I0NWJjMDYyIiwidHlwZSI6ImFwaV90b2tlbiJ9.BIwMWdaPNAcVM6yhNbLMD2SDbmTxfis_Emd6HUYfVME"}

    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": full_text,
        "chatbot_global_action": f"""Actua como un asistente cuya funcion es ayudar a abogados
                                 y personal legal a resumir documentos jurídicos extensos,
                                 destacando los datos más importantes para ahorrando tiempo 
                                 y esfuerzo en el análisis manual.
                                 
                                 Para la salida quiero que lo ordenes por puntos importantes, con una idea por punto y pongas Resumen: """,
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 1000,
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    return result['openai']['generated_text']


def summarize_Img(path): 
    '''It summarizes the content found in the image given.'''
    
    # Extract the text from the given image
    full_text = read_Img(path)
       
    # Use a chatbot with an API key
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzk2Y2QzNzgtZDhlZS00MzkxLWJmYmMtNzg1N2I0NWJjMDYyIiwidHlwZSI6ImFwaV90b2tlbiJ9.BIwMWdaPNAcVM6yhNbLMD2SDbmTxfis_Emd6HUYfVME"}

    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": full_text,
        "chatbot_global_action": f"""Actua como un asistente cuya funcion es ayudar a abogados
                                 y personal legal a resumir documentos jurídicos extensos,
                                 destacando los datos más importantes para ahorrando tiempo 
                                 y esfuerzo en el análisis manual.
                                 
                                 Para la salida quiero que lo ordenes por puntos importantes, con una idea por punto y pongas Resumen: """,
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 1000,
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    return result['openai']['generated_text']