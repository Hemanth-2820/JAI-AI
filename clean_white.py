from PIL import Image

def make_transparent_white():
    # Load the latest uploaded image with the white background
    img = Image.open(r'C:\Users\DELL\.gemini\antigravity-ide\brain\0910b676-633f-4297-8aa3-640f47c4d789\media__1781097685166.png').convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        r, g, b, a = item
        
        # We are looking for bright, low-saturation pixels (white, off-white, light gray)
        min_c = min(r, g, b)
        max_c = max(r, g, b)
        
        # If it's a bright pixel (min RGB > 190) and relatively neutral (difference between max and min < 40)
        if min_c > 180 and (max_c - min_c) < 40:
            # Map min_c from 180 (opaque) to 255 (fully transparent)
            # 255 -> alpha 0
            # 180 -> alpha 255
            alpha = int(255 - (min_c - 180) * (255.0 / 75.0))
            alpha = max(0, min(255, alpha))
            
            # Append pixel with new alpha
            newData.append((r, g, b, alpha))
        else:
            # Keep original pixel
            newData.append((r, g, b, 255))
            
    img.putdata(newData)
    img.save(r'public\images\logo_final_clean.png', "PNG")
    print("Cleaned white background and saved to logo_final_clean.png")

if __name__ == "__main__":
    make_transparent_white()
