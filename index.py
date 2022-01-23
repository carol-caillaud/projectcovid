from flask import Flask
import matplotlib.pyplot as plt; plt.rcdefaults()
import requests
import json
import mpld3
import numpy as np

app = Flask(__name__, static_url_path='', static_folder='')

def create_graph():
    ca = requests.get('https://api.covidtracking.com/v1/states/ca/current.json')
    ny = requests.get('https://api.covidtracking.com/v1/states/ny/current.json')
    ca_data = json.loads(ca.content.decode('utf-8'))
    ny_data = json.loads(ny.content.decode('utf-8'))

    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    states = ['NY', 'CA']
    y_pos = np.arange(len(states))
    print("y_pos: ", y_pos)
    covid_cases = [ca_data['positive'], ny_data['positive']]

    ax.barh(y_pos, covid_cases, align='center')
    ax.set_yticks(y_pos, labels=('NY', 'CA'))
    ax.text(3, 8, 'boxed italics text in data coords', style='italic',
            bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
    ax.set_xlabel('Cases')
    ax.set_title('Covid cases in the E.U.A')

    return fig.savefig('a.png') 


@app.route("/")
def graph():
    create_graph()
    f = open("plot.html", "r")
    return f.read() 
