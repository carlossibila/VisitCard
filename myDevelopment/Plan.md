# Digital Business Card - Real Estate Website Plan

## Project Overview
Create a mobile-optimized single-page website for Sibila Real State business card, accessible via QR code. The page will be hosted on GitHub Pages for zero cost.

## User Requirements - CONFIRMED
- **Target Device**: Mobile phones (QR code access)
- **Business Type**: Real estate
- **Business Name**: Sibila Real State
- **Color Scheme**: Professional blue/gray/white (trust & stability)
- **Hosting**: GitHub Pages (free)
- **Development Approach**: Create locally first, then deploy

## Content Details
- **Logo/Profile**: Company logo in header
- **Property Gallery**: 8 photos in scrollable gallery
- **Contact Info**:
  - Cell: +55 11 55248-5847 (Brazilian format)
  - Email: email@emailcompany.com.br
- **Social Media**: LinkedIn and Instagram (placeholder links to homepages)

## Technical Approach

### Phase 1: GitHub Pages Deployment
**Steps for user (detailed in README.md):**
1. Create free GitHub account at github.com
2. Create new public repository named `sibila-card` or similar
3. Upload files from root `VisitCard/` folder to repository (index.html, style.css, images/, README.md)
   - Note: myDevelopment/ folder is for local tracking only, don't upload it to GitHub
4. Go to repository Settings → Pages
5. Enable GitHub Pages (source: main branch, root folder)
6. Wait 2-3 minutes for deployment
7. Access site at: `username.github.io/sibila-card`
8. Generate QR code using free tool (qr-code-generator.com) pointing to the URL
9. Test QR code with phone to ensure it works
10. Print QR code on business cards

### Phase 2: Content Updates (After Deployment)
**To replace placeholders with real content:**
1. Replace logo.jpg with actual company logo
2. Replace property-1.jpg through property-8.jpg with real property photos
3. Update email in index.html (if needed)
4. Update LinkedIn and Instagram URLs in index.html
5. Commit and push changes to GitHub
6. Changes appear live within 1-2 minutes

## Design Specifications

### Layout Structure (Mobile-First)
```
┌─────────────────────────────┐
│  [LOGO]  Sibila Real State  │ ← Header (logo + business name)
│                             │   Blue-gray background
├─────────────────────────────┤
│   📱 +55 11 55248-5847      │ ← Contact section (clickable)
│   ✉️  email@emailcompany... │   Light gray background
├─────────────────────────────┤
│   Property Gallery          │
│  ┌───┬───┬───┬───┐         │ ← 8-photo grid gallery
│  │ 1 │ 2 │ 3 │ 4 │         │   2 columns, 4 rows
│  ├───┼───┼───┼───┤         │   Colored placeholders
│  │ 5 │ 6 │ 7 │ 8 │         │
│  └───┴───┴───┴───┘         │
├─────────────────────────────┤
│   [LinkedIn] [Instagram]    │ ← Footer with social icons
│                             │   Dark gray background
└─────────────────────────────┘
```

### Color Palette (Professional Real Estate)
- **Primary Blue**: #2c5282 (header, accents)
- **Light Blue**: #4299e1 (hover states)
- **Dark Gray**: #2d3748 (footer, text)
- **Medium Gray**: #718096 (secondary text)
- **Light Gray**: #edf2f7 (contact section background)
- **White**: #ffffff (background, text on dark)

### Technology Stack
- **HTML5**: Semantic structure
- **CSS3**: Modern styling, CSS Grid for gallery, Flexbox for layout
- **No JavaScript**: Keep it simple and fast-loading
- **No frameworks**: Pure HTML/CSS for zero dependencies
- **Mobile viewport**: Optimized for 360px-428px width

### Key Features
- Click-to-call phone link (`tel:` protocol)
- Click-to-email link (`mailto:` protocol)
- Responsive image gallery (2-column grid on mobile)
- Social media icons with external links
- Fast loading with optimized images
- Professional, clean aesthetic

## Project File Structure
```
VisitCard/                      # Main project folder
├── index.html                  # Main HTML file
├── style.css                   # All styling (mobile-first)
├── README.md                   # GitHub Pages deployment guide
├── images/                     # Image assets
│   ├── logo.jpg               # Company logo/profile (placeholder)
│   ├── property-1.jpg         # Property photo 1 (placeholder)
│   ├── property-2.jpg         # Property photo 2 (placeholder)
│   ├── property-3.jpg         # Property photo 3 (placeholder)
│   ├── property-4.jpg         # Property photo 4 (placeholder)
│   ├── property-5.jpg         # Property photo 5 (placeholder)
│   ├── property-6.jpg         # Property photo 6 (placeholder)
│   ├── property-7.jpg         # Property photo 7 (placeholder)
│   └── property-8.jpg         # Property photo 8 (placeholder)
└── myDevelopment/             # Development tracking folder
    └── Plan.md                # This plan document (for easy reference)
```

