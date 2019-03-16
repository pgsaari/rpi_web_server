from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/cool-page')
def coolpage():
   return render_template('cool-page.html')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
