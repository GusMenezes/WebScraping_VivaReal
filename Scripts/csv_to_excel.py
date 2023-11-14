import pandas as pd


df = pd.read_csv(r"D:\ginga\Documents\Gustavo\WebScraping_VivaReal\WebScraping_VivaReal\Exel_and_Csv_Files\LISTA_URLS_VIVAREAL.csv")


df.to_excel("ceps.xlsx",index=False)