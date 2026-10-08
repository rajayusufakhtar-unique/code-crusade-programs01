sent=input("enter sentence: ")
vow=["a","e","i","o","u"]
vowel=0
space=0
cons=0
digit=0
spl_char=0
for i in sent:
    if i.isdigit():
        digit+=1
    elif i in vow:
        vowel+=1
    elif i.isspace():
        space+=1
    elif i not in vow:
        cons+=1
    else:
        spl_char+=1
print(f"digit:",digit,"cons:",cons,"spl char:",spl_char,"space:",space,"vowel:",vowel)
