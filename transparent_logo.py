from PIL import Image, ImageDraw

def make_transparent():
    # Open the image and convert to RGBA
    img = Image.open('public/images/logo.jpg').convert("RGBA")
    
    # Use floodfill to replace the white background with transparency
    # Start at the four corners to ensure we get all the background
    # thresh=40 means it will match anything within 40 RGB values of the corner pixel (usually pure white)
    ImageDraw.floodfill(img, xy=(0, 0), value=(0, 0, 0, 0), thresh=40)
    ImageDraw.floodfill(img, xy=(img.width-1, 0), value=(0, 0, 0, 0), thresh=40)
    ImageDraw.floodfill(img, xy=(0, img.height-1), value=(0, 0, 0, 0), thresh=40)
    ImageDraw.floodfill(img, xy=(img.width-1, img.height-1), value=(0, 0, 0, 0), thresh=40)
    
    # Save it as a PNG to preserve transparency
    img.save('public/images/logo.png', "PNG")
    print("Background removed and saved as logo.png")

if __name__ == "__main__":
    make_transparent()
