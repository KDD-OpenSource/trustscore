import os
import glob
import json

files=glob.glob("backup_results/*.json")

rename={}

def do_one(fn):
    with open(fn, "r") as f:
        data=json.load(f)
    job, who=data["job"], data["who"]
    who=who.lower()
    if not (who in rename):
        rename[who]=len(list(rename.keys()))
    who=rename[who]
    data["who"]=who
    fn2=f"results/score_{job}_{who}.json"
    with open(fn2, "w") as f:
        json.dump(data, f, indent=2)
    #os.remove(fn)

for fn in files:
    do_one(fn)

print(rename)

