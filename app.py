from flask import Flask, render_template, request, jsonify
from werkzeug.utils import redirect

app = Flask(__name__)

url_mapping = {}
counter = 1  # To simulate a unique identifier

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    global counter
    long_url = request.form['long_url']
    short_url = id_to_short_url(counter)
    url_mapping[short_url] = long_url
    counter += 1
    return jsonify({'short_url': short_url})

@app.route('/<short_url>')
def redirect_to_original(short_url):
    long_url = url_mapping.get(short_url, '/')
    return redirect(long_url)

def id_to_short_url(n):
    char_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    short_url = ""
    
    while n:
        short_url += char_map[n % 62]
        n //= 62
    
    return short_url[::-1]

if __name__ == '__main__':
    app.run(debug=True)
