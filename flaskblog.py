from flask import Flask, render_template, url_for, request, redirect
import datetime
import csv

app = Flask(__name__)

x = datetime.datetime.now()
date = x.strftime("%Y")


@app.route("/")
def index():
    return render_template('index.html', date=date, title="Home")


@app.route("/about")
def about():
    return render_template('about.html', date=date, title="About")


@app.route("/works")
def works():
    return render_template('works.html', date=date, title="Works")


@app.route("/work")
def work():
    return render_template('work.html', date=date, title="Work")


@app.route("/contact")
def contact():
    return render_template('contact.html', date=date, title="Contacts")


@app.route("/Thankyou")
def Thankyou():
    return render_template('Thankyou.html', date=date, title="ThankYou")


@app.route("/resend")
def resend():
    return render_template('resend.html', date=date, title="Re-send")


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#     file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["Email: ", email, "\nSubject : ",
                            subject, "\nMessage : ", message])


@ app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect(url_for('Thankyou'))
        except:
            return "Something Went wrong"
    else:
        return redirect(url_for('resend'))


if __name__ == "__main__":
    app.run(debug=True)
