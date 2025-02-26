# QR Code Generator  

A lightweight and easy-to-use Python tool for generating QR codes from text or URLs. Customize colors, sizes, and save your QR codes as images in seconds!  

## Features  
✅ Generate high-quality QR codes  
✅ Save as PNG/JPG with customizable resolution  
✅ Choose custom colors and sizes  
✅ Works with text, URLs, and any other data  

## Installation  
First, install the required dependency:  
```bash
pip install qrcode[pil]
```
## Usage

1️⃣ Run the script to generate a QR code:
```
python generate_qr.py
```

2️⃣ Or use it inside your Python code:
```
import qrcode  

# Create a QR code from a URL
 qr = qrcode.make("https://opensource.google/")  

# Save the QR code as an image  
qr.save("open_source_qr.png")  

```


