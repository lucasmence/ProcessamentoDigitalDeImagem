from PIL import Image
import histograma

def execute(path, newChannel):
    
    img = Image.open(path)
    pixels = img.load()
    
    list = [[0 for x in range(img.width)] for y in range(img.height)]
    
    linha =  img.width
    coluna = img.height
    pixel = 0
    auxiliar = [0] * 246

    if (linha > 0):
        if ((newChannel > 0) and (newChannel < 128)):
            divisao = 246 / newChannel
            auxiliarValor = 0

            for i in range(0,linha):
                for j in range(0,coluna):
                    pixel = pixels[i,j]
                    auxiliarValor = pixel % (divisao);
                    auxiliarValor = divisao - auxiliarValor - 1;
                    pixel = pixel + auxiliarValor
                    list[i][j] = pixel 
                    img.putpixel((i,j),pixel)
                      
    
    histograma.saveHistogram('histogram.txt',list,img.width,img.height)        
    img.save("result.bmp")














