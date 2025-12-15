# Sibila Real State - Digital Business Card

A mobile-optimized single-page website for your real estate business card, accessible via QR code. Zero-cost hosting with GitHub Pages.

## Quick Start

### 1. Generate Placeholder Images (First Time Only)

Run the Python script to create colored placeholder images:

```bash
python Python/create_placeholders.py
```

This creates 9 placeholder JPG files in the `images/` folder.

### 2. Preview Locally

Open `index.html` in your web browser:
- Double-click the file, or
- Right-click → Open with → Your browser
- Use **mobile view** in browser DevTools (F12 → Device Toggle)

## Deploying to GitHub Pages (Free Hosting!)

Since you already have GitHub experience, here's how GitHub Pages works:

### How GitHub Pages Works

**Simple Concept**: GitHub Pages takes files from your repository and serves them as a static website.

- Your repo becomes a web server
- `index.html` in the root = your homepage
- No server-side code, just HTML/CSS/JS/images
- Your URL: `https://yourusername.github.io/repository-name`

### Deployment Steps (Two Options)

---

#### **Option A: Using Git (Command Line/Desktop)**

**1. Create New Repository on GitHub**
```bash
# On GitHub.com:
# Click + → New repository
# Name: sibila-card (or any name)
# Public repository (required for free Pages)
# DON'T initialize with README
```

**2. Push Your Files**
```bash
# In your VisitCard folder:
cd "d:\ParalelProjects\VisitCard"

# Initialize git (if not already)
git init

# Add files (exclude myDevelopment for production)
git add index.html style.css images/

# Commit
git commit -m "Initial commit: Sibila Real State business card"

# Link to your GitHub repo (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/sibila-card.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**3. Enable GitHub Pages**
- Go to repo Settings → Pages (left sidebar)
- Under "Build and deployment":
  - **Source**: Deploy from a branch
  - **Branch**: `main`
  - **Folder**: `/ (root)` ← This means serve files from repository root
- Click **Save**

**What "Branch: main, Folder: root" means:**
- **Branch**: Which branch to use (`main` is your default branch)
- **Folder**: Where your website files are (root = top level of repo)
- GitHub Pages will look for `index.html` in that location

---

#### **Option B: Using GitHub Web Interface (Easier)**

**1. Create Repository**
- GitHub.com → + → New repository
- Name: `sibila-card`
- Public
- Create

**2. Upload Files**
- In the new repo, click "uploading an existing file"
- Drag these files from your computer:
  - `index.html`
  - `style.css`
  - `images/` folder (with all photos inside)
- Commit directly to `main` branch

**3. Enable Pages** (same as above)
- Settings → Pages → Source: `main` branch, `/ (root)` folder

---

### Understanding the "Branch" Setting

**You asked: "Why branch the root?"**

You're NOT "branching the root" - here's what's happening:

1. **Your repository has branches** (like `main`, `develop`, etc.)
2. **GitHub Pages asks**: "Which branch should I use to build your website?"
3. **You select**:
   - Branch: `main` (your default branch with the code)
   - Folder: `/ (root)` (where `index.html` lives - at the top level)

**Alternative folder options:**
- Some people keep website files in a `/docs` folder
- Or use a separate `gh-pages` branch
- For us: files are in the root of `main` branch (simplest)

### After Deployment

**1. Wait 2-3 minutes** for GitHub to build and deploy

**2. Check your URL**:
- Settings → Pages will show: "Your site is live at https://..."
- Copy this URL

**3. Test it**:
- Open the URL in your browser
- Should see your business card!

### File Structure in Repository

Your GitHub repo should look like:
```
sibila-card/
├── index.html          ← GitHub Pages serves this as homepage
├── style.css           ← Loaded by index.html
└── images/
    ├── logo.jpg
    └── property-*.jpg
```

**Do NOT commit:**
- `myDevelopment/` folder (development documentation only)
- `Python/` folder (utility scripts, not needed for production)
- `Share/` folder (generated QR codes, not part of website)
- `.git/` folder (automatically ignored)

### Updating Your Site Later

**After making changes locally:**

```bash
# Edit files locally
# Then:
git add index.html style.css images/
git commit -m "Update contact info"
git push

