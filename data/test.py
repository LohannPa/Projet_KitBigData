import csv
# with open ('C:/Users/leeby/OneDrive/Bureau/KitBigData/data/data_taches.csv', 'r', newline = '') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for i, row in enumerate(csv_reader):
#         idx = i
#         print(i, row)
rows = []
with open ('C:/Users/leeby/OneDrive/Bureau/KitBigData/data/data_taches copy.csv', 'r', newline = '') as csv_file:
    csv_reader = csv.reader(csv_file)
    # print(csv_reader)
    for row in csv_reader:
        if row[0] == 'Tache5':
            row[2] = 'True'
            rows.append(row)
        else:
            rows.append(row)
        # print(rows)

with open ('C:/Users/leeby/OneDrive/Bureau/KitBigData/data/data_taches copy.csv', 'w', newline = '') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(rows)

# print(csv_writer[idx])