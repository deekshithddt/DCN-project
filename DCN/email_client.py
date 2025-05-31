from flask import Flask, render_template, request
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sender = request.form['from_email']
        receiver = request.form['to_email']
        subject = request.form['subject']
        message_body = request.form['message']

        # Construct MIME email
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = subject
        message.attach(MIMEText(message_body, 'plain'))

        # Send the email using TCP client
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('localhost', 12345))
            client_socket.send(message.as_string().encode('utf-8'))

            # Receive acknowledgment
            ack = client_socket.recv(1024).decode('utf-8')
            client_socket.close()
            return render_template('compose_email.html', success_message=f"Email sent successfully! Server acknowledgment: {ack}")
        except Exception as e:
            return render_template('compose_email.html', error_message=f"Failed to send email: {e}")

    return render_template('compose_email.html')

if __name__ == '__main__':
    app.run(debug=True)
    