from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse_emotion', methods=['POST'])
def analyse_emotion():
    texte = request.form['texte']
    blob = TextBlob(texte, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    sentiment = blob.sentiment
    polarity = sentiment[0]
    subjectivity = sentiment[1]
    
    if polarity > 0.5 and subjectivity > 0.5:
        emotion = "amour"
    elif polarity < -0.5 and subjectivity > 0.5:
        emotion = "haine"
    elif polarity < 0 and subjectivity > 0.5:
        emotion = "colère"
    else:
        emotion = "neutre"

    return jsonify({'emotion': emotion})


if __name__ == '__main__':
    app.run(debug=True)
