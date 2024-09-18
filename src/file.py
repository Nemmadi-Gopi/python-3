import csv
import os
import pandas as pd


path = r"C:\Users\nemma\Desktop\ab.csv"
# print(os.path.isfile(path))

with open(path, 'r') as file:
    csvreader =csv.reader(file)
    csvheader = next(csvreader)
    csvheader.append("Test_Result")
    rows = list(csvreader)


    for row in rows:
        row.append("TRUE")
    with open(r"C:\Users\nemma\Desktop\abc.csv", 'w', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(rows)


        # if row[0] and row[1]:
        #     data = {
        #         'Name': [row[0]], 'Riskrating':[row[1]]
        #     }
        #     df = pd.DataFrame(data)
        #     row[2] = "TRUE"
        #     print(row[2])
            # with open(path, 'a') as file1:
            #     writer = csv.writer(file1)
            #     writer.writerow([row[2]])
            #     file1.close()
        #     # row[2] = Ouput_validation()
        #     # data1 = {
        #     #     row[2]: row
        #     # }

        #     writer.writerows({"test_result": ["hello"]})
        # file1.close()
        #     y = []
        #     y.append[True or False]
        #     writer.writerow([row[2]+y])

        
#--------------------------------------------

# path = r"C:\Users\nemma\Desktop\ab.csv"
# print(os.path.isfile(path))

# with open(path, 'r') as file:
#     csvreader =csv.reader(file)
#     csvheader = next(csvreader)
#     for row in csvreader:
#         print(row)

#         if row[0] and row[1]:
#             data = {
#                 'Name': [row[0]], 'Riskrating':[row[1]]
#             }
#             df = pd.DataFrame(data)
#             row[2] = "TRUE"
#             print(row[2])
#             # with open(path, 'a') as file1:
#             #     writer = csv.writer(file1)
#             #     writer.writerow([row[2]])
#             #     file1.close()
#         #     # row[2] = Ouput_validation()
#         #     # data1 = {
#         #     #     row[2]: row
#         #     # }

#         #     writer.writerows({"test_result": ["hello"]})
#         # file1.close()
#         #     y = []
#         #     y.append[True or False]
#         #     writer.writerow([row[2]+y])
print("hello")
        