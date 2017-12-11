LABEL_LIST = [2,8,9]#if you choice chipstar at first, you should change to 0
LABEL_NUM = "023/"

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
import os
import re
from PIL import Image
path = os.getcwd()
g= open("train.txt","w")


for file in os.listdir("Labels/"+LABEL_NUM):
    if ".txt" in file:
        print "I find the file"
        filename = file[:-4]+".JPEG"
        f = open("Labels/"+LABEL_NUM+file)
        h = open("converted_labels/"+file,"w")
        filepath = path + "/Images/"+LABEL_NUM+filename
        g.write(filepath+"\n")
        line_i = 0
        for line in f.readlines():
            #match = re.findall(r"\((\d+), (\d+)\) \((\d+), (\d+)\)", line)
            match = re.findall(r'(\d+) (\d+) (\d+) (\d+)', line)
            print "match is ",match
            if match:
                xmin = float(match[0][0])
                ymin = float(match[0][1])
                xmax = float(match[0][2])
                ymax = float(match[0][3])
                b = (xmin,xmax,ymin,ymax)
                im = Image.open(filepath)
                size = im.size
                bb = convert(size,b)
                h.write(str(LABEL_LIST[line_i])+" "+" ".join([str(a) for a in bb])+"\n")
                line_i += 1
                print "create new label"
        h.close()
        f.close()
g.close()




