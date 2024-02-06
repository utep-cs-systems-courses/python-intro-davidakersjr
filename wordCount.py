import sys       
import re         
import os        
import subprocess

def wordCount(inputFile, outputFile):
        inF = os.open(inputFile, os.O_RDWR)
        words = True
        wordDic = {}
        bit = 0
        temp = os.read(inF, bit)
        outF = os.open(outputFile, os.O_RDWR)
        while temp.decode('utf-8') != '\n':

                temp2 = temp.decode('utf-8')
                if temp2 in wordDic:
                        wordDic[temp2]+= 1
                else:
                        wordDic[temp2] = 1
                        
                bit+=1
                temp = os.read(inF, bit)
                
        for key, value in wordDic.items():
                byteType = (f"{key}: {value}\n").encode('utf-8')
                os.write(outF, byteType)        
        print(wordDic)
                        
                
        os.close(outF)  
        os.close (inF)

inputTo = sys.argv[1]
outputTo = sys.argv[2]

wordCount(inputTo, outputTo)


 

