import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    noun=w.title()
    upp=w.upper()
    data_key=data.keys()
    if w in data:    #to find match of word in lower from data
        return data[w]
    elif noun in data:  #to find match of noun from data
       return data[w.title()]
    elif upp in data:  #to find match of definoitation of acronyms from data
       return data[w.upper()]
    else:
        close_match=get_close_matches(w,data.keys().lower(),n=10,cutoff=0.8) #to find close match to word
        l=len(close_match)
        print(w)

        if l>0: #to show close matches to entered words.
            print("Did you mean one among following:")
            for i in range(len(close_match)):
                print(i+1,':',close_match[i])
#to get serial number of correct word from the list of close matching words
            ch_no=0
            while(ch_no==0): # to get correct choice from user
                choice=input("if yes enter Y  else enter N:\n ")
                if choice.upper()=='Y':
                    c_len=l+1
                    wh=1 #to get correct serial number from user which is within the limit
                    while(wh==1):
                        corr=int(input("enter serial number of correct word:"))
                        if corr not in range(c_len) or corr==0:
                            print("It seems that you have entered wrong serial number please enter correct serial number..:")

                        else:
                            return data[close_match[corr-1]]
                            wh=0
                    ch_no=1
                elif choice.upper()=='N':
                     return "It seems that you have entered completely wrong word\nplease recheak this word and visit again.."
                     ch_no=1
                else:
                    print("wrong choice.")

        else:
            return "you have entered completely wrong word\nplease recheak this word and visit again.."
word=input("enter word:")
op=(translate(word))

if type(op)==list:
    for item in op:
        print(item)
else:
    print(op)
