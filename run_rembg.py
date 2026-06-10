from rembg import remove
from PIL import Image
import os

def main():
    input_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\0910b676-633f-4297-8aa3-640f47c4d789\media__1781097685166.png'
    output_path = r'public\images\logo_final.png'
    
    if os.path.exists(input_path):
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print("Successfully removed background!")
    else:
        print("Input file not found.")

if __name__ == "__main__":
    main()
