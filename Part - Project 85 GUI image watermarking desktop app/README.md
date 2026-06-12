# GUI Image Watermarking Desktop Application

## Project Overview
A desktop application built with Tkinter and PIL (Pillow) for adding text watermarks to images. This tool provides a user-friendly interface for opening images, applying customizable watermarks, and saving the results.

## Technologies Used
- Python 3.x
- Tkinter (GUI framework)
- PIL/Pillow (image processing)
- File dialog operations
- RGB/HEX color conversion
- Image manipulation and compositing

## Project Structure
```
Part - Project 85 GUI image watermarking desktop app/
├── ImageDesktop.py      # Main GUI application
└── README.md           # This file
```

## Features
- **Image Support**: Open common image formats (PNG, JPG, JPEG)
- **Customizable Watermark**: Text input with font, size, and color options
- **Preview System**: Real-time watermark preview before applying
- **Position Control**: Watermark placement options
- **Transparency Support**: Adjustable watermark opacity
- **Save Functionality**: Export watermarked images
- **User-Friendly Interface**: Clean, intuitive GUI design
- **Error Handling**: Graceful handling of invalid inputs

## Installation
### Prerequisites
1. Python 3.x installed
2. Install required packages:
   ```bash
   pip install pillow
   ```

### Running the Application
```bash
python ImageDesktop.py
```

## User Interface
### Main Window Components
1. **Text Entry Field**: For watermark text input
2. **Open Image Button**: Browse and select image files
3. **Apply Watermark Button**: Preview watermark on selected image
4. **Save Button**: Export watermarked image
5. **Preview Area**: Display image with watermark
6. **Color Customization**: RGB color picker (planned feature)

## Code Structure
### Color Conversion Utility
```python
def rgb_a_hex(r, g, b):
    """Convert RGB values to hexadecimal color code."""
    return f"#{r:02x}{g:02x}{b:02x}"
```

### Main Application Class
```python
class AppWatermark:
    def __init__(self, root):
        self.root = root
        self.image = None
        self.photo = None
        
        # Dark theme colors
        bg_color = rgb_a_hex(30, 30, 40)
        
        root.configure(bg=bg_color)
        root.title("Image Watermark App")
        
        # Create main frame
        frame = tk.Frame(root, bg=bg_color)
        frame.pack(fill="both", expand=True)
        
        # Watermark text entry
        self.entry = tk.Entry(frame, width=40, bg=bg_color, fg="white")
        self.entry.pack(pady=5)
        self.entry.insert(0, "© My Name")  # Default watermark text
        
        # Control buttons
        tk.Button(frame, text="Open Image", command=self.open_image).pack(pady=5)
        tk.Button(frame, text="Apply Watermark", command=self.apply_watermark).pack(pady=5)
        tk.Button(frame, text="Save", command=self.save).pack(pady=5)
        
        # Preview area
        self.preview = tk.Label(frame, bg=bg_color)
        self.preview.pack()
```

## Core Functions
### Open Image Function
```python
def open_image(self):
    """Open an image file using file dialog."""
    from tkinter import filedialog
    
    path = filedialog.askopenfilename(
        filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    
    if not path:
        return  # User cancelled
    
    try:
        self.image = Image.open(path).convert("RGBA")
        self.show_preview(self.image)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open image: {e}")
```

### Apply Watermark Function
```python
def apply_watermark(self):
    """Apply text watermark to the current image."""
    if self.image is None:
        messagebox.showwarning("Warning", "Open an image first")
        return
    
    text = self.entry.get().strip()
    if not text:
        messagebox.showwarning("Warning", "Enter watermark text")
        return
    
    try:
        # Create watermark layer
        watermark_layer = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark_layer)
        
        # Calculate font size based on image dimensions
        base_font_size = max(self.image.size) // 20
        font = ImageFont.truetype("arial.ttf", base_font_size)
        
        # Calculate text position (center)
        text_width, text_height = draw.textsize(text, font=font)
        position = (
            (self.image.width - text_width) // 2,
            (self.image.height - text_height) // 2
        )
        
        # Draw text with semi-transparency
        draw.text(
            position,
            text,
            font=font,
            fill=(255, 255, 255, 128)  # White with 50% opacity
        )
        
        # Composite images
        watermarked = Image.alpha_composite(self.image, watermark_layer)
        self.show_preview(watermarked)
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to apply watermark: {e}")
```

