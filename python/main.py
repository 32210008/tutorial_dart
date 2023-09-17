from Flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Selamat Datang di Hotel Kami</h1>"

if __name__ == '__main__':
    app.run(debug=True)