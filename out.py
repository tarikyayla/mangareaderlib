import json
import main
import os
import mangareader as mr 
array = main.mangaUpdatesFromEpikManga()
def saveAsJSON(objectArray):
    with open("jsonfile.json","w+") as writer:
        writer.write("[")
        for x,manga in enumerate(objectArray):
            writer.write(json.dumps(manga.__dict__,indent=4,ensure_ascii=False))
            if(x != len(objectArray)-1):writer.write(",")
        writer.write("]")

saveAsJSON(array)

    




