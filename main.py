from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
@app.route("/")

def mainFunc():
    list_t = []
    path = r"C:\Users\danhc\Desktop\test"
    allFiles = os.listdir(path)
    for file in allFiles:
        filePath = os.path.join(path,file)
        fileSize = os.stat(filePath).st_size
        infoTup = (file, fileSize)
        list_t.append(infoTup)
    return render_template('index.html', the_title='Home', list_t=list_t,path=path)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")