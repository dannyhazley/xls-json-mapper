import pandas as pd
import uuid

def injestFile(FilePath, actionBool):
    dfRaw = pd.read_excel(FilePath)

    output = ""
    for index, row in dfRaw.iterrows():
        if actionBool:
            id = uuid.uuid4()
            output += "// {action}: \n".format(action=dfRaw.iloc[index].iloc[2])
            output += "new Action = ({id}, {description}, Map.of(\n".format(id=id, description=dfRaw.iloc[index].iloc[2])
            for x in range (3, len(dfRaw.columns)):
                if pd.notna(row.iloc[x]):
                    output += "\t\"{key}\", {value},\n".format(key=dfRaw.columns[x], value=row.iloc[x])
                x += 1
            output += "));"
            output += "\n\n//----------------------\n\n"
        else:
            output += "{enum}(\"{description}\", Map.of(\n".format(enum=dfRaw.iloc[index].iloc[0].to_string().upper(), description=dfRaw.iloc[index].iloc[1])
            output += "// {enum}: ".format(enum=dfRaw.iloc[index].iloc[0].to_string().upper())
            for x in range (2, len(dfRaw.columns)):
                if pd.notna(row[x]):
                    output += "\t\"{key}\", {value},\n".format(key=dfRaw.columns[x], value=row.iloc[x])
                x += 1
            output += ")),"
            output += "\n\n//----------------------\n\n"

    return output
