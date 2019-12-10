import os
import glob

path = 'test/*ipynb'
files = glob.glob(path)

for name in files:
    os.system("jupyter nbconvert --to rst from "+name)
    #os.system("jupyter nbconvert --to rst from "+name+" --stdout --template rst_template.tpl)