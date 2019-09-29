
import pandas as pd
ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo)

ufo.to_csv(path_or_buf='./ufo_reports.csv', index=False)