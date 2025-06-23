from PIL import Image, ImageEnhance, ImageFilter

# Load image
img = Image.open("your_image_path.jpg")

# Apply blur filter
img = img.filter(ImageFilter.GaussianBlur(2))

# Adjust color
enhancer = ImageEnhance.Color(img)
img = enhancer.enhance(1.5)  # Increase color saturation

# Save modified image
img.save("modified_image.jpg")
