from flask import Flask, render_template, url_for, request
from pytube import YouTube

app = Flask('app')


@app.route('/')
def hello_world():
  return render_template("index.html")


@app.route('/getvid', methods=["POST"])
def getvid():
  return request.form.get("link")


app.run(host='0.0.0.0', port=80)
