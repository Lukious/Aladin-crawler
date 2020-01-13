from PIL import Image
import numpy
import os,glob

categori = "컴퓨터"
# 가정요리뷰티 / 과학 / 대중예술 / 소설시 / 여행 / 유아 / 인문학 / 종교 / 중등참고서 / 컴퓨

folder_path = './img/' + categori

def PNG_case(filename):
    im = Image.open(folder_path+'/'+filename)
    size = (90, 120)
    im = im.resize(size)  
    im.save('./Preprocessed/'+categori+'/'+filename[:-4]+'.png')

def JPG_case(filename):
    im = Image.open(folder_path+'/'+filename)
    size = (90, 120)
    im = im.resize(size)  
    im.save('./Preprocessed/'+categori+'/' + filename[:-4]+'.png')

def Image2Matrix(filename):
    im = Image.open(folder_path+'/'+filename)
    size = (56, 56)
    im.resize(size)  
    ImageMatrix = numpy.asarray(im.convert('L'))
    numpy.save('./Preprocessed/'+categori+'/'+filename[:-4],ImageMatrix)


for filename in os.listdir(folder_path):
    print(filename)
    if(filename[-3:] == 'png'):
        PNG_case(filename)
    elif(filename[-3:] == 'jpg'):
        JPG_case(filename)
    #Image2Matrix(filename)