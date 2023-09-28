import arcpy
import os
arcpy.env.workspace = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_3_Automating_Scripts_with_Lists\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists.gdb"

# Output folder path is where the txt file will get created
output_folder_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_3_Automating_Scripts_with_Lists"
# Output file name
output_text_file = "MajorAttractions_info.txt"

output_file_path = os.path.join(output_folder_path, output_text_file)
print(output_file_path)

file_obj = open(output_file_path, "w")
print("Field properties of Major Attractions are")
file_obj.write("Field properties of Major Attractions are \n")
print("--------------------------------------------")

# Listing fields and looping through fields
field_list = arcpy.ListFields("MajorAttractions")
for field in field_list:
    print("Field Name: {}, Type: {}, Length: {}".format(field.name, field.type, field.length))
    file_obj.write("Name: {}, Type: {}, Length: {} \n".format(field.name, field.type, field.length))

    print("------------------------------------------")
    file_obj.write("---------------------------------------------\n")

file_obj.close()
print("Process Completed")







