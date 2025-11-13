import os
import pandas as pd

from datetime import datetime as dt

def outputToText(output, filepath, action = True):
    type = ""
    if action:
        type = "action"
    else:
        type = "event"
    outputDir = os.path.dirname(filepath)
    utc = dt.now().strftime('%Y%m%d_%H%M%S')
    fName = "{origin}/{dateTime}_{actionTrue}_xlsConvertedToJSON.txt".format(origin = outputDir, dateTime=utc, actionTrue=type)

    with open(fName, "a") as f:
        print(output, file=f)