### Save Function
```python
def save(self):
    """Save the watermarked image to file."""
    if self.image is None:
        messagebox.showwarning("Warning", "No image to save")
        return
    
    path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg *.jpeg"),
            ("All files", "*.*")
        ]
    )
    
    if not path:
        return  # User cancelled
    
    try:
        # Convert to RGB if saving as JPEG
        if path.lower().endswith(('.jpg', '.jpeg')):
            save_image = self.image.convert("RGB")
        else:
            save_image = self.image
        
        save_image.save(path)
        messagebox.showinfo("Success", f"Image saved to:\n{path}")
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save image: {e}")
```

## Advanced Features
### Watermark Customization Options
```python
class WatermarkSettings:
    """Manage watermark customization settings."""
    
    def __init__(self):
        self.text = "© Watermark"
        self.font_name = "arial.ttf"
        self.font_size = 40
        self.color = (255, 255, 255)  # White
        self.opacity = 128  # 50% (0-255)
        self.position = "center"  # center, top-left, bottom-right, etc.
        self.rotation = 0  # Degrees
        
    def apply_to_image(self, image):
        """Apply current settings to an image."""
        # Create watermark layer
        layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(layer)
        
        # Load font
        try:
            font = ImageFont.truetype(self.font_name, self.font_size)
        except IOError:
            font = ImageFont.load_default()
        
        # Calculate position based on setting
        text_width, text_height = draw.textsize(self.text, font=font)
        position = self._calculate_position(image.size, text_width, text_height)
        
        # Apply rotation if needed
        if self.rotation != 0:
            layer = layer.rotate(self.rotation, expand=True, resample=Image.BICUBIC)
        
        # Draw text
        draw.text(
            position,
            self.text,
            font=font,
            fill=self.color + (self.opacity,)
        )
        
        # Composite with original image
        return Image.alpha_composite(image.convert("RGBA"), layer)
    
    def _calculate_position(self, image_size, text_width, text_height):
        """Calculate text position based on settings."""
        img_width, img_height = image_size
        
        positions = {
            "center": ((img_width - text_width) // 2, (img_height - text_height) // 2),
            "top-left": (10, 10),
            "top-right": (img_width - text_width - 10, 10),
            "bottom-left": (10, img_height - text_height - 10),
            "bottom-right": (img_width - text_width - 10, img_height - text_height - 10),
            "top-center": ((img_width - text_width) // 2, 10),
            "bottom-center": ((img_width - text_width) // 2, img_height - text_height - 10),
        }
        
        return positions.get(self.position, positions["center"])
```

### Batch Processing
```python
def batch_watermark(input_folder, output_folder, settings):
    """Apply watermark to all images in a folder."""
    import os
    from pathlib import Path
    
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    
    # Create output folder if it doesn't exist
    output_path.mkdir(exist_ok=True)
    
    supported_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.gif'}
    
    for file_path in input_path.iterdir():
        if file_path.suffix.lower() in supported_extensions:
            try:
                # Open and process image
                image = Image.open(file_path).convert("RGBA")
                watermarked = settings.apply_to_image(image)
                
                # Save with appropriate format
                output_file = output_path / file_path.name
                if output_file.suffix.lower() in {'.jpg', '.jpeg'}:
                    watermarked = watermarked.convert("RGB")
                
                watermarked.save(output_file)
                print(f"Processed: {file_path.name}")
                
            except Exception as e:
                print(f"Error processing {file_path.name}: {e}")
```

### Preview System
```python
def show_preview(self, image):
    """Display image in preview area with proper scaling."""
    # Resize for preview while maintaining aspect ratio
    max_preview_size = (600, 400)
    
    # Calculate scaling factor
    width_ratio = max_preview_size[0] / image.width
    height_ratio = max_preview_size[1] / image.height
    scale_factor = min(width_ratio, height_ratio, 1.0)  # Don't enlarge
    
    new_size = (
        int(image.width * scale_factor),
        int(image.height * scale_factor)
    )
    
    # Resize image
    preview_image = image.resize(new_size, Image.Resampling.LANCZOS)
    
    # Convert to PhotoImage for Tkinter
    self.photo = ImageTk.PhotoImage(preview_image)
    self.preview.config(image=self.photo)
    self.preview.image = self.photo  # Keep reference
```

