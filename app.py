from flask import Flask, render_template, jsonify, json, request
import pandas as pd

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')


filename = 'data.csv'
df = pd.read_csv(filename)
print(df.head())

content = []
for i in range(len(df)):
    content.append([df.loc[df.index[i], 'name'], df.loc[df.index[i],
                                                        'detail'], df.loc[df.index[i], 'description'], df.loc[df.index[i], 'src']])


response = {
    'content': content
}


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html', name='Kitta', response=response)


if __name__ == '__main__':
    app.run(debug=True)
