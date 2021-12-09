from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "GOTEAM"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_give_info():
    session['form_data'] = request.form
    return render_template('results.html', your_name = request.form['your_name'],
    dojo_location = request.form['dojo_location'],
    fav_language = request.form['favorite_language'], optional_comm=request.form['optional_comment']
    )

@app.route('/redirect_demo')
def redirect_demo():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)