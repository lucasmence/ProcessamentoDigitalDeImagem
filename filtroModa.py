from PIL import Image
import histograma

def execute(path):
    
    img = Image.open(path)
    pixels = img.load()
    
    lines = 3
    columns = 3
    matrix = [[-1 for x in range(columns)] for y in range(lines)]
    list = [[0 for x in range(img.width)] for y in range(img.height)]

    for i in range(0,img.width):
        for j in range(0,img.height):
            
            totalPixels = 0
            pixelSum = 0
            popular = 0
            value = 0.00
            
            pixelList = [0] * 256
            
            for x in range(0,lines):
                for y in range(0,columns):
                    if (i-1+x < 0) or (j-1+y < 0) or (i-1+x >= img.width) or (j-1+y >= img.width):
                        matrix[x][y] = -1
                    else:
                        matrix[x][y] = pixels[i-1+x,j-1+y]
                        totalPixels = totalPixels + 1
                        pixelList[pixels[i-1+x,j-1+y]] = pixelList[pixels[i-1+x,j-1+y]] + 1
            
            
            for x in range(0,256):
                if (popular < pixelList[x]):
                    popular = x
            
            img.putpixel((i,j),popular)
            list[i][j] = popular
                           
            
    histograma.saveHistogram('histogram.txt',list,img.width,img.height)          
    img.save("result.bmp")