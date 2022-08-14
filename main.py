from os import name
from flask import Flask, request, jsonify
import markdown.extensions.fenced_code
import json
import random
import googletrans
# import tools.mongo_tools as mongo
import tools.sql_tools as sql
import pandas as pd
# from nltk.corpus import stopwords
# nltk.download('stopwords')
# stop_words = stopwords.words('english')
# from collections import Counter, OrderedDict




app = Flask(__name__)

# GET: render markdown
@app.route("/")  
def index():
    readme_file = open("README.md", "r")
    md_template = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template

#we created a special feature that generates a number between 0 and 1000 to test the program
@app.route("/random-number") 
def random_number():
    return str(random.choice(range(0,1000)))

# Get everything: SQL
@app.route("/speeches")
def get_everything ():
    return jsonify(sql.get_everything())

# Query the different Presidents of the United States 
# It shows all the name of US presidents.
@app.route("/presidents") 
def list_all_presidents():
    return jsonify(sql.list_all_presidents())

# Query the different Parties of the United States 
# It shows all the name of US presidents.
@app.route("/parties") 
def list_all_parties():
    return jsonify(sql.list_all_parties())


@app.route("/sentiment/president/<president>")
def get_sentiment_president(president):
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    import statistics as st
    import string
    from textblob import TextBlob
    alphabet = string.ascii_letters+" '"+string.digits

    sese = jsonify(sql.get_everything_from_president(president)) 
    all = sese.get_json()
    sentimentdf = pd.DataFrame.from_dict(all)
    
    def replacing(s):
        for c in s:
            if c.lower() not in alphabet:
                s=s.replace(c,' ')
        return s

    sentimentdf["Transcript"] = sentimentdf["Transcript"].apply(lambda x: replacing(x) )
    temp = sentimentdf.groupby('President', as_index=False)['Transcript'].apply(lambda x: ' '.join(x))
    blob = TextBlob(str(temp["Transcript"].values[0]))
    feelings = round(blob.sentiment.polarity,2)

    if feelings == 0:
        return f"The polarity score is {feelings}, meaning {president}'s Speeches were NEUTRAL"
    elif feelings > 0:
        return f"The polarity score is {feelings}, meaning {president}'s Speeches were SOMEWHAT POSITIVE"
    elif feelings > 0.25:
        return f"The polarity score is {feelings}, meaning {president}'s Speeches were POSITIVE"
    elif feelings > 0.50:
        return f"The polarity score is {feelings}, meaning {president}'s Speeches were VERY POSITIVE"
    elif feelings < 0:
        return f"The polarity score is {feelings}, meaning {president}'s Speeches were SOMEWHAT NEGATIVE"
    elif feelings < -0.25:
        return f"The polarity score is {feelings}, meaning {president}'s Speeches were NEGATIVE"
    elif feelings < -0.50:
        return f"The polarity score is {feelings}, meaning {president}'s Speeches were VERY NEGATIVE"
    else:
        return "No polarity detected for {president}'s Speeches"


@app.route("/sentiment/party/<party>")
def get_sentiment_party(party):
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    import statistics as st
    import string
    from textblob import TextBlob
    alphabet = string.ascii_letters+" '"+string.digits

    sese = jsonify(sql.get_everything_from_party(party)) 
    all = sese.get_json()
    sentimentdf = pd.DataFrame.from_dict(all)
    
    def replacing(s):
        for c in s:
            if c.lower() not in alphabet:
                s=s.replace(c,' ')
        return s

    sentimentdf["Transcript"] = sentimentdf["Transcript"].apply(lambda x: replacing(x) )
    temp = sentimentdf.groupby('Party', as_index=False)['Transcript'].apply(lambda x: ' '.join(x))
    blob = TextBlob(str(temp["Transcript"].values[0]))
    feelings = round(blob.sentiment.polarity,2)

    if feelings == 0:
        return f"The polarity score is {feelings}, meaning {party}'s Speeches were NEUTRAL"
    elif feelings > 0:
        return f"The polarity score is {feelings}, meaning {party}'s Speeches were SOMEWHAT POSITIVE"
    elif feelings > 0.25:
        return f"The polarity score is {feelings}, meaning {party}'s Speeches were POSITIVE"
    elif feelings > 0.50:
        return f"The polarity score is {feelings}, meaning {party}'s Speeches were VERY POSITIVE"
    elif feelings < 0:
        return f"The polarity score is {feelings}, meaning {party}'s Speeches were SOMEWHAT NEGATIVE"
    elif feelings < -0.25:
        return f"The polarity score is {feelings}, meaning {party}'s Speeches were NEGATIVE"
    elif feelings < -0.50:
        return f"The polarity score is {feelings}, meaning {party}'s Speeches were VERY NEGATIVE"
    else:
        return "No polarity detected for {party}'s Speeches"

# Get everything FROM someone AND use a condition: SQL, argument & params
@app.route("/one/<name>")
def one_random_language (name):
    frases = mongo.all_sentences(name)
    one = random.choice(frases)

    language = request.args["language"]
    trans = googletrans.Translator()
    result = trans.translate(one["dialogue"], dest=language)

    one["dialogue"] = result.text
    
    return one


## POST
@app.route("/newline", methods=["POST"])
def insert_new_speech():
    Year = request.form.get("Year")
    Date = request.form.get("Date")
    President = request.form.get("President")
    Party = request.form.get("Party")
    Title = request.form.get("Title")
    Summary = request.form.get("Summary")
    Transcript = request.form.get("Transcript")
    URL = request.form.get("URL")

    return sql.insert_new_speech (Year, Date, President, Party, Title, Summary, Transcript, URL)

app.run(port = 5001, debug=True)