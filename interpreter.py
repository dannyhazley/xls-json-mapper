import pandas as pd
import uuid

def injestFile(FilePath, actionBool):
    dfRaw = pd.read_excel(FilePath)

    #id = uuid.uuid4()
    id = 0
    output = ""
    for index, row in dfRaw.iterrows():
        id += 1
        if actionBool:
            output += "// {action}: \n".format(action=dfRaw.iloc[index].iloc[2])
            output += "TempList.add(new Action({id}, \"{description}\", Map.ofEntries(\n".format(id=id, description=dfRaw.iloc[index].iloc[2])
            lines = []
            for x in range(3, len(dfRaw.columns)):
                if pd.notna(row.iloc[x]):
                    val = row.iloc[x]
                    val = int(val) if isinstance(val, float) and val.is_integer() else val

                    lines.append("\tMap.entry(\"{key}\", {value})".format(
                        key=dfRaw.columns[x],
                        value=val
                    ))
            output += ",\n".join(lines) + "\n"
            output += ")));"
            output += "\n\n//----------------------\n\n"
        else:
            output += "// {enum}: \n".format(enum=dfRaw.iloc[index].iloc[0].upper())
            output += "{enum}(\"{description}\", Map.of(\n".format(enum=dfRaw.iloc[index].iloc[0].upper().replace(" ", "_"), description=dfRaw.iloc[index].iloc[1])
            for x in range (2, len(dfRaw.columns)):
                if pd.notna(row.iloc[x]):
                    output += "\t\"{key}\", {value},\n".format(key=dfRaw.columns[x], value=row.iloc[x])
                x += 1
            output += ")),"
            output += "\n\n//----------------------\n\n"

    return output
