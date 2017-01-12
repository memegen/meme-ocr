import json

wl = open("dict/linuxwords.txt","r").read().upper().split("\n")

# mock ocr functions:

# diy raw ocr from data without auto-correct
def ocr0(path):
    import parse
    parse.path = path
    fi = open("data/"+path.split("/")[-1].split(".")[0]+".json","r")
    js = json.loads(fi.read())
    parse.bds = js[0]
    parse.ccr = js[1]
    return parse.guesscaption(simple=True)

# diy ocr from scratch
def ocr(path):
    import memeocr as mo
    import parse
    parse.bds, parse.ccr = mo.rawocr(path)
    return parse.guesscaption()

# diy ocr from data
def ocr1(path):
    import parse
    parse.path = path
    fi = open("data/"+path.split("/")[-1].split(".")[0]+".json","r")
    js = json.loads(fi.read())
    parse.bds = js[0]
    parse.ccr = js[1]
    return parse.guesscaption()

# mock tesserect result
def ocr2(path):
    return "YO BAWC I HEAR YOU CAN'T USE WIKIDEMIA AS A SOURCE SC | SOURCE THE SOURCES INSIDE OF WIRETAPPER'S SOURCES"


# evaluate the quality of an ocr result
def evalresult(t):
    puncs = ".,!?"
    t = t.replace("\n"," ")
    for p in puncs:
        t = t.replace(p," "+p)
    t = t.split(" ")
    score = 0.0
    for i in range(0,len(t)):
        if t[i] in wl:
            score += 1.0
    print score/len(t)
    return score/len(t)

# sort a list of ocr functions by their quality
def ocrcomp(path,*args):
    results = []
    for f in args:
        results.append((f,f(path)))
    return sorted(results, key = lambda x: evalresult(x[1]), reverse = True)

if __name__ == "__main__":
    #print ocr1("images/img11.jpg")

    print ocrcomp("images/img6.jpg",ocr0,ocr2)

