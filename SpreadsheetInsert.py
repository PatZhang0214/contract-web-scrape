import pandas as pd
from MerxScrape import getAllParsedInfo
from BiddingGoScrape import scrapeAllTerms
from GlobalScrape import fetchContracts

def clearExcelFile(file_path):
    df = pd.read_excel(file_path)
    # Create a DataFrame with the same columns but no data
    empty_df = pd.DataFrame(columns=df.columns)
    # Write the empty DataFrame back to the Excel file
    empty_df.to_excel(file_path, index=False)


if __name__ == '__main__':
  spreadsheetsFile = 'information.xlsx'
  clearExcelFile(spreadsheetsFile)

  keywords = ["Drones", "UAV", "UAVs", "RPA", "RPAS", "Remotely Piloted Aircraft Systems",
                  "EVTOL", "VTOL", "Electric Fixed-wing Aircraft", "Heavy-lift Drones", "DJI",
                    "Dajiang Industries", "Mavic 3", "Matrice 350", "M3E", "M3M", "M30", "M30T",
                      "M350", "Multispectral", "Thermal", "Night Vision"]

  keywords = ["Thermal", "Drones", "Night Vision"]

  # keywords = ["Drones"]
  parsedDicts = getAllParsedInfo(keywords=keywords)
  parsedDictsBiddingGo = scrapeAllTerms(keywords=keywords)
  parsedDictsGlobal = fetchContracts(keywords=keywords)

  spreadsheet = {"Type": [], "Tender Put": [], "Links": []}
  for key in parsedDicts.keys():
      for k in parsedDicts[key].keys():
          spreadsheet["Type"].append(key)
          spreadsheet["Tender Put"].append(k)
          spreadsheet["Links"].append(parsedDicts[key][k])

  for key in parsedDictsBiddingGo.keys():
      for name in parsedDictsBiddingGo[key]:
          spreadsheet["Type"].append(key)
          spreadsheet["Tender Put"].append(name)
          spreadsheet["Links"].append("Please search via BiddingGo, remove OXOXOXOX prior to search")

  for key in parsedDictsGlobal.keys():
      for tup in parsedDictsGlobal[key]:
          spreadsheet["Type"].append(key)
          spreadsheet["Tender Put"].append(tup[1])
          spreadsheet["Links"].append(tup[0])

  df_new = pd.DataFrame(spreadsheet)


  with pd.ExcelWriter(spreadsheetsFile, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
      df_new.to_excel(writer, sheet_name='Sheet1', startrow=writer.sheets['Sheet1'].max_row, header=False, index=False)

  print("DataFrame appended successfully.")

