from PIL import Image
import os
os.chdir(r'C:\Users\memov\Desktop\ihd-solution.com')
for name in ['Logo.webp','Primer.webp','Segundo.webp','Quinto.webp','Sexto.webp']:
    path = os.path.join('assets','images', name)
    try:
        with Image.open(path) as img:
            print(name, img.width, img.height)
    except Exception as e:
        print(name, 'ERROR', e)
