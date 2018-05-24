from PIL import Image
import histograma

def execute(path):
    
    img = Image.open(path)
    pixels = img.load()
    
    list = [[0 for x in range(img.width)] for y in range(img.height)]
    
    channel = 247
    
    auxiliar = [0] * channel
    novo = [0] * channel
    ideal = (img.width * img.height) / channel
    
    for i in range(0,img.width):
        for j in range(0,img.height):
            
            color = pixels[i,j]
            auxiliar[color] = auxiliar[color] + 1
            
    auxiliarValor = 0
    for x in range(0,channel):
        auxiliarValor = auxiliarValor + auxiliar[x]
        if (((auxiliarValor/ideal) - 1) > 0):
            novo[x] = (auxiliarValor/ideal) - 1
        else:
            novo[x] = 0
    
    for i in range(0,img.width):
        for j in range(0,img.height):
            color = pixels[i,j]
            list[i][j] = novo[color] 
            img.putpixel((i,j),novo[color])
                  
    
    histograma.saveHistogram('histogram.txt',list,img.width,img.height)        
    img.save("result.bmp")
