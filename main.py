import csv
import glob
import os.path
import random

if __name__ == '__main__':
    # for the players table
    f = "C:\\Users\\itama\\Desktop\\csv_for_db\\atp_players_filtered.csv"
    with open(f, mode="r") as old_file:
        reader_obj = csv.reader(old_file)  # read the current csv file

        with open(os.path.dirname(f)+"\\fillter_"+os.path.basename(f), mode="w", newline='') as new_file:
            writer_obj = csv.writer(new_file)  # Writes to the new CSV file
            for data in reader_obj:
                # if the height is misssing
                if data[6] == "":
                    data[6] = str(random.randint(160, 200))
                    # take only the columns we need
                writer_obj.writerow((data[0], data[1], data[2], data[3], data[4], data[5], data[6]))

# if __name__ == '__main__':
#     # for the matches table
#     path = "C:\\Users\\itama\\Desktop\\csv_for_db\\tennis_apt_master\\*.csv"
#     for f in glob.glob(path):
#         print(os.path.dirname(f)+"\\fillter_"+os.path.basename(f))
#
#         with open(f, mode="r") as old_file:
#             reader_obj = csv.reader(old_file)  # read the current csv file
#
#             with open(os.path.dirname(f)+"\\fillter_"+os.path.basename(f), mode="w", newline='') as new_file:
#                 writer_obj = csv.writer(new_file)  # Writes to the new CSV file
#                 for data in reader_obj:
#                     writer_obj.writerow((data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
