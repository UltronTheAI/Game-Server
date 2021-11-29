import glob
import os

folders = os.listdir()
# files = glob.glob('*.js')
# print(folders)
# print(files)
for i in folders:
    if '.' not in i:
        files = glob.glob(i + '/*.js')
        for i2 in files:
            if '.js' in i2:
                f = open(i2, 'r')
                fr = f.read()
                f.close()
                if 'localhost:3000' in fr:
                    print('Localhost IN ' + i2)