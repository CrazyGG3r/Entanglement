import random as r

titlelsit = ["Sir please marks dedein",
             "1/0 = infinity",
             "Entanglement",
             "Cats are so sweet",
             "My roll number is unique",
             "Mothers deserve all the Happiness",
             "177063",
             "r/ligma",
             "TINGA TINGA TINGA TINGA TINGA",
             "[Enter text here]"
             ,"Shaheer Ul Islam",
             "East Aand West SUNNI are the best",
             "Patch 7.69a: Removed Techies",
             "Abdul rehman",
             "Maaz Muhammad Khan"]

fontlist = ["font\\f1.ttf",
            "font\\f2.ttf",
            "font\\f3.ttf",
            "font\\f4.ttf",
            "font\\f5.ttf",
            "font\\f6.ttf",
            "font\\f7.ttf",
            "font\\f8.ttf",
            "font\\f9.ttf",
            "font\\f10.ttf"
            ]

def titleselect():
   x = r.randint(0,13)
   return titlelsit[x]

def fontselect():
    x = r.randint(0,9)
    return fontlist[x]
    



