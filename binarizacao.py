from PIL import Image
import time
import histograma

def execute(path):
    
    img = Image.open(path)
    pixels = img.load()
    list = [[0 for x in range(img.width)] for y in range(img.height)]

    for i in range(0,img.width):
        for j in range(0,img.height):
            fator = pixels[i,j]
            if fator > 127:
                img.putpixel((i,j),246)
                list[i][j] = 246
            else:
                img.putpixel((i,j),0)
                list[i][j] = 0
    
    histograma.saveHistogram('histogram.txt',list,img.width,img.height)
            
    img.save("result.bmp")
     
