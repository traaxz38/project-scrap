import pandas as pd
import numpy as np
import re

data = pd.read_csv('operations.csv')
print(data)

VALID_CATEG = ['AUTRE', 'TRANSPORT', 'FACTURE TELEPHONE', 'COURSES', 'COTISATION BANCAIRE'
                  , 'RESTAURANT','LOYER']
mask = ~data['categ'].isin(VALID_CATEG)
data.loc[mask, 'categ'] = 'AUTRE'


data['montant'] = pd.to_numeric(data['montant'], errors='coerce')
data.loc[data['montant'].isnull(), 'montant'] = data['montant'].mean()

data.drop_duplicates(subset=['date_operation', 'libelle', 'montant', 'solde_avt_ope'], inplace=True, ignore_index=True)
print(data.loc[data[['date_operation', 'libelle', 'montant', 'solde_avt_ope']].duplicated(keep=False),:])
a = data.loc[data['montant']==-15000,:].index[0] # récupération de l'index de la transaction à -15000

data.iloc[a-1:a+2,:] # on regarde la transaction précédente et la suivante
data.loc[data['montant']==-15000, 'montant'] = -14.39
print(data.isnull().sum())
