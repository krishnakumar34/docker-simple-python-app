import logging

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello Worldkk'

@app.route('/test')
def get_high_res(url):
 from pytube import YouTube
 yt = YouTube(url)

 return yt.streams.get_highest_resolution().url


url = 'https://www.youtube.com/watch?v=yWtWt-e_p24'

m3u = get_high_res(url)
print(m3u)
return m3u


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
