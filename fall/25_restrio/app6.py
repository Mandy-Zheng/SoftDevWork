#Amanda Zheng
#SoftDev1 pd1
#K25: Getting More Rest
#2019-11-13
from flask import Flask , render_template
import urllib, json
from json import loads
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib.request.urlopen(" http://openlibrary.org/works/OL16813032W.json")
    response = u.read()
    data = json.loads(response)
    return render_template("books.html", title=data['title'], genre=data['subjects'],
                                        setting=data['subject_times'])

if __name__ == "__main__":
    app.debug = True
    app.run()
