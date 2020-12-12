from os import listdir, rename
from os.path import isfile, join

for f in listdir('./'):
    if isfile(join('./', f)) and not f.endswith('.py') and not f.endswith('.cpp'):
        rename(f, f + '.py')