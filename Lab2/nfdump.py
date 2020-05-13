import os

nfdump = "nfdump -r nfcapd.202002251200 'dst ip 217.15.20.194 or src ip 217.15.20.194' -o csv -O tstart > data_internet.csv"
os.system(nfdump)