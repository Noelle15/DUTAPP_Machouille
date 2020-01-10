import pandas as pd

produits = pd.read_csv('./FichierProduits.csv', sep=';', encoding='ISO-8859-1')
paniers = pd.read_csv('./FichierPanier.csv', sep=';', encoding='ISO-8859-1')

print(produits.to_json(r'products.json', orient='records'))
print(paniers.to_json(r'cart.json', orient='records'))
