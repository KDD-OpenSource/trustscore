#Simple questionary programm, calculating and saving the trust score

import numpy as np

import os
import json

from questions import questions, subtasks

def read_number(prompt):
    while True:
        try:
            ret=float(input(prompt))
            if ret<0 or ret>10:
                print("Please enter a number between 0 and 10")
            else:
                return ret
        except ValueError:
            print("Invalid input. Please enter a number.")

def read_int(prompt,minv=0,maxv=10):
    while True:
        try:
            ret=(input(prompt))
            if len(ret.strip())==0:
                return minv
            ret=int(ret)
            if ret<minv or ret>maxv:
                print(f"Please enter a number between {minv} and {maxv}")
            else:
                return ret
        except ValueError:
            print("Invalid input. Please enter a number.")

def read_positive_number(prompt):
    while True:
        try:
            ret=float(input(prompt))
            if ret<0:
                print("Please enter a positive number.")
            else:
                return ret
        except ValueError:
            print("Invalid input. Please enter a number.")


def fmea(prob):
    print("Evaluating the problem: ", prob)
    O=read_number("Occurrence (O) [1 bad, 10 good]: ")
    S=read_number("Significance (S) [1 bad, 10 good]: ")
    D=read_number("Detection Probability (D) [1 bad, 10 good]: ")
    return {"O":O, "S":S, "D":D}

def boolean(prompt,exp=""):
    while True:
        ret=input(prompt+ (f"[{exp}]" if exp else ""))
        if len(ret.strip())==0:
            ret=exp
        if ret.lower() in ["y", "yes"]:
            return True
        if ret.lower() in ["n", "no"]:
            return False
        print("Invalid input. Please enter yes or no.")

def chooseOne(prompt, options):
    print(prompt)
    print("Your options are:")
    for i, option in enumerate(options):
        print(f"{i+1}: {option}")
    selection=read_int("Please enter the number of your selection: ",1,len(options))
    return selection-1

def chooseMany(prompt, options, maxcou=3):
    first=chooseOne(prompt, options)
    ret=[first]
    while boolean("Do you want to add another option?","n"):
        nex=chooseOne(prompt, options)
        ret.append(nex)
        if len(ret)>=maxcou:
            print("Maximum number of options reached.")
            break
    return ret

def subsubscore(dic):
    return (dic["O"]*dic["S"]*dic["D"])**(1/3)

def subscore(dics):
    return np.mean([subsubscore(dic) for dic in dics])

def weightmod(weights):
    weigths=np.array(weights)
    weigths=0.1+weigths/(2*np.sum(weigths))
    return weights

def score(infs):
    for inf in infs:
        if inf["score"]==0 and inf["weight"]>0:
            return 0.0
    return np.mean([inf["score"]*inf["weight"] for inf in infs])/np.mean([inf["weight"] for inf in infs])


job=input("Please enter which object you are evaluating: ")
who=input("Please enter your name: ")

print(f"We will go through {len(subtasks)} subtasks and score them, then I will calculate a trust score for you")

infos=[]


for taski,task in enumerate(subtasks):
    while True:
        print(f"Subtask {taski+1}/{len(subtasks)}: {task}")
        todoo=chooseMany("Please select the problems you want to evaluate", questions[taski])
        dics=[]
        for todo in todoo:
            dic=fmea(questions[taski][todo])
            dic={"todo":todo, "question":questions[taski][todo], **dic}
            dics.append(dic)
    
        ev=subscore(dics)
        print(f"The score for the subtask '{task}' is {ev}")
        if boolean("Are you happy with this?","y"):
            break

    toadd={"taski":taski, "task":task, "dics":dics, "score":ev}
    infos.append(toadd)


    print()

print("Thank you for your input so far. We will now require weights for each task. They will automatically be normalized")
for info in infos:
    info["ori_weight"]=read_positive_number(f"Please enter the weight for the task {info['task']}: ")

weights=[info["ori_weight"] for info in infos]
weights=weightmod(weights)
for info,weight in zip(infos,weights):
    info["weight"]=weight

print("Thank you for your input. I will now calculate your trust score")
result=score(infos)
print(f"Your trust score is {result}")

if boolean("Do you want to save this result?", "y"):
    fn=f"score_{job}_{who}.json"

    if os.path.exists(fn):
        if not boolean(f"The file {fn} already exists. Do you want to overwrite it?","y"):
            print("Aborting.")
            exit()

    with open(fn, "w") as f:
        json.dump({"job":job,"who":who,"infos":infos, "result":result}, f, indent=2)
    print(f"Saved the result to {fn}")













