import os

folder_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_3_Automating_Scripts_with_Lists"

file_name = "readme.txt"

file_path = os.path.join(folder_path, file_name)

file_obj = open(file_path, 'r')

lines = (file_obj.readlines())


for line in lines:
    print("{}".format(line))