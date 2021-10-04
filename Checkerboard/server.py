from flask import Flask, render_template

app = Flask(__name__)

# 8 by 8
@app.route('/')
def _8by8_():
    return render_template("index.html", row=8, column=8, color1="aqua", color2="red")

# 8 by 4
@app.route('/<int:x>')
def setRow(x):
    return render_template("index.html", row=x, column=8, color1="aqua", color2="red")

# x * y
@app.route('/<int:x>/<int:y>')
def setRowNCol(x,y):
    return render_template("index.html", row=x, column=y, color1="aqua", color2="red")

# x * y + color 1
@app.route('/<int:x>/<int:y>/<string:one>')
def setRowColColor(x,y,one):
    return render_template("index.html", row=x, column=y, color1=one, color2="red")

# x * y + color 1/color 2
@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def setRCColor(x,y,one,two):
    return render_template("index.html", row=x, column=y, color1=one, color2=two)


if __name__=="__main__":
    app.run(debug=True)
