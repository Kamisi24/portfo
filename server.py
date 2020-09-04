from flask import Flask, render_template, url_for, request, redirect
import csv
#$env:FLASK_APP = "server.py"
# to run: python -m flask run
# webpage: http://127.0.0.1:5000/

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/components.html')
def my_components():
    return render_template('components.html')


@app.route('/<string:page_name>')
def components(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            filename = 'database.csv'

            with open(filename, mode = 'a', newline = '') as file_object:
                email = data["email"]
                subject = data["subject"]
                message = data["message"]
                csv_writer = csv.writer(file_object, delimiter= ',', quotechar='"', quoting= csv.QUOTE_MINIMAL) #each item in the row will be seperated by a ,
                csv_writer.writerow([email, subject, message])
            return redirect('/thanks.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'



if __name__ == '__main__':
    app.run(debug=True)