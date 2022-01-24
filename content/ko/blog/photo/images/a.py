import os

for file in sorted(os.listdir()):
    if file.split('.')[-1] == 'jpg':
        print('<img src=\'images\\{}\'>'.format(file))
