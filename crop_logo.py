from PIL import Image

def crop_bottom():
    img = Image.open(r'public\images\logo_final_clean.png')
    width, height = img.size
    
    # The bright line is at the very bottom of the image.
    # We will crop the bottom 50 pixels off.
    crop_amount = 50
    cropped_img = img.crop((0, 0, width, height - crop_amount))
    
    cropped_img.save(r'public\images\logo_final_cropped.png', "PNG")
    print(f"Cropped {crop_amount} pixels from the bottom. Saved to logo_final_cropped.png")

if __name__ == "__main__":
    crop_bottom()
