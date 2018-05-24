import codecs


def saveHistogram(filename, list, width, height):
    fileOutputText = codecs.open(filename,'w','utf-8')
    
    finalText = ''
    
    for x in xrange(0,width):
        for y in xrange(0,height):
            if list[x][y] > 246:
                list[x][y] = 246
            elif list[x][y] < 0:
                list[x][y] = 0                
            finalText = finalText + str(list[x][y]) + '\n'
        
    fileOutputText.write(u"\ufeff"+finalText)
    fileOutputText.close()  