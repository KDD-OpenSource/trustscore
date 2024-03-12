#Simple questionary programm, calculating and saving the trust score

import numpy as np

import os
import json

from questions import questions, subtasks


def meaning_string():
    print("""| Occurrence (O)  | Significance (S)       | Detection (D)     |
|-----------------|------------------------|-------------------|
| Impossible (10) | Negligible (10)        | Certain (10)      |
| Unlikely (9)    | Barely perceptible (9) | High (9)          |
| Very low (7-8)  | Insignificant (7-8)    | Moderate (7-8)    |
| Low (4-6)       | Moderate (4-6)         | Low (4-6)         |
| Moderate (2-3)  | Severe (2-3)           | Very low (2-3)    |
| High (1)        | Extremely severe (1)   | Unlikely (1)      |
| Certain (0)     | Unacceptable (0)       | Impossible (0)    |""")




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
    meaning_string()
    print("Evaluating the problem: ", prob)
    O=read_number("Occurrence (O) [0 inexcusable, 1 bad, 9 good, 10 everything ok]: ")
    S=read_number("Significance (S) [0 inexcusable, 1 bad, 9 good, 10 everything ok]: ")
    D=read_number("Detection Probability (D) [0 inexcusable, 1 bad, 9 good, 10 everything ok]: ")
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
    vals=[dic["O"],dic["S"],dic["D"]]
    if 0 in vals:return 0
    if 10 in vals:return 10
    return (dic["O"]*dic["S"]*dic["D"])**(1/3)

def subscore(dics):
    return np.mean([subsubscore(dic) for dic in dics])

def weightmod(w):
    w=np.array(w)
    w=0.1+w/(2*np.sum(w))
    return w

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
    dics=[]
    ev=1.0
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
    print(f"The questions for {info['task']} are")
    for dic in info["dics"]:
        print(dic["question"])
    info["ori_weight"]=read_positive_number(f"Please enter the weight for the task {info['task']}: ")

weights=[info["ori_weight"] for info in infos]
weights=weightmod(weights)
for info,weight in zip(infos,weights):
    info["weight"]=weight

print("Thank you for your input. I will now calculate your trust score")
result=score(infos)
print(f"Your trust score is {result}")

if boolean("Do you want to save this result?", "y"):
    fn=f"results/score_{job}_{who}.json"

    if os.path.exists(fn):
        if not boolean(f"The file {fn} already exists. Do you want to overwrite it?","y"):
            print("Aborting.")
            exit()

    with open(fn, "w") as f:
        json.dump({"job":job,"who":who,"infos":infos, "result":result}, f, indent=2)
    print(f"Saved the result to {fn}")













