import os, glob

path = 'C:\\Users\ii.azorkin\Downloads\config_files'
for filename in glob.glob(os.path.join(path, '*.log')):
    with open(filename) as f:
        for line in f:
            if "ip address" in line:
                print(line)