## Image Processing Techniques
### Multiple Watermark Styles
```python
class WatermarkStyles:
    """Different watermark style implementations."""
    
    @staticmethod
    def text_watermark(image, text, **kwargs):
        """Standard text watermark."""
        # Implementation as shown above
        pass
    
    @staticmethod
    def tiled_watermark(image, text, **kwargs):
        """Tile watermark across entire image."""
        layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(layer)
        font = ImageFont.truetype("arial.ttf", 20)
        
        # Tile pattern
        text_width, text_height = draw.textsize(text, font=font)
        for x in range(0, image.width, text_width + 20):
            for y in range(0, image.height, text_height + 20):
                draw.text((x, y), text, font=font, fill=(255, 255, 255, 64))
        
        return Image.alpha_composite(image, layer)
    
    @staticmethod
    def diagonal_watermark(image, text, **kwargs):
        """Diagonal watermark across image."""
        layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(layer)
        font = ImageFont.truetype("arial.ttf", 60)
        
        # Draw at 45-degree angle
        draw.text((50, 50), text, font=font, fill=(255, 255, 255, 64))
        
        # Rotate layer
        layer = layer.rotate(45, expand=False, center=(50, 50))
        
        return Image.alpha_composite(image, layer)
    
    @staticmethod
    def logo_watermark(image, logo_path, **kwargs):
        """Logo/image-based watermark."""
        try:
            logo = Image.open(logo_path).convert("RGBA")
            
            # Resize logo
            logo_size = min(image.size) // 4
            logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            # Position in bottom-right corner
            position = (
                image.width - logo.width - 20,
                image.height - logo.height - 20
            )
            
            # Create composite
            composite = image.copy()
            composite.paste(logo, position, logo)
            
            return composite
            
        except Exception as e:
            print(f"Logo watermark error: {e}")
            return image
```

## Color Management
### Color Picker Integration
```python
def add_color_picker(self):
    """Add color picker widget to GUI."""
    from tkinter import colorchooser
    
    def choose_color():
        color_code = colorchooser.askcolor(title="Choose Watermark Color")[1]
        if color_code:
            self.watermark_color = color_code
            # Update preview if image exists
            if self.image:
                self.apply_watermark()
    
    color_button = tk.Button(
        self.control_frame,
        text="Choose Color",
        command=choose_color,
        bg="#4a4a5a",
        fg="white"
    )
    color_button.pack(pady=5)
```

### Opacity Control
```python
def add_opacity_control(self):
    """Add opacity slider to GUI."""
    opacity_label = tk.Label(self.control_frame, text="Opacity:", bg=self.bg_color, fg="white")
    opacity_label.pack()
    
    self.opacity_var = tk.IntVar(value=128)  # Default 50%
    
    opacity_scale = tk.Scale(
        self.control_frame,
        from_=0,
        to=255,
        orient=tk.HORIZONTAL,
        variable=self.opacity_var,
        command=self.update_opacity,
        bg=self.bg_color,
        fg="white",
        troughcolor="#4a4a5a"
    )
    opacity_scale.pack(fill=tk.X, padx=10)
```

## Error Handling and Validation
### Input Validation
```python
def validate_inputs(self):
    """Validate all user inputs before processing."""
    errors = []
    
    # Check if image is loaded
    if self.image is None:
        errors.append("No image loaded")
    
    # Check watermark text
    text = self.entry.get().strip()
    if not text:
        errors.append("Watermark text is empty")
    elif len(text) > 100:
        errors.append("Watermark text too long (max 100 characters)")
    
    # Check save path if saving
    if hasattr(self, 'save_path') and self.save_path:
        if not os.path.exists(os.path.dirname(self.save_path)):
            errors.append("Save directory does not exist")
    
    return errors
```

### Graceful Error Recovery
```python
def safe_image_operation(self, operation, *args, **kwargs):
    """Execute image operation with error handling."""
    try:
        return operation(*args, **kwargs)
    except IOError as e:
        messagebox.showerror("File Error", f"Cannot read/write file: {e}")
    except MemoryError:
        messagebox.showerror("Memory Error", "Image too large for available memory")
    except Exception as e:
        messagebox.showerror("Processing Error", f"Unexpected error: {e}")
    return None
```

## Performance Optimization
### Image Caching
```python
class ImageCache:
    """Cache processed images for better performance."""
    
    def __init__(self, max_size=5):
        self.cache = {}
        self.max_size = max_size
        self.access_order = []
    
    def get(self, key):
        """Get image from cache."""
        if key in self.cache:
            # Update access order
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None
    
    def put(self, key, image):
        """Store image in cache."""
        if len(self.cache) >= self.max_size:
            # Remove least recently used
            lru_key = self.access_order.pop(0)
            del self.cache[lru_key]
        
        self.cache[key] = image
        self.access_order.append(key)
```

### Thumbnail Generation
```python
def generate_thumbnail(image, size=(200, 200)):
    """Generate thumbnail for faster preview."""
    # Maintain aspect ratio
    image.thumbnail(size, Image.Resampling.LANCZOS)
    return image
```

## Project Purpose
This project demonstrates:
- Desktop GUI application development with Tkinter
- Image processing with PIL/Pillow library
- File dialog operations and file handling
- User interface design principles
- Image manipulation techniques (compositing, transparency)
- Color management and conversion
- Error handling and input validation
- Performance optimization for image processing