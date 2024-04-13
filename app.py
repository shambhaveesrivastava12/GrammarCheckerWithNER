from flask import Flask, request, render_template
from Model import SpellCheckerModule
import spacy
from spacy import displacy

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()
nlp = spacy.load('en_core_web_sm')

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell', methods=['POST', 'GET'])
def spell():
    if request.method == 'POST':
        text = request.form['text']
        corrected_text = spell_checker_module.correct_spell(text)
        corrected_grammar, _ = spell_checker_module.correct_grammar(text)
        return render_template('index.html', corrected_text=corrected_text, corrected_grammar=corrected_grammar)

@app.route('/grammar', methods=['POST', 'GET'])
def grammar():
    if request.method == 'POST':
        file = request.files['file']
        readable_file = file.read().decode('utf-8', errors='ignore')
        corrected_file_text = spell_checker_module.correct_spell(readable_file)
        corrected_file_grammar, _ = spell_checker_module.correct_grammar(readable_file)
        return render_template('index.html', corrected_file_text=corrected_file_text, corrected_file_grammar=corrected_file_grammar)

@app.route('/ner', methods=['POST'])
def ner():
    if request.method == 'POST':
        corrected_text = request.form['corrected_text']
        docs = nlp(corrected_text)
        html = displacy.render(docs, style='ent', jupyter=False)
        return render_template('index.html', html=html, corrected_text=corrected_text)


# python main
if __name__ == "__main__":
    app.run(debug=True)