## Implementation Steps

### Step 1: Create HTML Structure
**File**: `VisitCard/index.html`
- Semantic HTML5 structure
- Meta tags for mobile optimization (viewport, charset)
- Header section: Logo + "Sibila Real State" text
- Contact section: Phone and email with clickable links
- Gallery section: 8 images in CSS Grid layout
- Footer: LinkedIn and Instagram icon/links
- Use colored div placeholders for images initially

### Step 2: Create CSS Styling
**File**: `VisitCard/style.css`
- CSS reset for consistent rendering
- Mobile-first approach (default styles for 360px-428px)
- Professional blue/gray/white color scheme
- Flexbox for header and footer layout
- CSS Grid for 2-column photo gallery
- Hover effects for links and social icons
- Typography: Clean, readable fonts (system fonts)
- Spacing and padding for mobile usability

### Step 3: Create Placeholder Images
**Folder**: `VisitCard/images/`
- Create 9 colored placeholder images:
  - `logo.jpg`: 200x200px square (company logo placeholder)
  - `property-1.jpg` to `property-8.jpg`: 400x300px landscape (gallery placeholders)
- Use different colors to distinguish each placeholder
- Keep file sizes small for fast loading

### Step 4: Create Deployment Guide
**File**: `VisitCard/README.md`
- Step-by-step GitHub Pages setup instructions
- How to replace placeholder images with real photos
- How to generate QR code from final URL
- Tips for updating content later

### Step 5: Local Testing
- Open `index.html` in browser
- Test in mobile view (Chrome DevTools responsive mode)
- Verify all links work (tel: and mailto:)
- Check layout on different screen sizes
- Ensure professional appearance

### Step 6: Create Plan Document
**File**: `VisitCard/myDevelopment/Plan.md`
- Copy this plan to myDevelopment folder for easy tracking
- User can reference design decisions and progress
- Keeps development documentation organized

## Critical Files to Create
1. `VisitCard/index.html` - Main page structure with Sibila Real State content
2. `VisitCard/style.css` - Complete styling with blue/gray theme
3. `VisitCard/images/` - Folder with 9 placeholder images
4. `VisitCard/README.md` - GitHub Pages deployment instructions
5. `VisitCard/myDevelopment/Plan.md` - This plan document (copy for reference)

## Success Criteria
- ✅ Page loads quickly on mobile (< 2 seconds)
- ✅ All contact info is clickable (tel: and mailto: links)
- ✅ Professional blue/gray design suitable for real estate
- ✅ Logo prominently displayed in header
- ✅ 8-photo gallery displays properly on mobile
- ✅ Social media links work correctly
- ✅ Easy to preview locally before deployment
- ✅ Simple to update content later (just edit HTML/replace images)
- ✅ Zero hosting costs via GitHub Pages
- ✅ QR code successfully opens website on mobile devices

## Technical Notes

### Image Optimization
- Placeholder images will be colored divs with CSS
- Real images should be:
  - Logo: 400x400px max, optimized JPEG/PNG
  - Properties: 800x600px max, optimized JPEG
  - Keep file sizes under 200KB each for fast loading

### Browser Compatibility
- Modern mobile browsers (Chrome, Safari, Firefox, Edge)
- No legacy browser support needed (users scan from phones)

### Accessibility
- Semantic HTML for screen readers
- Alt text for all images
- Sufficient color contrast (WCAG AA)
- Touch-friendly tap targets (min 44x44px)

## Next Steps After Plan Approval
1. Check if `VisitCard/myDevelopment/` folder exists (user mentioned it exists)
2. Create `VisitCard/index.html` - Complete HTML structure
3. Create `VisitCard/style.css` - Mobile-first styling
4. Create `VisitCard/images/` folder with 9 placeholder images (colored backgrounds)
5. Create `VisitCard/README.md` - Deployment and update instructions
6. Copy this plan to `VisitCard/myDevelopment/Plan.md` for user reference
7. Test locally in browser (mobile view)
8. Guide user through GitHub Pages deployment (upload only root files, not myDevelopment/)
9. Help generate QR code for final URL
10. Provide instructions for updating placeholders with real photos/content
