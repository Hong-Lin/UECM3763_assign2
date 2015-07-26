from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

start = dt(2011, 1, 1)
end = dt(2015, 5, 1)
df = DR("1295.KL", 'yahoo', start, end)
dw = DR("^KLSE", 'yahoo', start, end)

df['5D_MA'] = pd.rolling_mean(df['Close'],5)         # calculate moving average
dw['5D_MA'] = pd.rolling_mean(dw['Close'],5)

#start plotting
plt.subplot(2,1,1)
plt.plot(df.index,df['5D_MA'],'r',label='Public Bank 5-day MA')
plt.xlabel('Years')
plt.ylabel('5-day MA')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=4, mode="expand", borderaxespad=0.)
plt.subplot(2,1,2)
plt.plot(dw.index,dw['5D_MA'],'b',label='KLSE 5-day MA')
plt.xlabel('Years')
plt.ylabel('5-day MA')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=4, mode="expand", borderaxespad=0.)        
plt.show()

df = df.reset_index()
dw = dw.reset_index()
mm = pd.merge(df, dw, on='Date', suffixes=['_pbb', '_KLSE'])   # merge dataframe
a = np.corrcoef(mm['Close_pbb'],mm['Close_KLSE'])              # calculate correlation coefficient
print ('Correlation coefficient=', a)

