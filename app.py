from flask import Flask, render_template,request
import tools

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    result = None
    if request.method == 'POST' and request.form['plaintext'] != "":
        plaintext = request.form['plaintext']
        keyword = request.form['keyword']
        if request.form['action'] == 'encrypt':
            result = tools.encrypt(plaintext,keyword)
        else:
            result = tools.decrypt(plaintext,keyword)
    return render_template('index.html',result=result)

if __name__ == "__main__":
    app.run()