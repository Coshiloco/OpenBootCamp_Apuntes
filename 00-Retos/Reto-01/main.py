import pandas as pds
import pprint

from pandas import DataFrame

dfs = pds.read_excel("contacts.xlsx", sheet_name=None, usecols="A,K")

dataframe = dfs.get("100-contacts")  # type: DataFrame

nombre = input("Introduce el nombre a buscar:")

resultado = dataframe[dataframe.first_name == nombre]

print(resultado.email)
