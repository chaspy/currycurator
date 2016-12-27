from flask import Flask, render_template
from pymongo import MongoClient
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    article = get_db()
    return render_template('index.html', article=article)

def get_db():
    db = MongoClient().ArticleDB
    co = db.article_collection
    list = []
    for x in co.find():
        site = (x["title"],x["href"])
        list.append(site)
    return list


if __name__ == '__main__':
    app.run(host='0.0.0.0') 
