#from machinetranslation import translator
from machinetranslation import english_to_french, french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/englishToFrench')
def english_to_french_endpoint():
    english_text = request.args.get('text')
    french_text = english_to_french(english_text)
    return french_text

@app.route('/frenchToEnglish')
def french_to_english_endpoint():
    french_text = request.args.get('text')
    english_text = french_to_english(french_text)
    return english_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
