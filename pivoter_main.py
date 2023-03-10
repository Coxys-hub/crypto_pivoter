#crypto csv pivot

import pandas as pd

cryptocsv = pd.read_csv("cryptos-jan23.csv", names=["ticker", "count", "date"])

cryptocsv["ticker"] = cryptocsv["ticker"].str.replace('\W', '', regex=True) #strip BS chars from ticker colum
table = pd.pivot_table(cryptocsv, index='date', columns=['ticker'], values='count') #transform tickers from column to row with date as index

#table.insert(0, 'TEST', '')
print(table)


#3 day expoential moving average accross time series \n
# but need to sort the column problem of 'count' as each column header
#table = table.assign(ewm_3day = table['count'].ewm(span=3, adjust=False).mean())

# ask if user wants to dump contents of dataframe to CSV
def export_control():
    asktosave = input("Do you want to dump the above to csv? Y/N ")

    if asktosave.lower() == "y":
        table.to_csv("./csvdump.csv")
        print("dumped to csv")
    else:
        print("DID NOT DUMP TO CSV")

export_control()



