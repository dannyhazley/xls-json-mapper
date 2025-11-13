import interpreter
import output


print("---The following program is for use with a CSC2058 Group 7 Spreadsheet.---\n")


action = input("Do you want to interpret an action spreadsheet (a), or an event spreadsheet (e)?: ")
actionBool = True
while True:
    if action == "a":
        print("Please ensure your .xlsx is the following shape:")
        print("Column A: ID (Replaced with UUID4), Column B: Category, Column C: Description, Column D onwards: Effect Keys")
        print("Row A: Headings.  For Columns D onward please use the Key, Row B onwards: Values")
        actionBool = True
        break
    elif action == "e":
        print("Please ensure your .xlsx is the following shape:")
        print("Column A: Enum Name, Column B: Description, Column C onwards: Effect Keys")
        print("Row A: Headings.  For Columns C onward please use the Key, Row B onwards: Values")
        actionBool = False
        break
    else:
        action = input("Please enter \"a\" or \"e\": ")

fPath = input("Please enter the file path: ")
print("\n\n----------Outputting Maps----------\n\n\n\n\n\n")
out = interpreter.injestFile(fPath, actionBool)
output.outputToText(out, fPath, actionBool)




