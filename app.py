from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def format_file_size(bytes):
    """Format file size in human readable format"""
    if bytes == 0:
        return "0 Bytes"
    
    k = 1024
    sizes = ['Bytes', 'KB', 'MB', 'GB']
    i = int(__import__('math').floor(__import__('math').log(bytes) / __import__('math').log(k)))
    
    return f"{round(bytes / (k ** i), 2)} {sizes[i]}"

@app.route('/')
def index():
    """Serve the main HTML page"""
    return send_from_directory('.', 'index.html')

@app.route('/static/images/<filename>')
def serve_image(filename):
    """Serve animal images from static/images folder"""
    return send_from_directory('static/images', filename)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and return file information"""
    try:
        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        # Check if file was selected
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Get file information
        filename = secure_filename(file.filename)
        file_size = len(file.read())
        file.seek(0)  # Reset file pointer to beginning
        
        # Get file type
        file_type = file.content_type or 'Unknown type'
        
        # Save file (optional - you can remove this if you don't want to save files)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Return file information
        return jsonify({
            'name': filename,
            'size': format_file_size(file_size),
            'type': file_type
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(413)
def too_large(e):
    """Handle file too large error"""
    return jsonify({'error': 'File too large. Maximum size is 16MB.'}), 413

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
