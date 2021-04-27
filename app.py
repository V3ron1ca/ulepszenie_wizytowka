from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/mypage')
def index():
    return render_template('index.html')

@app.route('/mypage/contact', methods=["GET", "POST"])
def kontakt():
    if request.method == "POST":
        text = request.form.get("text", None)
        print(text)
    return render_template('kontakt.html')

if __name__ == '__main__':
    TEMPLATES_AUTO_RELOAD = True
    app.run(debug=True)
