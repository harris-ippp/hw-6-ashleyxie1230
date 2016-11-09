
import pandas as pd
import matplotlib.pyplot as plt

dataframe = []
for i in range(1924,2013):
    if not i%4:
        csv_file = str(i) +".csv"
        header = pd.read_csv(csv_file, nrows = 1).dropna(axis = 1)
        d = header.iloc[0].to_dict()
        df = pd.read_csv(csv_file, index_col = 0,
            thousands = ",", skiprows = [1])
        df.rename(inplace = True, columns = d)
        df.dropna(inplace = True, axis = 1)
        df["Year"] = i
        dataframe.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])

DF = pd.concat(dataframe)
DF["Republican Share"] = DF["Republican"]/DF["Total Votes Cast"]
# Save the plot as png.
DF.loc[["Accomack County"]].plot(kind = "line", x = "Year", y = "Republican Share")
plt.savefig("accomack.png")