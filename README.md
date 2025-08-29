# Animal Selection & File Upload Application

A Flask-based web application that allows users to select a single animal (cat, dog, or elephant) and upload files to get file information.

## Features

- **Single Animal Selection**: Choose one animal from cat, dog, or elephant using radio buttons
- **Animal Image Display**: Shows the selected animal's image
- **File Upload**: Upload any file type with drag-and-drop support
- **File Information**: Get file name, size, and type from the backend
- **Modern UI**: Beautiful, responsive design with smooth animations

## Project Structure

```
session_2/
├── app.py                 # Flask backend application
├── index.html            # Frontend HTML/CSS/JS
├── requirements.txt      # Python dependencies
├── download_images.py    # Script to download animal images
├── static/
│   └── images/          # Animal images (cat.jpg, dog.jpg, elephant.jpg)
└── uploads/             # Uploaded files (optional)
```

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Download Animal Images

```bash
python download_images.py
```

This will download sample images for cat, dog, and elephant from Unsplash.

### 3. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Usage

1. **Animal Selection**: Click on any animal (cat, dog, or elephant) to select it. Only one animal can be selected at a time.
2. **Image Display**: When an animal is selected, its image will appear below the selection.
3. **File Upload**: 
   - Click on the upload area to browse for files
   - Or drag and drop files onto the upload area
   - The file information (name, size, type) will be displayed after upload

## API Endpoints

- `GET /` - Serves the main HTML page
- `POST /upload` - Handles file upload and returns file information
- `GET /static/images/<filename>` - Serves animal images

## Technical Details

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **File Upload**: Supports any file type up to 16MB
- **Responsive Design**: Works on desktop and mobile devices
- **Error Handling**: Graceful error handling for file uploads and image loading

## Customization

- **Animal Images**: Replace images in `static/images/` folder
- **File Size Limit**: Modify `MAX_CONTENT_LENGTH` in `app.py`
- **Styling**: Edit CSS in `index.html` to change appearance
- **File Storage**: Uncomment the file save line in `app.py` if you want to store uploaded files

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## License

This project is open source and available under the MIT License.
