import interpreter


print("---The following program is for use with a CSC2058 Group 7 Spreadsheet.---\n")
print("Please ensure your .xlsx is the following shape:")
print("Column A: ID (Replaced with UUID4), Column B: Category, Column C: Description, Column D onwards: Effect Keys")
print("Row A: Headings.  For Columns D onward please use the Key, Row B onwards: Values")

fPath = input("Please enter the file path: ")
print("\n\n----------Outputting Maps----------\n\n\n\n\n\n")
interpreter.injestFile(fPath)

