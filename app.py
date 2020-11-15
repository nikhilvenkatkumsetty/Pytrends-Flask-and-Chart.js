from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
import csv

app = Flask(__name__)

@app.route('/')
def barchart():
    with open('trends.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    # print(data)
    labels=[]
    values=[]
    for i in range(1,len(data)):
        labels.append(data[i][0])
        values.append(data[i][1])
    return render_template('chart.html', values=values, labels=labels)

if __name__ == '__main__':    
    app.run()
