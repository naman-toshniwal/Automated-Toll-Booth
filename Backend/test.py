import pandas as pd

ds = pd.read_csv("ds_rfid.csv")
df1 = pd.read_csv("final.csv")
df2 = df1["RFID Entry"]
ds1 = ds["RFID"]
# print(ds1)
dn = pd.read_csv("customer rfid.csv")
da = pd.read_csv("rto.csv")
dx1 = pd.read_csv("final_accepted.csv")
dw = pd.read_csv("warning.csv")

# detected = {"detected_car": 'TN05DF3578', "time_noted": '09:45'}
# detection = None
# print(detected["time_noted"])

# n1 = ds.loc[ds["CAR NUMBER"] == detected["detected_car"]]
# # print(n1)
# print(n1.iloc[0]["RFID"])

# n2 = df1.loc[df1["Time"] == detected['time_noted']]
# # print(n2)
# print(n2.iloc[0]["RFID Entry"])

# if (n1.iloc[0]["RFID"] ==  n2.iloc[0]["RFID Entry"]):
#     print("Test check")

# Warning tests
warning_list = []
print(dw)

dw_len = len(dw)
# print(dw_len)

for i in range(dw_len):
    # print(dw.iloc[i]["CAR NUMBER"])
    warning_list += [dw.iloc[i]["CAR NUMBER"]]

print(warning_list)

data_len = len(dx1)
# print(data_len)
rfid_final = []

for j in range(data_len):
    # print(dx1.iloc[i]["RFID Entry"])
    rfid_final += [dx1.iloc[j]["RFID Entry"]]

print(rfid_final)

car_number_final = []

for i in rfid_final:
    f1 = ds.loc[ds["RFID"] == i]
    # print(f1.iloc[0]["CAR NUMBER"])
    car_number_final += [f1.iloc[0]["CAR NUMBER"]]

print(car_number_final)

warned_bool = []

for k in car_number_final:
    if k in warning_list:
        print("Vehicle Detected from the warning list!")
        print(f"The Vehicle with Car Number {k}")
        warned_bool += [True]
    else:
        warned_bool += [False]

print(warned_bool)

# Making use of the warned_bool
index = 0

for bools in warned_bool:
    if bools:
        print(f"The Vehicle with Car Number {car_number_final[index]} has received a penalty!")
        index += 1
    else:
        print(f"The Vehicle with Car Number {car_number_final[index]} has no warning")
        index += 1
        


