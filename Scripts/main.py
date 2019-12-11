import os
import glob

os.system("python convert.py")
path = 'test/*rst'
files = glob.glob(path)

def make_texList(filename):
    f = open(filename, "r", encoding="utf8")
    texList = []
    for line in f:
        texList.append(line)
    return texList

def func_replace(a, b, filename):
    with open(filename,'r+', encoding="utf8") as f:
            #convert to string:
            data = f.read()
            f.seek(0)
            f.write(data.replace(a, b))
            f.truncate()


def remove_raw_latex(filename):
    raw_latex=0
    str3 = ":raw-latex:`"
    str2 = "`"
    texlist = make_texList(filename)
    f = open(filename, "w", encoding="utf8")
    for i in range(0, len(texlist)):
        srr = ""
        if str3 in texlist[i]:
            raw_latex=1
            x=0
            while x<len(texlist[i]):
                if raw_latex==2:
                    if str2 in texlist[i][x]:
                        raw_latex=-1
                if raw_latex==-1:
                    srr+=""
                    x+=1
                    raw_latex=0
                if raw_latex==2:
                    srr+=texlist[i][x]
                    x+=1

                if x<(len(texlist[i])-12):
                    if str3 in texlist[i][x:x+12]:
                        srr+=""
                        x+=12
                        raw_latex=2
                    else:
                        srr+=texlist[i][x]
                        x+=1
        else:
            srr+=texlist[i]
             
        f.write(srr+"\n")

    f.close()




def math_environment_process(filename):
    mathen=0
    code=0
    str3 = " code-block::"
    str1 = "$"
    texlist = make_texList(filename)
    f = open(filename, "w", encoding="utf8")
    for i in range(0, len(texlist)):
        srr = ""
        if str3 in texlist[i]:
            code==1
        if code==0:
            for x in range(0, len(texlist[i])-1):
                if x==0:
                    if str1 in texlist[i][x]:
                        if mathen==-1:
                            mathen=1
                        if mathen==2:
                            mathen=0

                else:
                    if str1 in texlist[i][x]:
                        if "\\" not in texlist[i][x-1]:
                            if mathen==-1:
                                mathen=1
                            if mathen==2:
                                mathen=0

                if mathen==2:
                    srr+=texlist[i][x]
                if mathen==1:
                    srr+=":math:`"
                    mathen=2
                if mathen==-1:
                    srr+=texlist[i][x]
                if mathen==0:
                    srr+="`"
                    mathen = -1
        else:
            srr+=texlist[i]

        if i<(len(texlist)-1):
            length = len(texlist[i+1])
        if code==1:
            if texlist[i+1][0]==" ":
                code=1
            elif length==0:
                code=1
            else:
                code=0
             
        f.write(srr+"\n")

    f.close()


def make_changes(filename):
    func_replace(' code::', ' code-block::', filename)
    func_replace('ipython3', 'python3', filename)

for name in files:
    make_changes(name)
    math_environment_process(name)
    remove_raw_latex(name)
