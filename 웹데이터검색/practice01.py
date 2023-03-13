from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
        data = pd.read_excel('C:\업무자동화\웹데이터검색\DB.xlsx')
        data = data[data['원문'].str.contains(keyword, na=False)]
        return render_template('index.html', tables=[data.to_html(classes='data')], titles=data.columns.values)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=80)
