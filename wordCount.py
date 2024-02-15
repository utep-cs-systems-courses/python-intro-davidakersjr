#! /usr/bin/env python3 #Add to every file
import sys       
import re         
import os        
import subprocess


def wordCount(inputFile, outputFile):
        inF = os.open(inputFile, os.O_RDWR)
        words = True
        wordDic = {}
        bit = os.stat(inF).st_size #finds size of file in byte form
        file =  os.read(inF, bit) #tells it to read x amount of bytes

        outF = os.open(outputFile, os.O_RDWR)#trucncate next time
        pos = 0
        temp2 = ''
        temp = file.decode('utf-8')        
        isPunc = False
        
        for string in temp: #for chars in strings in temp
                if not checkChar(string):
                        if string.isspace() or string == '-' or string == "'":
                                if temp2:
                                        temp2 = temp2.strip()
                                        if temp2 in wordDic:
                                                wordDic[temp2]+= 1
                                        else:
                                                wordDic[temp2] = 1
                                        temp2 = ''
                        else:         
                                temp2+= string.lower()
                                    
                        
                
                        
                        
                                
                #print(temp3)
                


        sortWordDic = {key: value for key, value in sorted(wordDic.items())} #key : value for new dictionary for all keys, values from wordDic.items which is a pair
        
        for key, value in sortWordDic.items(): #for key value pair in sorted word dictionary it iterates through the items to pass them encoded as bytes as pairs in this format
                byteType = (f"{key} {value}\n").encode('utf-8')
                os.write(outF, byteType)
                
        #print(wordDic)
                        
                
        os.close(outF)  
        os.close (inF)

        
punctuation = {",",".",":",";"} #punctuation set so we can see if a char is in the set therefor a punctuation
        
def checkChar(i):
        if i in punctuation:
                return True
        else:
                return False
        
        
        
        
inputTo = sys.argv[1]
outputTo = sys.argv[2]

wordCount(inputTo, outputTo)


 

