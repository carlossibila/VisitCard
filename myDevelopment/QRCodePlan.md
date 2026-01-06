# QR Code Generator - Standalone Python Utility

## Overview
Create a Python script to generate QR codes from URLs. The QR code can be used on printed materials to direct people to the digital business card. This is a portable, reusable utility that can be used across different projects.

## Implementation Plan

### 1. Project Restructuring

**Create new folder structure**:
```
d:\ParalelProjects\VisitCard\
├── Python/                          # New folder for Python utilities
│   ├── create_placeholders.py      # Move existing script here
│   └── generate_qrcode.py          # New QR code generator
└── Share/                           # New folder for generated QR codes (created by script)
    └── QRC_300x300_Black.png       # Example output files
    └── QRC_300x300_White.png
```

**Actions**:
1. Create `d:\ParalelProjects\VisitCard\Python\` folder
2. Move `d:\ParalelProjects\VisitCard\create_placeholders.py` to `Python/` folder
3. Create `d:\ParalelProjects\VisitCard\Python\generate_qrcode.py`
4. Script will auto-create `d:\ParalelProjects\VisitCard\Share\` folder when run

### 2. QR Code Generator Script
**File**: `d:\ParalelProjects\VisitCard\Python\generate_qrcode.py`

The script will:
- Accept a URL as input (command-line argument or interactive prompt)
- Generate QR codes in both BLACK and WHITE versions
- Generate QR codes in multiple sizes (each with black and white versions)
- Use transparent backgrounds (PNG format)
- Save QR codes to `../Share/` folder (one level up from script location)
- Follow portable design - works in any project

### 3. Required Dependencies
Install the following Python libraries:
- `qrcode[pil]` - Main QR code generation library with image support
- `Pillow` (PIL) - Already used in the project for image manipulation

Installation command: `pip install qrcode[pil]`

### 4. URL Input Methods - Code Examples

The script supports two ways to provide the URL:

#### Method 1: Interactive Prompt
```bash
python generate_qrcode.py
```
```python
# Inside the script:
if len(sys.argv) < 2:
    url = input("Enter the URL to generate QR code: ")
else:
    url = sys.argv[1]
```
**User experience**: Script prompts "Enter the URL to generate QR code: " and waits for input.

#### Method 2: Command-Line Argument
```bash
python generate_qrcode.py https://yourusername.github.io/visitcard
```
```python
# Inside the script:
import sys
if len(sys.argv) >= 2:
    url = sys.argv[1]
    print(f"Generating QR code for: {url}")
```
**User experience**: URL is passed directly, no prompt needed.

### 5. Core Features

#### QR Code Generation:
- **Black Version**: QR code with black foreground, transparent background
- **White Version**: QR code with white foreground, transparent background
- **Multiple Sizes**: Generate 3 default sizes (or customizable)
  - Small: 300x300 pixels
  - Medium: 600x600 pixels
  - Large: 1200x1200 pixels
- **Transparent Background**: PNG format with alpha channel
- **Error Correction**: HIGH level (explained below)

#### File Naming Pattern:
All files follow the format: `QRC_{width}x{height}_{color}.png`

Examples:
- `QRC_300x300_Black.png` - Small black QR code
- `QRC_300x300_White.png` - Small white QR code
- `QRC_600x600_Black.png` - Medium black QR code
- `QRC_600x600_White.png` - Medium white QR code
- `QRC_1200x1200_Black.png` - Large black QR code
- `QRC_1200x1200_White.png` - Large white QR code

Total files generated per run: **6 files** (3 sizes × 2 colors)

### 6. Error Correction Explained

QR codes have built-in error correction that allows them to be read even when partially damaged or obscured.

**Error Correction Levels**:
- **L (Low)**: ~7% of code can be damaged and still readable
- **M (Medium)**: ~15% of code can be damaged and still readable
- **Q (Quartile)**: ~25% of code can be damaged and still readable
- **H (High)**: ~30% of code can be damaged and still readable

**Why use HIGH error correction**:
- QR codes on printed materials can get scratched, smudged, or wrinkled
- Allows the code to work even if partially covered by fingers while scanning
- More resilient to printing imperfections
- Critical for business cards that may be handled frequently
- Small trade-off: slightly more complex QR pattern (more "dots")

**Implementation**:
```python
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H  # HIGH level
)
```

### 7. Script Structure

```
1. Import libraries (qrcode, PIL, os, sys)
2. Get URL input (command-line arg or interactive prompt)
3. Create Share folder (../Share/) if it doesn't exist
4. Define size configurations [(300, 'Small'), (600, 'Medium'), (1200, 'Large')]
5. Loop through sizes:
   a. Create QR code instance with HIGH error correction
   b. Add URL data to QR code
   c. Generate BLACK version:
      - Create image with black fill, transparent background
      - Save as QRC_{size}x{size}_Black.png
   d. Generate WHITE version:
      - Create image with white fill, transparent background
      - Save as QRC_{size}x{size}_White.png
   e. Print success message for each file
