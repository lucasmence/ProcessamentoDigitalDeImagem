from PIL import Image
import histograma

def execute(path):
    
    img = Image.open(path)
    imgHorizontal = Image.open(path)
    imgVertical = Image.open(path)
    pixels = img.load()
    
    lines = 3
    columns = 3
    matrix = [[-1 for x in range(columns)] for y in range(lines)]
    list = [[0 for x in range(img.width)] for y in range(img.height)]
    listHorizontal = [[0 for x in range(img.width)] for y in range(img.height)]
    listVertical = [[0 for x in range(img.width)] for y in range(img.height)]

    for i in range(0,img.width):
        for j in range(0,img.height):
            
            totalPixels = 0
            pixelSum = 0
            pixelSumX = 0
            pixelSumY = 0
            average = 0.00
            
            maskX = ((1,0,0),(0,-1,0),(0,0,0))
            maskY = ((0,0,1),(0,-1,0),(0,0,0))
            
            for x in range(0,lines):
                for y in range(0,columns):
                    if (i-1+x < 0) or (j-1+y < 0) or (i-1+x >= img.width) or (j-1+y >= img.width):
                        matrix[x][y] = -1
                    else:
                        matrix[x][y] = pixels[i-1+x,j-1+y]
                        
                        totalPixels = totalPixels + 1
                        if (maskX[x][y] >= 0):
                            pixelSumX = pixelSumX + ( maskX[x][y] * pixels[i-1+x,j-1+y] )
                        else:
                            pixelSumX = pixelSumX - ( maskX[x][y] * pixels[i-1+x,j-1+y] )
                            
                        if (maskX[x][y] >= 0):
                            pixelSumY = pixelSumY + ( maskY[x][y] * pixels[i-1+x,j-1+y] )
                        else:
                            pixelSumY = pixelSumY - ( maskY[x][y] * pixels[i-1+x,j-1+y] )
                            
                        
            if pixelSumX < 0:
                pixelSumX = pixelSumX * -1
            if pixelSumY < 0:
                pixelSumY = pixelSumY * -1
           # pixelSum =  pixelSumX + pixelSumY
           
           # pixelSumP1 = (matrix[0][0] + 0*matrix[0][1] + 0*matrix[0][2]) - (0*matrix[1][0] + (-1*matrix[1][1]) + 0*matrix[1][2])
           # pixelSumP2 = (0*matrix[0][0] + 0*matrix[0][1] + matrix[0][2]) - (0*matrix[1][0] + (-1*matrix[1][1]) + 0*matrix[1][2])
            
            pixelSumP1 = ((matrix[2][0] + matrix[2][1] + matrix[2][2]) - (matrix[0][0] + matrix[0][1] + matrix[0][2]))
            pixelSumP2 = ((matrix[0][2] + matrix[1][2] + matrix[2][2]) - (matrix[0][0] + matrix[1][0] + matrix[2][0]))
            
            if pixelSumP1 < 0:
                pixelSumP1 = pixelSumP1 * -1
            if pixelSumP2 < 0:
                pixelSumP2 = pixelSumP2 * -1
            
            pixelSum = pixelSumP1 + pixelSumP2 
            img.putpixel((i,j),pixelSum)
            imgHorizontal.putpixel((i,j),pixelSumP1)
            imgVertical.putpixel((i,j),pixelSumP2)
            list[i][j] = pixelSum
            listHorizontal[i][j] = pixelSumP1
            listVertical[i][j] = pixelSumP2
    
    histograma.saveHistogram('histogram.txt',list,img.width,img.height)
    histograma.saveHistogram('histogramHorizontal.txt',listHorizontal,img.width,img.height)
    histograma.saveHistogram('histogramVertical.txt',listVertical,img.width,img.height)
    
    img.save("result.bmp")
    imgHorizontal.save("resultHorizontal.bmp")
    imgVertical.save("resultVertical.bmp") 
