from flask import Flask, render_template, request, redirect, url_for
import PyPDF2
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return redirect(request.url)
    pdf_file = request.files['pdf']
    
    if pdf_file.filename == '':
        return redirect(request.url)
    
    if pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ''
        for page_num in range(pdf_reader.getNumPages()):
            text += pdf_reader.getPage(page_num).extractText()
        
        # Store the PDF text for future chatbot interactions
        with open('uploaded_pdf.txt', 'w') as file:
            file.write(text)
        
        return redirect(url_for('chat'))
    else:
        return redirect(request.url)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return render_template('chat.html', answer=None)
    elif request.method == 'POST':
        user_question = request.form['question']
        # Simulate a chatbot response (replace this with a real chatbot)
        bot_answer = "This is a placeholder response."

        return render_template('chat.html', answer=bot_answer)

if __name__ == '__main__':
    app.run(debug=True)