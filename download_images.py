import requests
import os

def download_image(url, filename):
    """Download an image from URL and save it to static/images folder"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        filepath = os.path.join('static', 'images', filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

def main():
    # Create static/images directory if it doesn't exist
    os.makedirs('static/images', exist_ok=True)
    
    # Sample animal images (using placeholder images)
    images = {
        'cat.jpg': 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=400&h=300&fit=crop',
        'dog.jpg': 'https://images.unsplash.com/photo-1517423440428-a5a00ad493e8?w=400&h=300&fit=crop',
        'elephant.jpg': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=300&fit=crop'
    }
    
    print("Downloading animal images...")
    for filename, url in images.items():
        download_image(url, filename)
    
    print("Image download complete!")

if __name__ == '__main__':
    main()
