"""code to create an instance of the IBM Watson Language translator"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(text1):
    """This function translate english to french"""
    french_translation = language_translator.translate(
    text=text1,
    model_id='en-fr').get_result()
    return french_translation.get("translations")[0].get("translation")

def french_to_english(text1):
    """This function translatefrench to english"""
    english_translation = language_translator.translate(
    text=text1,
    model_id='fr-en').get_result()
    return english_translation.get("translations")[0].get("translation")
