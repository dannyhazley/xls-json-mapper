import pandas as pd
import uuid

def injestFile(FilePath):
    dfRaw = pd.read_excel(FilePath)

    for index, row in dfRaw.iterrows():
        id = uuid.uuid4()
        code = "new Action = ({id}, {description}, Map.of(\n".format(id=id, description=dfRaw.iloc[index][2])
        print("// {action}: ".format(action=dfRaw.iloc[index, 2]))
        for x in range (3, len(dfRaw.columns)):
            if pd.notna(row[x]):
                code += "\t\"{key}\", {value},\n".format(key=dfRaw.columns[x], value=row[x])
            x += 1
        code += "));"
        print(code)
        print("\n\n//----------------------\n\n")

