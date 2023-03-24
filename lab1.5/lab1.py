import os, glob

path = 'C:\\Users\ii.azorkin\Downloads\config_files'
parsed = []
for filename in glob.glob(os.path.join(path, '*.log')):
    with open(filename) as f:
        for line in f:
            if "ip address" in line:
                pars_line = line.split()
                if len(pars_line) == 4:
                    parsed.append(line[:-1])
                    #print(line)

parsed2 = set(parsed)
print(parsed2)
