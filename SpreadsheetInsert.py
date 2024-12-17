import pandas as pd
from MerxScrape import getAllParsedInfo

spreadsheetsFile = 'information.xlsx'

keywords = ["Drones", "UAV", "UAVs", "RPA", "RPAS", "Remotely Piloted Aircraft Systems",
                "EVTOL", "VTOL", "Electric Fixed-wing Aircraft", "Heavy-lift Drones", "DJI",
                  "Dajiang Industries", "Mavic 3", "Matrice 350", "M3E", "M3M", "M30", "M30T",
                    "M350", "Multispectral", "Thermal", "Night Vision"]

# keywords = ["Drones"]
parsedDicts = getAllParsedInfo(keywords=keywords)

spreadsheet = {"Type": [], "Tender Put": [], "Links": []}
for key in parsedDicts.keys():
    for k in parsedDicts[key].keys():
        spreadsheet["Type"].append(key)
        spreadsheet["Tender Put"].append(k)
        spreadsheet["Links"].append(parsedDicts[key][k])

df_new = pd.DataFrame(spreadsheet)

with pd.ExcelWriter(spreadsheetsFile, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
    df_new.to_excel(writer, sheet_name='Sheet1', startrow=writer.sheets['Sheet1'].max_row, header=False, index=False)

print("DataFrame appended successfully.")


