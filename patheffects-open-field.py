import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.patheffects import withStroke
path = '/Users/DDDDDDDDDDDDDDDDD/'
# read all csv files
dfs = []
for file in os.listdir(path):
    if file.endswith('.csv'):
        df1 = pd.read_csv(path+file)
        df1 = df1.iloc[::1, :]
        df1 = df1.query("ROI_location != 'non_roi'")
        df1 = df1.drop(df1.index[np.where(df1.index > 8999)])
        df1['Distance_cm'] = df1['Distance_cm'].cumsum()
        if df1['X'].max() >= 600:
           continue
        dfs.append(df1)
# concatenate all dataframes 
df = pd.concat(dfs, axis=1).fillna(0)
# create new columns with shifted values
X = df['X']
Y = df['Y']
Z = df['Distance_cm']
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=5, cstride=3,
                       linewidth=0, antialiased=False)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('ROI_TT_S')
plt.savefig("FIGURE.png", dpi=300)
plt.show()
