# InternTrack CSS Design System

## Overview
All HTML templates inherit styling from `static/style.css` through the Jinja2 template inheritance system. Every page automatically receives the complete design system.

## How Style is Applied

### Template Hierarchy
```
base.html (links to style.css)
├── index.html (Dashboard)
├── applications.html (View all)
├── add_application.html (Form)
├── edit_application.html (Form)
└── statistics.html (Analytics)
```

Each template extends `base.html`, which includes:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

This means all child templates automatically receive all CSS styling.

## Color Palette

### Primary Colors
- **Primary Blue**: `#3498db` - Used for main buttons and links
- **Primary Dark**: `#667eea` to `#764ba2` - Gradient for headers/nav
- **Light Gray**: `#ecf0f1` - Background for disabled/secondary elements

### Status Colors
- **Applied**: `#3498db` (Blue)
- **Under Review**: `#f39c12` (Orange)
- **Interview Scheduled**: `#9b59b6` (Purple)
- **Rejected**: `#e74c3c` (Red)
- **Offer Extended**: `#27ae60` (Green)
- **Offer Accepted**: `#16a085` (Teal)

### Semantic Colors
- **Success**: `#27ae60` (Green)
- **Warning**: `#f39c12` (Orange)
- **Danger**: `#e74c3c` (Red)
- **Info**: `#3498db` (Blue)

## CSS Variables (Root)

```css
:root {
    --primary-color: #3498db;
    --secondary-color: #f39c12;
    --success-color: #27ae60;
    --danger-color: #e74c3c;
    --warning-color: #f39c12;
    --info-color: #3498db;
    --light-color: #ecf0f1;
    --dark-color: #2c3e50;
    --text-color: #34495e;
    --border-color: #bdc3c7;
    --shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 4px 16px rgba(0, 0, 0, 0.15);
}
```

## Component Classes

### Navigation (`.navbar`)
- Menu bar with gradient background
- Sticky positioning (stays at top while scrolling)
- Responsive mobile menu
- Logo with hover effect

**Used in:** base.html

### Buttons (`.btn`)
- `.btn-primary` - Main action button (blue)
- `.btn-secondary` - Secondary button (light gray)
- `.btn-small` - Compact button
- `.btn-edit` - Edit action (info color)
- `.btn-delete` - Delete action (danger color)

**Features:**
- Smooth hover effects with transform
- Hover elevation (translateY)
- Focus states for accessibility
- Responsive sizing

**Used in:** All templates with action buttons

### Dashboard (`.dashboard`)
- Main container for dashboard page
- Responsive grid layout
- Flex layout for cards

**Used in:** index.html

### Statistics Grid (`.stats-grid`)
- Responsive grid layout
- Auto-fit columns (min 250px)
- Card-based layout
- Hover animations

**Components:**
- `.stat-card` - Individual stat container
- `.stat-icon` - Large emoji/icon (80px)
- `.stat-value` - Large number (2.5rem)
- `.stat-detail` - Small secondary text

**Used in:** index.html, statistics.html

### Tables (`.applications-table`)
- Full-width responsive table
- Gradient header
- Striped rows
- Hover effects
- Responsive action column

**Components:**
- `thead` - Table header with gradient
- `tbody` - Table body with hover state
- `.company-cell` - Company name styling (colored)
- `.action-cell` - Button container

**Used in:** applications.html

### Forms (`.form`)
- Flex column layout
- `.form-group` - Input container
- `.form-page` - Page wrapper
- `.form-container` - Form wrapper with shadow

**Input Styling:**
- 2px border with focus states
- Smooth color transitions
- Focus shadow effect
- Properly spaced labels

**Used in:** add_application.html, edit_application.html

### Badges (`.badge`)
- Inline color-coded status indicator
- Rounded corners (border-radius: 20px)
- Padding and font styling
- Dynamic colors via inline style

**Used in:** Any template displaying status

### Status Breakdown (`.status-breakdown`)
- Visual bar chart for statuses
- `.status-item` - Individual item
- `.status-bar-container` - Container for bar
- `.status-bar` - Animated bar fill

**Features:**
- Percentage-based width calculation
- Smooth transitions
- Color-coded bars

**Used in:** index.html, statistics.html

### Empty State (`.empty-state`)
- Centered content container
- Encouraging message styling
- Call-to-action button

**Used in:** applications.html, statistics.html

