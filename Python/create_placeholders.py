from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Color palette for placeholders
colors = [
    '#2c5282',  # Primary Blue (logo)
    '#4299e1',  # Light Blue
    '#2d3748',  # Dark Gray
    '#718096',  # Medium Gray
    '#a0aec0',  # Light Medium Gray
    '#cbd5e0',  # Very Light Gray
    '#3182ce',  # Blue
    '#2b6cb0',  # Dark Blue
    '#bee3f8',  # Very Light Blue
]

# Create logo placeholder (200x200)
print("Creating logo placeholder...")
logo = Image.new('RGB', (200, 200), colors[0])
draw = ImageDraw.Draw(logo)
# Add text
try:
    # Try to use a default font
    font = ImageFont.truetype("arial.ttf", 24)
except:
    font = ImageFont.load_default()
text = "LOGO"
# Get text bounding box for centering
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
position = ((200 - text_width) // 2, (200 - text_height) // 2)
draw.text(position, text, fill='white', font=font)
logo.save('images/logo.jpg', 'JPEG', quality=85)
print("[OK] logo.jpg created")

# Create property placeholders (400x300)
for i in range(1, 9):
    print(f"Creating property-{i} placeholder...")
    img = Image.new('RGB', (400, 300), colors[i])
    draw = ImageDraw.Draw(img)

    # Add text
    try:
        font = ImageFont.truetype("arial.ttf", 32)
    except:
        font = ImageFont.load_default()

    text = f"Property {i}"
    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((400 - text_width) // 2, (300 - text_height) // 2)
    draw.text(position, text, fill='white', font=font)

    img.save(f'images/property-{i}.jpg', 'JPEG', quality=85)
    print(f"[OK] property-{i}.jpg created")

print("\n[SUCCESS] All placeholder images created successfully!")
print("Check the 'images' folder for 9 placeholder JPG files")
