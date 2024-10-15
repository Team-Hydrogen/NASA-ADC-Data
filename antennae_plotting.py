import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./antennacartesian.csv")


angvel = 7.2921150e-5
tilt = np.radians(23.439292)
# tilt = np.radians(0)

df2 = pd.read_csv("./hsdata.csv")
times_minutes = df2["MISSION ELAPSED TIME (mins)"].to_list()
times = [i*60 for i in times_minutes]

antenna_coords = [[[] for i in range(3)] for j in range(4)]
print(antenna_coords)

antenna_pos_dict = {"Antenna":[], "Time (sec)":[], "X":[], "Y":[], "Z":[]}

for i, antenna in enumerate(antenna_coords):
    X = df.iloc[i]["X (km)"]*np.cos(tilt) - df.iloc[i]["Z (km)"]*np.sin(tilt)
    Y = df.iloc[i]["Y (km)"]
    Z = df.iloc[i]["Z (km)"]*np.cos(tilt) + df.iloc[i]["X (km)"]*np.sin(tilt)
    for t in times:
        antenna_pos_dict["Antenna"].append(df.iloc[i]["Name"])
        antenna_pos_dict["Time (sec)"].append(t)

        antenna_pos_dict["X"].append(X * np.cos(tilt) * np.cos(angvel * t) - Y * np.sin(angvel * t) * np.cos(tilt) + Z * np.sin(tilt))
        antenna_pos_dict["Y"].append(X * np.sin(angvel * t) + Y * np.cos(angvel * t))
        antenna_pos_dict["Z"].append(-X * np.sin(tilt) * np.cos(angvel * t) + Y * np.sin(tilt) * np.sin(angvel * t) + Z * np.cos(tilt))
# print(antenna_coords)

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# for i in range(4):
#     ax.plot(df.iloc[i]["X (km)"],df.iloc[i]["Y (km)"], df.iloc[i]["Z (km)"],'ro',label=df.iloc[i]["Name"])
# for i in range(4):
#     ax.plot(antenna_coords[i][0], antenna_coords[i][1], antenna_coords[i][2], label=df.iloc[i]["Name"])

# plt.legend()
# plt.show()

df_out = pd.DataFrame(antenna_pos_dict, columns=list(antenna_pos_dict.keys()))
df_out.to_csv("antenna_plot.csv",index=False)
