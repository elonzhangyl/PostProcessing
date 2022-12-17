import shutil
import os

base_dir = r'D:\Projects\10097 Huadong floating\20221207 4thLoop'
dst_file = base_dir + r'\4. DLC1.2 - RigidBlade - A16 - 8deg2'
if os.path.isdir(dst_file):
    print('The folder exists')# Check if the folder has existed
else:
    os.makedirs(dst_file)
    for i in range(6,1656,6):
        src_file = base_dir + r'\4. DLC1.2 - RigidBlade - A16\DLC1.6-'+str(i)+'.dat'
        dst_file_full = dst_file + r'\DLC1.6-'+str(i)+'.dat'
        shutil.copyfile(src_file, dst_file_full)

