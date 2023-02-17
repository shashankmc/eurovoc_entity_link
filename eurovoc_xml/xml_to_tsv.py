import xml.etree.ElementTree as Xet
import pandas as pd

cols = ['ID', 'EN']
rows = []

xmlparse = Xet.parse('./desc_en.xml')
root = xmlparse.getroot()
for i in root:
    rows.append({"ID": i.find("DESCRIPTEUR_ID").text, "EN": i.find("LIBELLE").text})
df = pd.DataFrame(rows, columns=cols)
df.to_csv('eurovoc.tsv', sep='\t', index=False)
