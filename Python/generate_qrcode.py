import qrcode
from PIL import Image
import os
import sys

# Get URL from command line or user input
if len(sys.argv) >= 2:
    url = sys.argv[1]
    print(f"Generating QR codes for: {url}\n")
else:
    url = input("Enter the URL to generate QR code: ")
    print(f"Creating QR codes for: {url}\n")

# Create Share directory one level up from script location if it doesn't exist
share_dir = os.path.join(os.path.dirname(__file__), '..', 'Share')
os.makedirs(share_dir, exist_ok=True)

# Define size configurations: (pixel_size, label)
sizes = [
    (300, 'Small'),
    (600, 'Medium'),
    (1200, 'Large')
]

# Define color configurations: (color_name, fill_color_rgb)
colors = [
    ('Black', (0, 0, 0)),
    ('White', (255, 255, 255))
]

# Counter for total files created
total_files = 0

# Generate QR codes for each size
for size, label in sizes:
    print(f"Generating {label} ({size}x{size}) QR codes...")

    # Create QR code instance with HIGH error correction
    qr = qrcode.QRCode(
        version=None,  # Auto-determine version based on data
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # HIGH error correction (30%)
        box_size=10,  # Initial box size (will be adjusted)
        border=4,  # Standard border size (4 boxes)
    )

    # Add URL data to QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Generate both black and white versions
    for color_name, fill_color in colors:
        # For black QR codes: black fill on white background (make white transparent)
        # For white QR codes: white fill on black background (make black transparent)
        if color_name == 'Black':
            back_color = (255, 255, 255)  # White background
            transparent_color = (255, 255, 255)  # Make white transparent
        else:  # White
            back_color = (0, 0, 0)  # Black background
            transparent_color = (0, 0, 0)  # Make black transparent

        # Create QR code image
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Convert to RGBA for transparency support
        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        # Make background transparent
        datas = img.getdata()
        new_data = []
        for item in datas:
            # Make the background color transparent, keep the QR pattern
            if item[:3] == transparent_color:
                new_data.append((0, 0, 0, 0))  # Fully transparent
            else:
                new_data.append(item)

        img.putdata(new_data)

        # Resize to exact target size
        img = img.resize((size, size), Image.Resampling.LANCZOS)

        # Save with naming pattern: QRC_{size}x{size}_{color}.png
        # This will override existing files automatically
        filename = f"QRC_{size}x{size}_{color_name}.png"
        filepath = os.path.join(share_dir, filename)
        img.save(filepath, 'PNG')

        print(f"[OK] {filename} created")
        total_files += 1

    print()  # Empty line between size groups

print(f"[SUCCESS] {total_files} QR code files created successfully!")
print(f"Check the '{os.path.relpath(share_dir)}' folder for all PNG files")
