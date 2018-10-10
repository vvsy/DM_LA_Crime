import pandas as pd

dfp = pd.read_csv('~/Dropbox/現在的LOL.csv')

dfp0 = dfp[dfp['win'] == 0]

dfp1 = dfp[dfp['win'] == 1]

print(dfp0.shape)
print(dfp1.shape)
