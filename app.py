from flask import Flask, request, render_template, url_for, redirect
from clean_text import preprocess_text
import joblib

tfidf = joblib.load('tfidf_vectorizer.joblib')
svm = joblib.load('svm_sentiment_model.joblib')
lblenc = joblib.load('label_encoder.joblib')

initial_text = '''
After a bridge and a train engine, Bihar's list of bizarre thefts continued with an entire pond being "stolen". The pond vanished and had a hut built on it, leaving the locals baffled in Darbhanga district.'
'''

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global initial_text
    if request.method == 'POST':
        text = request.form['news']
        initial_text = text
        sentiment_result = applyModel(preprocess_text(text))
        return render_template('result.html', text=text, sentiment=sentiment_result)

    return render_template('index.html', text=initial_text)

def applyModel(text):
    text_tfidf = tfidf.transform([text])
    prediction = svm.predict(text_tfidf)
    label = lblenc.inverse_transform(prediction)

    return label[0]
    
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')