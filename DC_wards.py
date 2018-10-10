import pandas as pd

df = pd.read_csv('~/Dropbox/現在的LOL.csv')

dfp = df[df['wardsplaced'] <= 25]


dfpp = df[df['pinksbought'] <= 15]
