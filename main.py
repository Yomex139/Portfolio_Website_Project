from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import datetime as dt
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

#mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MY_MAIL')
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWD')

mail = Mail(app)


# Home page
@app.route('/')
def home():
    return render_template("index.html", dt=dt)


# About page
@app.route('/about')
def about():
    return render_template("about.html", dt=dt)


# Projects page
@app.route('/project')
def projects():
    return render_template("project.html", dt=dt)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        # Here, you can save the message, send an email, etc.
        msg = Message(subject=f'New Contact Form Submission: {subject}',
                      sender=email,
                      recipients=[os.environ.get('MY_MAIL')],
                      )
        msg.body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
        # send the mail
        try:
            mail.send(msg)
            flash("Thank you! Your message has been sent successfully.")
        except Exception as e:
            flash("An error occurred while sending your message. Please try again later.")
            print(f"Error: {e}")
        return redirect(url_for('contact'))  # Redirect to avoid form resubmission issues

    # For GET request, just render the contact page with the current date
    return render_template("contact.html", dt=dt)


if __name__ == "__main__":
    app.run(debug=True)