# Image Enlarge Feature - Enhancement Plan

## Overview
Add click-to-enlarge functionality for property gallery images. When users click/tap a property photo, it opens in a full-screen lightbox modal for better viewing.

## User Experience
1. User clicks on any property image in the gallery
2. Image enlarges to full screen with dark overlay
3. User can close by:
   - Clicking the X button
   - Clicking outside the image
   - Pressing ESC key (desktop)

## Implementation

### Step 1: Create JavaScript File

**File**: `script.js` (new file in root)

```javascript
// Image Lightbox Functionality
document.addEventListener('DOMContentLoaded', function() {
    // Create modal elements
    const modal = document.createElement('div');
    modal.className = 'image-modal';
    modal.innerHTML = `
        <div class="modal-content">
            <span class="modal-close">&times;</span>
            <img src="" alt="" class="modal-image">
        </div>
    `;
    document.body.appendChild(modal);

    const modalImage = modal.querySelector('.modal-image');
    const closeBtn = modal.querySelector('.modal-close');

    // Add click handlers to all gallery images
    const galleryImages = document.querySelectorAll('.gallery-image');

    galleryImages.forEach(image => {
        // Add pointer cursor hint
        image.style.cursor = 'pointer';

        // Click to open modal
        image.addEventListener('click', function() {
            modalImage.src = this.src;
            modalImage.alt = this.alt;
            modal.classList.add('active');
            document.body.style.overflow = 'hidden'; // Prevent background scrolling
        });
    });

    // Close modal functions
    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = ''; // Restore scrolling
    }

    // Close button click
    closeBtn.addEventListener('click', closeModal);

    // Click outside image to close
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

    // ESC key to close
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
});
```

### Step 2: Add Script Reference to HTML

**File**: `index.html`

Add before closing `</body>` tag (line ~84):

```html
    <script src="script.js"></script>
</body>
</html>
```

### Step 3: Add Modal Styles to CSS

**File**: `style.css`

Add at the end of the file:

```css
/* Image Modal / Lightbox */
.image-modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.95);
    z-index: 9999;
    animation: fadeIn 0.3s ease;
}

.image-modal.active {
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal-content {
    position: relative;
    max-width: 90%;
    max-height: 90vh;
    padding: 20px;
}

.modal-image {
    width: 100%;
    height: auto;
    max-height: 90vh;
    object-fit: contain;
    border-radius: 8px;
}

.modal-close {
    position: absolute;
    top: -10px;
    right: -10px;
    font-size: 40px;
    color: var(--white);
    background-color: var(--primary-blue);
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    line-height: 1;
    transition: background-color 0.3s ease;
}

.modal-close:hover {
    background-color: var(--light-blue);
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

/* Add cursor pointer hint to gallery images */
.gallery-image {
    cursor: pointer;
    transition: transform 0.2s ease, opacity 0.2s ease;
}

.gallery-image:hover {
    transform: scale(1.02);
    opacity: 0.9;
}
```

## Benefits

✅ **Better property viewing** - Clients can see details clearly
✅ **Professional touch** - Modern, expected functionality
✅ **Mobile-friendly** - Works on phones and tablets
✅ **Zero dependencies** - Pure vanilla JavaScript, no libraries
✅ **Lightweight** - ~1KB of code added
✅ **Accessible** - Keyboard navigation (ESC to close)

## File Changes Summary

**New Files:**
- `script.js` - Lightbox functionality

**Modified Files:**
- `index.html` - Add `<script src="script.js"></script>` before `</body>`
- `style.css` - Add modal styles (append to end)

**No changes needed:**
- Images stay the same
- Existing HTML structure unchanged
- No impact on GitHub Pages deployment

## Estimated Time to Implement
- 5 minutes to create files
- 2 minutes to test locally
- Total: ~7 minutes

## Testing Checklist

After implementation:
- [ ] Click any property image → Opens enlarged
- [ ] Click X button → Closes modal
- [ ] Click outside image → Closes modal
- [ ] Press ESC key → Closes modal (desktop)
- [ ] Test on mobile → Tap works smoothly
- [ ] Background doesn't scroll when modal open
- [ ] Images display at good quality when enlarged

## Deployment Notes

Since this adds a JavaScript file:
1. Upload `script.js` to GitHub repository root
2. Ensure `index.html` references it correctly
3. GitHub Pages will serve it automatically
4. No special configuration needed

## Alternative: CSS-Only Solution

If client prefers zero JavaScript, there's a CSS-only option using `:target` pseudo-class, but it's less user-friendly (requires URL changes, no ESC key, more HTML markup).

**Recommendation**: Use JavaScript solution for better UX.

## Future Enhancements (Optional)

If client wants more features later:
- Add prev/next arrows to navigate between images
- Add image captions
- Add pinch-to-zoom on mobile
- Add loading spinner for large images
- Add swipe gestures on mobile

## Cost Impact

**Zero additional cost** - JavaScript runs in browser, no server needed.

---

**Status**: Ready to implement when client approves
**Priority**: Enhancement (not required for MVP)
**Risk**: Low (simple, well-tested pattern)
