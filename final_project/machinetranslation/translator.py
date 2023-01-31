"""
Translator to translate languages.
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create Instance

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-01-31',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#Translation functions

def english_to_french(english_text):
    """
    This function translate english to french
    """
    if english_text == "":
        return "NO INPUT PROVIDED."

    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return french_text.get("translations")[0]['translation']

def french_to_english(french_text):
    """
    This function translate french to english
    """
    if french_text == "":
        return "NO INPUT PROVIDED."

    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return english_text.get("translations")[0]['translation']
