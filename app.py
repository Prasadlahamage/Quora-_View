from Proxy import proxies
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return render_templates('index.html')

@app.route('/proxy', methods=['GET','POST'])
def proxy():
    url = request.form['url']
    ip = request.form['ip']
    return proxies(url, int(ip)+1)
    
if __name__ == '__main__':
    app.run(Debug="True")
