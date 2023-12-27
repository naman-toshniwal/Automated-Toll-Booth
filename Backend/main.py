import pandas as pd

ds = pd.read_csv("ds_rfid.csv")
df1 = pd.read_csv("final.csv")
df2 = df1["RFID Entry"]
ds1 = ds["RFID"]
dn = pd.read_csv("customer rfid.csv")
da = pd.read_csv("rto.csv")
dw = pd.read_csv("warning.csv")

#! Basic Entry of Data (Creating the DataBasee)
rf_inp = input("Enter the RFID Entry Scanned: ")
time_inp = input("Enter the time at which it has been scanned: ")
fare_inp = int(input("Input the fare: "))

df = pd.DataFrame({
    'RFID Entry': [rf_inp],
    'Time' :[time_inp],
    'Fare':[fare_inp]
          }
) # Using Fake input due to lack of hardware

#? Writing the data into final.csv which is the one accessed by the workers at toll booth
df.to_csv("final.csv", mode = 'a', index=False, header = False)

print(df1)

#? Mulitple DataFrames to used for reading and fetching the data

fetch = int(input("Press '1' to access the Car Details using RFID Tag. \nPress '2' to access the Owner Details using RFID Tag. \nPress '3' to access the RTO Name using RFID Tag. \nAny other No. to exit. \nENTER: "))

if fetch == 1:
    rfid_input = int(input("Enter the Serial Number of the RFID from the Database: "))
    a = df2[rfid_input - 1]
    print(a) 
    # if a in ds1.values:
    #     b = ds.loc[]
    b = ds.loc[ds["RFID"] == a]
    # print(b)

    # Printing the details of the car
    car_details = [b.iloc[0]["MANUFACTURER"], b.iloc[0]["MODEL"], b.iloc[0]["CAR NUMBER"], b.iloc[0]["CHASIS NUMBER"], b.iloc[0]["CITY"]] 
    for i in car_details:
        print(i)

    # l = []
    # for i in b:
    #     print(i)
    # print(l)
    # print(b["MANUFACTURER"])
    # print(f"The Details of the Car is: \nManufacturer: {b[MANUFACTURER]} \nModel: {b[MODEL]}")

elif fetch == 2:
    rfid_input = int(input("Enter the Serial Number of the RFID from the Database: "))
    c = df2[rfid_input - 1]
    print(c)
    d = dn.loc[dn["RFID NO"] == c]
    # print(d)
    # print(d.iloc[0]["Owner"]) 
    fetch2 = d.iloc[0]["Owner"]
    print(fetch2)

elif fetch == 3:
    rfid_input = int(input("Enter the Serial Number of the RFID from the Database: "))
    e = df2[rfid_input - 1]
    print(e)
    f = da.loc[da["Tag"] == e]
    # print(f.iloc[0]["RTO name"])
    fetch3 = f.iloc[0]["RTO name"]
    print(fetch3)

else:
    print("You can try this feature again")


#? Verifying the car number with the one captured from ANPR
# detected = {"detected_car": 'TN05DF3578', "time_noted": '09:45'}
# detection = None
# # print(detected["time_noted"])

# n1 = ds.loc[ds["CAR NUMBER"] == detected["detected_car"]]
# # print(n1)
# #* print(n1.iloc[0]["RFID"])

# n2 = df1.loc[df1["Time"] == detected['time_noted']]
# # print(n2)
# #* print(n2.iloc[0]["RFID Entry"])

# if n1.iloc[0]["RFID"] == n2.iloc[0]["RFID Entry"]:
#     detection = True
#     print("The car detected and RFID Tag matches")
# else: 
#     detection = False
#     print("The Car detected and RFID do not match!")
    
# #? Making use of the detection boolean
# acception = None # This variable is used to finalize that the RFID Entry is approved or not

# print(detection)
# if detection: 
#     print("The Vehicle detected and the RFID Entry matches")
#     acception = True
# else:
#     print("An Illegal/Faulty input has been detected")
#     acception = False

# print(acception)

# Making use of the acception boolean
# x1 = df1.iloc[df1["RFID Entry"] == n2["RFID Entry"]]
# print(x1)

#? Appending the finally accepted data into the final_accepted.csv
dx1 = pd.read_csv("final_accepted.csv")
# print(dx1)

#! Uncomment the code-snippet below to start appending to the final_accepted.csv

#* if acception:
#*     dx = pd.DataFrame({
#*         'RFID Entry' : [n2.iloc[0]['RFID Entry']],
#*         'Time' : [n2.iloc[0]['Time']],
#*         'Fare' : [n2.iloc[0]['Fare']]
#*     })
#*     print(dx)

#*     dx.to_csv('final_accepted.csv', mode = "a", index = False, header = False)
#*     # print("Need to check if the next line is being printed")
#*     print(dx1)
#* else:
#*     print("Incorrect inputs!")

#* print(dx)
#* print(dx1)

#? Warning tests
warning_list = []
print(dw)

dw_len = len(dw)
# print(dw_len)

for i in range(dw_len):
    # print(dw.iloc[i]["CAR NUMBER"])
    warning_list += [dw.iloc[i]["CAR NUMBER"]]

print(warning_list)

#! Change df1 back to dx1 when we use final_accepted.csv in lines: 151, 152, 158

print(df1)
data_len = len(df1)
# print(data_len)
rfid_final = []

for j in range(data_len):
    # print(dx1.iloc[i]["RFID Entry"])
    rfid_final += [df1.iloc[j]["RFID Entry"]]

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

#? This list consists the booleans for the data cross-checked in the warning list with the car numbers in the final_accepted csv
print(warned_bool) #! Warning booleans are stored in this list


#? Making use of the warned_bool
index = 0

for bools in warned_bool:
    if bools:
        print(f"The Vehicle with Car Number {car_number_final[index]} has received a penalty!")
        index += 1
    else:
        print(f"The Vehicle with Car Number {car_number_final[index]} has no warning")
        index += 1
