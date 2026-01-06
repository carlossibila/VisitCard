import qrcode
from PIL import Image
import os
import sys


if len(sys.argv) >= 2:
    url = sys.argv[1]
    print(f"Generating QR codes for: {url}\n")
else:
    url = input("Enter the URL to generate QR code: ")
    print(f"Creating QR codes for: {url}\n")

# Create Share directory one level up from script location if it doesn't exist
share_dir = os.path.join(os.path.dirname(__file__), '..', 'Share')
os.makedirs(share_dir, exist_ok=True)

# Define size configurations
sizes = [
    (300, 'Small'),
    (600, 'Medium'),
    (1200, 'Large')
]

# Define color configurations
colors = [
    ('Black', (0, 0, 0)),
    ('White', (255, 255, 255))
]


total_files = 0

# Generate QR codes for each size
for size, label in sizes:
    print(f"Generating {label} ({size}x{size}) QR codes...")

    # Create QR code instance 
    qr = qrcode.QRCode(
        version=None,  
        error_correction=qrcode.constants.ERROR_CORRECT_H,  
        box_size=10,  
        border=4,  
    )

    
    qr.add_data(url)
    qr.make(fit=True)

    # Generate both black and white versions
    for color_name, fill_color in colors:
        
        if color_name == 'Black':
            back_color = (255, 255, 255)  # White background
            transparent_color = (255, 255, 255)  # white transparent
        else:  
            back_color = (0, 0, 0)  # Black background
            transparent_color = (0, 0, 0)  # black transparent

        
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Convert to RGBA for transparency support
        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        
        datas = img.getdata()
        new_data = []
        for item in datas:
            
            if item[:3] == transparent_color:
                new_data.append((0, 0, 0, 0))  
            else:
                new_data.append(item)

        img.putdata(new_data)

        
        img = img.resize((size, size), Image.Resampling.LANCZOS)

        # Save naming pattern: QRC_{size}x{size}_{color}.png
        filename = f"QRC_{size}x{size}_{color_name}.png"
        filepath = os.path.join(share_dir, filename)
        img.save(filepath, 'PNG')

        print(f"[OK] {filename} created")
        total_files += 1

    print()  

print(f"[SUCCESS] {total_files} QR code files created successfully!")
print(f"Check the '{os.path.relpath(share_dir)}' folder for all PNG files")
