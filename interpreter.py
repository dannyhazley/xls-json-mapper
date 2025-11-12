import pandas as pd
import uuid

def injestFile(FilePath, actionBool):
    dfRaw = pd.read_excel(FilePath)

    for index, row in dfRaw.iterrows():
        if actionBool:
            id = uuid.uuid4()
            code = "new Action = ({id}, {description}, Map.of(\n".format(id=id, description=dfRaw.iloc[index].iloc[2])
            print("// {action}: ".format(action=dfRaw.iloc[index].iloc[2]))
            for x in range (3, len(dfRaw.columns)):
                if pd.notna(row[x]):
                    code += "\t\"{key}\", {value},\n".format(key=dfRaw.columns[x], value=row.iloc[x])
                x += 1
            code += "));"
            print(code)
            print("\n\n//----------------------\n\n")
        else:
            code = "{enum}(\"{description}\", Map.of(\n".format(enum=dfRaw.iloc[index].iloc[0].to_string().upper(), description=dfRaw.iloc[index].iloc[1])
            print("// {enum}: ".format(enum=dfRaw.iloc[index].iloc[0].to_string().upper()))
            for x in range (2, len(dfRaw.columns)):
                if pd.notna(row[x]):
                    code += "\t\"{key}\", {value},\n".format(key=dfRaw.columns[x], value=row.iloc[x])
                x += 1
            code += ")),"
            print(code)