### Alerts (`.alert`)
- Background color varies by type
- `.alert-error` - Error styling
- `.alert-success` - Success styling
- `.alert-warning` - Warning styling
- Left border for visual weight

**Used in:** Form templates

## Responsive Design

### Breakpoints

**Tablet & Smaller (max-width: 768px)**
- Stack navigation vertically
- Single column layouts
- Smaller padding/margins
- Adjusted font sizes

**Mobile (max-width: 480px)**
- Full-width buttons
- Minimal padding
- Single column everything
- Reduced navbar

### Responsive Features
- CSS Grid with `auto-fit`
- Flexbox for flexible layouts
- Mobile-first approach
- Touch-friendly button sizes

## Typography

### Font Stack
```css
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
```

### Font Sizes
- Headings: `h1` (2-2.5rem), `h2` (1.5rem), `h3` (1.2rem), `h4` (1.1rem)
- Body: 1rem
- Small: 0.85-0.95rem

### Line Height
- Default: 1.6 for readability
- Compact: 1.2-1.4 for headers

## Shadows & Elevation

### Drop Shadows
- **Standard**: `0 2px 8px rgba(0, 0, 0, 0.1)`
- **Large**: `0 4px 16px rgba(0, 0, 0, 0.15)`

### Used on:
- Cards (stat-card, app-card)
- Tables
- Forms
- Buttons on hover

## Animations & Transitions

### Hover Effects
- **Buttons**: `transform: translateY(-2px)` with shadow
- **Cards**: `transform: translateY(-5px)` with larger shadow
- **Links**: `opacity: 0.8` fade
- **Bars**: `transition: width 0.3s ease` smooth fill

### Timing
- Standard transition: `0.3s ease`
- CSS transforms for performance

## Accessibility Features

### Keyboard Navigation
- Focus states on inputs and buttons
- Visible focus indicators
- Proper tab order (semantic HTML)

### Color Contrast
- Text color on backgrounds meets WCAG standards
- Color-coded status + text labels (not color alone)

### Semantic HTML
- Proper heading hierarchy (h1, h2, h3, h4)
- Form labels associated with inputs
- Button elements for actions

## Layout System

### Container (`.container`)
- Max-width: 1200px
- Centered with margin: 0 auto
- Padding: 0 20px for mobile

### Grid Layouts
```css
display: grid;
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
gap: 2rem;
```

### Flexbox Layouts
- `.navbar .container` - Header navigation
- `.form` - Form fields stacking
- `.stats-card` - Icon and content side-by-side

## Browser Support

The CSS uses modern features with wide support:
- CSS Grid - All modern browsers
- Flexbox - All modern browsers
- CSS Variables - All modern browsers
- Transitions/Transforms - All modern browsers

**Supported Browsers:**
- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile Safari 14+
- Chrome Mobile

## How to Extend

### Add New Colors
1. Add to `:root` CSS variables
2. Use throughout with `var(--color-name)`

### Add New Components
1. Define class in style.css
2. Use in HTML templates
3. Test responsiveness

### Modify Styling
1. Edit `static/style.css`
2. Changes apply globally (no refresh needed in hot reload)
3. All templates inherit changes

## Performance Optimizations

### CSS Optimizations
- Single stylesheet (no multiple requests)
- CSS Variables reduce repetition
- No external fonts (system fonts)
- Minimal CSS for maximum coverage (1000+ lines of efficient CSS)

### File Size
- style.css: ~25KB (uncompressed)
- Will compress to ~8KB with gzip

## Testing Checklist

When modifying styles, verify:
- ✅ Desktop view (1920px+)
- ✅ Tablet view (768px)
- ✅ Mobile view (375-480px)
- ✅ Button hover/focus states
- ✅ Form input focus states
- ✅ Table scrolling on mobile
- ✅ Navigation on mobile
- ✅ Color contrast (accessibility)
- ✅ All templates load correctly

## File Structure

```
static/
├── style.css          # All styling rules (1000+ lines)
└── (no images or fonts needed)

templates/
├── base.html          # HTML structure + CSS link
├── index.html         # Uses .dashboard, .stats-grid
├── applications.html  # Uses .applications-table
├── add_application.html  # Uses .form-page, .form
├── edit_application.html # Uses .form-page, .form
└── statistics.html    # Uses .stats-grid, .status-breakdown
```

---

All HTML templates are fully styled through CSS inheritance. The design is consistent, responsive, and accessible across all pages.
