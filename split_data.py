import pandas as pd

df = pd.read_csv("/Users/wongshnyau/Desktop/stats1.csv")

df = df[df['wardsbought'] == 0]

df = df[df['wardsplaced'] > 0]
df = df.drop('wardsbought', axis=1)

#df.to_csv('現在的LOL.csv', encoding='utf_8_sig')
