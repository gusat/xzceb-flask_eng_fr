"""Module for translating text between English and French using IBM Watson Language Translator."""
import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()
APIKEY = os.environ['apikey']
URL = os.environ['url']

def create_translator_instance():
    """Create an instance of the IBM Watson Language Translator."""
    authenticator = IAMAuthenticator(APIKEY)
    language_translator = LanguageTranslatorV3(
        version='2021-09-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(URL)
    return language_translator

def english_to_french(english_text):
    """Translate text from English to French."""
    language_translator = create_translator_instance()
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Translate text from French to English."""
    language_translator = create_translator_instance()
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
