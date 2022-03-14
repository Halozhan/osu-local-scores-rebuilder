import os

path = "F:/osu!/Replays"
path2 = "F:/osu!/Data/r"
file_list = os.listdir(path)
file_list2 = os.listdir(path2)

# print("file_list: {}".format(file_list))

print(len(file_list))
print(len(file_list2))

for file in file_list:
    if ".osr" in file:
        # print(file, end=" ")
        os.startfile(path+"/"+file)
    
for file in file_list2:
    if ".osr" in file:
        # print(file, end=" ")
        os.startfile(path2+"/"+file)