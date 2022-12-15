from flask import Flask, render_template, url_for, request, redirect, send_from_directory
from pytube import YouTube

app = Flask('app')


@app.route('/')
def hello_world():
  return render_template("index.html")


@app.route('/getvid', methods=["POST"])
def getvid():
  yt = YouTube(request.form.get("link"))
  vid = yt.streams.filter(file_extension="mp4").first()
  vid.download('static/', 'vid.mp4')
  return send_from_directory(directory="static/",
                             path="vid.mp4",
                             as_attachment=True)


app.run(host='0.0.0.0', port=80)
