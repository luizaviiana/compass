import pandas as pd

df = pd.read_csv("concert_tours_by_women.csv") 
df = df.drop(columns=["Peak", "All Time Peak", "Ref."])

df.columns = [
    "Rank",
    "Actual gross",
    "Adjusted gross (in 2022 dollars)",
    "Artist",
    "Tour title",
    "Year(s)",
    "Shows",
    "Average gross"
]

monetary_columns = ["Actual gross", "Adjusted gross (in 2022 dollars)", "Average gross"]
for col in monetary_columns:
    df[col] = df[col].replace(r'\[.*?\]', '', regex=True)
    df[col] = df[col].replace(r'[\$,]', '', regex=True)   
    df[col] = df[col].astype(float)

text_columns = ["Artist", "Tour title"]
for col in text_columns:
    df[col] = df[col].replace(r'\[.*?\]', '', regex=True)         
    df[col] = df[col].replace(r'[†‡§]', '', regex=True)           
    df[col] = df[col].replace(r'[*:.\?!,]', '', regex=True)    
    df[col] = df[col].str.replace('&', 'and')   
    df[col] = df[col].str.replace(r'\s{2,}', ' ', regex=True)  
    df[col] = df[col].str.strip()                                  

df[["Start year", "End year"]] = df["Year(s)"].str.split('-', expand=True)
df["End year"] = df["End year"].fillna(df["Start year"])  
df = df.drop(columns=["Year(s)"])

df = df[[
    "Rank", "Actual gross", "Adjusted gross (in 2022 dollars)",
    "Artist", "Tour title", "Shows", "Average gross", "Start year", "End year"
]]

df.to_csv("csv_limpo.csv", index=False)
