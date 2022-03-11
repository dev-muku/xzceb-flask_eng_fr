"""
Module for Language Translation
"""
import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-03-09',
    authenticator=authenticator
)
"""
Setting Watson Language Translator domain
"""
language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Function for English to French Translation
    """
    if english_text is None :
        french_text = None
        return french_text

    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Function for French to English Translation
    """
    if french_text is None :
        english_text = None
        return english_text
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