6. Print final summary with total files created
```

### 8. Usage Examples

**Example 1: Interactive mode**
```bash
cd d:\ParalelProjects\VisitCard\Python
python generate_qrcode.py
```
Output:
```
Enter the URL to generate QR code: https://example.com
Creating QR codes for: https://example.com

Generating Small (300x300) QR codes...
[OK] QRC_300x300_Black.png created
[OK] QRC_300x300_White.png created

Generating Medium (600x600) QR codes...
[OK] QRC_600x600_Black.png created
[OK] QRC_600x600_White.png created

Generating Large (1200x1200) QR codes...
[OK] QRC_1200x1200_Black.png created
[OK] QRC_1200x1200_White.png created

[SUCCESS] 6 QR code files created successfully!
Check the '../Share' folder for all PNG files
```

**Example 2: Command-line argument**
```bash
cd d:\ParalelProjects\VisitCard\Python
python generate_qrcode.py https://yourusername.github.io/visitcard
```
Output:
```
Generating QR codes for: https://yourusername.github.io/visitcard

[Generates all 6 files as shown above]
```

### 9. QR Code Configuration

- **Error Correction**: HIGH (30% of code can be restored)
- **Box Size**: Calculated to achieve target pixel dimensions
- **Border**: 4 boxes (QR code standard minimum)
- **Fill Colors**:
  - Black version: `#000000` (RGB: 0, 0, 0)
  - White version: `#FFFFFF` (RGB: 255, 255, 255)
- **Background**: Transparent (RGBA with alpha=0)
- **Output Format**: PNG with alpha channel
- **Target Sizes**: 300x300, 600x600, 1200x1200 pixels

## Critical Files

**Folders to create:**
- `d:\ParalelProjects\VisitCard\Python\` - New folder for Python utilities
- `d:\ParalelProjects\VisitCard\Share\` - Auto-created by script for QR code output

**Files to move:**
- Move `d:\ParalelProjects\VisitCard\create_placeholders.py` → `d:\ParalelProjects\VisitCard\Python\create_placeholders.py`

**New files to create:**
- `d:\ParalelProjects\VisitCard\Python\generate_qrcode.py` - Main QR code generator script
- `d:\ParalelProjects\VisitCard\myDevelopment\QRCodePlan.md` - This plan document (copy from temp location)

**Files to reference for code style:**
- `d:\ParalelProjects\VisitCard\create_placeholders.py` - Style reference for consistency

**Output files (generated by script):**
- `d:\ParalelProjects\VisitCard\Share\QRC_300x300_Black.png`
- `d:\ParalelProjects\VisitCard\Share\QRC_300x300_White.png`
- `d:\ParalelProjects\VisitCard\Share\QRC_600x600_Black.png`
- `d:\ParalelProjects\VisitCard\Share\QRC_600x600_White.png`
- `d:\ParalelProjects\VisitCard\Share\QRC_1200x1200_Black.png`
- `d:\ParalelProjects\VisitCard\Share\QRC_1200x1200_White.png`

## Implementation Steps

**Step 1**: Restructure project
- Create `Python/` folder
- Move `create_placeholders.py` to `Python/` folder
- Update any documentation referencing the old location

**Step 2**: Create QR code generator
- Accept URL input (both methods: interactive and command-line)
- Generate 6 QR code files (3 sizes × 2 colors)
- Transparent backgrounds for all versions
- Save to `Share/` folder (auto-created)

**Step 3**: Test the script
- Test interactive mode
- Test command-line argument mode
- Verify all 6 files are created correctly
- Verify transparent backgrounds work
- Scan QR codes to verify they work

**Step 4**: Documentation
- Consider adding usage notes to README.md or creating a separate doc
- Document the new folder structure

## Key Design Principles

✓ **Portability**: Script works in any project, not tied to VisitCard specifics
✓ **Simplicity**: No logo embedding, no custom colors - just black and white
✓ **Transparency**: All QR codes have transparent backgrounds for flexible use
✓ **Naming Convention**: Clear, consistent file naming with size and color
✓ **Reusability**: Same script can generate QR codes for any URL
✓ **Multiple Options**: 3 sizes and 2 colors give users flexibility
✓ **Error Resilience**: HIGH error correction for durability
