import pandas as pd


df = pd.read_csv("D:\ginga\Documents\Gustavo\WebScraping_VivaReal\WebScraping_VivaReal\Ceps.csv")


df.to_excel("ceps.xlsx",index=False)