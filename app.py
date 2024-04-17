from flask import Flask, render_template, request, send_file
from img2table.document import Image, PDF
from img2table.ocr import TesseractOCR
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add a secret key for flash messages

def process(request):
    try:
        file = request.files['file']
        if file:
            filename = file.filename
            # Define the path to the uploads folder
            upload_folder = 'uploads/'
            # Ensure the uploads folder exists
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            # Save the file in the uploads folder
            file.save(os.path.join(upload_folder, filename))
            file_type = os.path.splitext(file.filename)[1].lower()
            if file_type == '.pdf':
                return process_pdf(os.path.join(upload_folder, filename))
            elif file_type in ['.jpg', '.jpeg', '.png', '.gif']:
                return process_image(os.path.join(upload_folder, filename))
            else:
                message = "Error: Unsupported file type."
                return {'message': message, 'success': False}
        else:
            message = "Error: No file provided."
            return {'message': message, 'success': False}
    except Exception as e:
        message = f"Error: {str(e)}"
        return {'message': message, 'success': False}

def process_pdf(filename):
    try:
        pdf = PDF(filename)
        ocr = TesseractOCR(lang="eng")
        pdf.to_xlsx("output.xlsx", ocr=ocr)
        message = "Success: PDF processed successfully."
        return {'message': message, 'success': True}
    except Exception as e:
        message = f"Error processing PDF: {str(e)}"
        return {'message': message, 'success': False}

def process_image(filename):
    try:
        image = Image(filename)
        ocr = TesseractOCR(lang="eng")
        image.to_xlsx("output.xlsx", ocr=ocr)
        message = "Success: Image processed successfully."
        return {'message': message, 'success': True}
    except Exception as e:
        message = f"Error processing image: {str(e)}"
        return {'message': message, 'success': False}

@app.route('/image_pdf_to_table', methods=['POST', 'GET'])
def image_pdf_to_table():
    if request.method == 'POST':
        result = process(request)
        return render_template('index.html', message=result['message'], success=result['success'])
    else:
        return render_template('index.html')

@app.route('/download_file')
def download_file():
    return send_file("output.xlsx", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
