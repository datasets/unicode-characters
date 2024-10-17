import pandas as pd

header = ['Code value','Character name','General category',
          'Canonical combining classes','Bidirectional category','Character decomposition mapping',
          'Decimal digit value','Digit value','Numeric value',
          'Mirrored','Unicode 1.0 Name','10646 comment field',
          'Uppercase mapping','Lowercase mapping','Titlecase mapping']

df = pd.read_csv('http://www.unicode.org/Public/UNIDATA/UnicodeData.txt',delimiter=';')
df_modified = pd.read_csv('http://www.unicode.org/Public/UNIDATA/UnicodeData.txt',delimiter=';',names=header)


df.to_csv('archive/source.csv',index=False)

df_modified.to_csv('data/data.csv',index=False)

