from subprocess import run
from sys import argv
from os import walk
from glob import glob

# node dmetool.js obj assets/Armor_TR_Male_HeavyAssault_Look001_Lod0.dme
# print(argv[1:])
dme_files = glob(argv[1] + '/*LOD0.dme')

print(dme_files)
for x in dme_files:
	run(['node', 'dmetool.js', "obj", x])
