import pandas as pds

df = pds.read_excel("contacts.xlsx", sheet_name=None, usecols="A,K")

full_list = df.get("100-contacts")

emails = full_list['email'].unique()

print(emails)