# GitHub Pages auto-updates in 1-2 minutes
```

Or use GitHub web interface to edit files directly.

## Generating QR Code

### Option 1: Python Script (Recommended - Local Generation)

**Requirements:** Install the QR code library first:
```bash
pip install qrcode[pil]
```

**Generate QR codes with command-line argument:**
```bash
cd Python
python generate_qrcode.py https://yourusername.github.io/repository-name
```

**Or run interactively:**
```bash
cd Python
python generate_qrcode.py
# Then enter your URL when prompted
```

**Output:**
- Creates 6 PNG files in the `Share/` folder
- **3 sizes**: 300x300, 600x600, 1200x1200 pixels
- **2 colors**: Black and White versions of each size
- **Transparent backgrounds**: Perfect for any design
- **HIGH error correction**: Works even if 30% damaged
- **File naming**: `QRC_300x300_Black.png`, `QRC_600x600_White.png`, etc.

**Features:**
- ✓ Portable script - works in any project
- ✓ Automatically overrides old files when re-run
- ✓ No internet connection needed
- ✓ Professional quality for printing

**When to use each size:**
- **300x300**: Small prints, email signatures
- **600x600**: Standard business cards
- **1200x1200**: Large posters, banners, high-quality prints

### Option 2: Free Online Tools
1. Go to [qr-code-generator.com](https://www.qr-code-generator.com/)
2. Select **URL** type
3. Paste your GitHub Pages URL
4. Customize design (optional):
   - Add your logo in the center
   - Change colors to match your brand
5. Download high-resolution QR code
6. Print on business cards!

### Option 3: QR Code API
Use a URL like:
```
https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=YOUR_GITHUB_PAGES_URL
```

## Updating Content

### Replace Placeholder Images

1. Prepare your real images:
   - **Logo**: 400x400px square, JPEG or PNG, < 200KB
   - **Property photos**: 800x600px landscape, JPEG, < 200KB each

2. Name them exactly as the placeholders:
   - `logo.jpg` (your company logo)
   - `property-1.jpg` through `property-8.jpg`

3. Replace files in the `images/` folder

4. **Upload to GitHub**:
   - Go to your repository → `images` folder
   - Click on each file (e.g., `logo.jpg`)
   - Click the trash icon to delete
   - Upload your new file with the same name
   - Commit changes

5. Changes go live within 1-2 minutes!

### Update Contact Information

Edit `index.html`:

**Phone Number** (line ~26):
```html
<a href="tel:+5511YOURNUMBER" class="contact-item phone">
    <span class="text">+55 11 YOURNUMBER</span>
```

**Email** (line ~30):
```html
<a href="mailto:youremail@domain.com" class="contact-item email">
    <span class="text">youremail@domain.com</span>
```

**LinkedIn** (line ~73):
```html
<a href="https://www.linkedin.com/in/yourprofile" ...>
```

**Instagram** (line ~79):
```html
<a href="https://www.instagram.com/yourhandle" ...>
```

After editing, upload the updated `index.html` to GitHub.

## Customizing Design

### Change Colors

Edit `style.css` variables (lines 9-15):

```css
:root {
    --primary-blue: #2c5282;    /* Header background */
    --light-blue: #4299e1;      /* Hover effects */
    --dark-gray: #2d3748;       /* Footer background */
    /* ... */
}
```

### Add More Social Media Icons

1. Find SVG icons at [heroicons.com](https://heroicons.com/) or [fontawesome.com](https://fontawesome.com/)
2. Add the icon to the SVG sprite in `index.html` (inside the `<svg>` tag at the top of `<body>`):
```xml
<symbol id="whatsapp" viewBox="0 0 24 24">
    <path d="..."/>
</symbol>
```
3. Add link in `index.html` footer:
```html
<a href="https://wa.me/5511YOURNUMBER" class="social-link whatsapp">
    <svg class="social-icon">
        <use href="#whatsapp"></use>
    </svg>
    <span>WhatsApp</span>
</a>
```

## File Structure

```
VisitCard/
├── index.html                      # Main website file (includes embedded SVG icons)
├── style.css                       # All styling
├── README.md                       # This file
├── Python/                         # Python utility scripts
│   ├── create_placeholders.py     # Image generator script (optional)
│   └── generate_qrcode.py         # QR code generator script
├── Share/                          # QR code output folder (created by script)
│   └── QRC_*.png                  # Generated QR code files
├── images/                         # Website images
│   ├── logo.jpg                   # Your company logo
│   └── property-1.jpg to property-8.jpg
└── myDevelopment/                  # Development documentation
    ├── Plan.md                    # Original development plan
    ├── imageEnlargePlan.md        # Lightbox feature plan
    └── QRCodePlan.md              # QR code generator plan
```

## Testing Checklist

Before deploying, test these:

- [ ] Open `index.html` in mobile view (360px width)
- [ ] Click phone number → Should open phone dialer
- [ ] Click email → Should open email client
- [ ] Click social links → Should open in new tabs
- [ ] All 8 property images display correctly
- [ ] Logo displays in header
- [ ] Page looks professional and loads quickly

## Troubleshooting

**Images not showing on GitHub Pages?**
- Make sure image filenames match exactly (case-sensitive)
- Check that images were uploaded to the `images/` folder
- Wait 2-3 minutes for changes to deploy

**QR code doesn't work?**
- Test the URL directly in your phone browser first
- Make sure you used the complete GitHub Pages URL
- Ensure repository is set to Public

**Want to use a custom domain?**
- Purchase a domain (optional)
- In GitHub Pages settings, add your custom domain
- Update DNS records with your domain provider
- Generate new QR code with custom domain

## Cost Breakdown

- GitHub Pages hosting: **FREE** ✅
- Domain (optional): ~$10-15/year
- QR code generation: **FREE** ✅
- Total base cost: **$0/year** 🎉

## Support

For questions or issues:
- Check GitHub Pages documentation: [docs.github.com/pages](https://docs.github.com/pages)
- Refer to the development plan in `myDevelopment/Plan.md`

---

**Built with:** HTML5, CSS3, SVG
**Hosted on:** GitHub Pages
**Optimized for:** Mobile devices (QR code access)
