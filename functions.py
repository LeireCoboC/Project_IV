# Load required libraries

import json
import requests
import PyPDF2
import easyocr
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


def summarize_pdf_eng(path): 
    '''It summarizes the content found in the image given.'''
    
    # Extract the text from the given file
    full_text = read_pdf(path)
       
    # Use a chatbot with an API key
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzk2Y2QzNzgtZDhlZS00MzkxLWJmYmMtNzg1N2I0NWJjMDYyIiwidHlwZSI6ImFwaV90b2tlbiJ9.BIwMWdaPNAcVM6yhNbLMD2SDbmTxfis_Emd6HUYfVME"}

    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": full_text,
        "chatbot_global_action": f"""Act as a paralegal who has to summarize different models of wills from different countries.
                                  You have to return a summary in a single paragraph using connectors and including all these chacteristics:
                                 
                                   - Identification of the testator: full name, date of birth, nationality and address.
                                   - Date of execution: Day, month and year in which the will is drawn up.
                                   - Declaration of capacity: Affirmation that the testator is of legal age and of sound mind.
                                   - Goods: List the assets (property, money, investments, etc.) that the testator intends to distribute.
                                   - Debts: Include any outstanding debts or liabilities.
                                   - Beneficiaries: Specify who will inherit from the testament. Include their names and relationships to the testator.
                                   - Appointment of heirs: Identification of the persons to whom the inheritance is left and in what proportion.
                                   - Designation of assets: Specification of the assets and how they will be distributed among the heirs.
                                   - Appointment of executor: Person in charge of carrying out the provisions of the will.
                                   - Guardianship and custody of minor children: In case of having minor children, it must be designated who will take care of them.
                                   - Witnesses: Note the names and signatures of witnesses who observed the testament's execution.
                                   - Testator's signature: Confirm that the testator signed the document.
                                   If there is any field that you do not have the information, return 'unspecified information'. """,

        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 1000,
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    return result['openai']['generated_text']


def summarize_Img_eng(path): 
    '''It summarizes the content found in the image given.'''
    
    # Extract the text from the given image
    full_text = read_Img(path)
       
    # Use a chatbot with an API key
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzk2Y2QzNzgtZDhlZS00MzkxLWJmYmMtNzg1N2I0NWJjMDYyIiwidHlwZSI6ImFwaV90b2tlbiJ9.BIwMWdaPNAcVM6yhNbLMD2SDbmTxfis_Emd6HUYfVME"}

    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": full_text,
        "chatbot_global_action": f"""Act as a paralegal who has to summarize different models of wills from different countries.
                                  You have to return a summary in a single paragraph using connectors and including all these chacteristics:
                                 
                                   - Identification of the testator: full name, date of birth, nationality and address.
                                   - Date of execution: Day, month and year in which the will is drawn up.
                                   - Declaration of capacity: Affirmation that the testator is of legal age and of sound mind.
                                   - Goods: List the assets (property, money, investments, etc.) that the testator intends to distribute.
                                   - Debts: Include any outstanding debts or liabilities.
                                   - Beneficiaries: Specify who will inherit from the testament. Include their names and relationships to the testator.
                                   - Appointment of heirs: Identification of the persons to whom the inheritance is left and in what proportion.
                                   - Designation of assets: Specification of the assets and how they will be distributed among the heirs.
                                   - Appointment of executor: Person in charge of carrying out the provisions of the will.
                                   - Guardianship and custody of minor children: In case of having minor children, it must be designated who will take care of them.
                                   - Witnesses: Note the names and signatures of witnesses who observed the testament's execution.
                                   - Testator's signature: Confirm that the testator signed the document.
                                   If there is any field that you do not have the information, return 'unspecified information'. """,

        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 1000,
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    return result['openai']['generated_text']