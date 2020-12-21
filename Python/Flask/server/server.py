from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    print('we are at ...')
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# CSV actually stands for comma separated values


def write_to_csv(data):
    with open('./databese.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writter = csv.writer(
            database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([email, subject, message])


def write_to_file(data):
    with open('databese.text',newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, \t{subject}, \t{message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # print(boody)
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        # write_to_file(data)
        print(data)
    return redirect('thankyou.html')

# @app.route('/index.html')
# def index():
#     return render_template('index.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')
