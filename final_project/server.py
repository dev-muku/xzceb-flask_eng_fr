'''
Defining app routes and setting server port.
'''
from flask import Flask, render_template, request
from machinetranslation import translator
#import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_2_french():
    '''
    Translating text from English to French.
    '''
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    translation_to_french = translator.english_to_french(text_to_translate)
    return translation_to_french

@app.route("/frenchToEnglish")
def french_2_english():
    '''
    Translating text from French to English.
    '''
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    translation_to_english = translator.french_to_english(text_to_translate)
    return translation_to_english

@app.route("/")
def render_index_page():
    '''
    Rendering index page.
    '''
    return render_template("templates/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
