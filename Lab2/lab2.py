import csv

IP = '217.15.20.194'

pack_src_bytes = 0
pack_dst_bytes = 0

with open ('data_internet.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		if row['sa'] == IP:
			pack_src_bytes = pack_src_bytes + int(row['ibyt']) + int(row['obyt'])
		if row['da'] == IP:
			pack_dst_bytes = pack_dst_bytes + int(row['ibyt']) + int(row['obyt'])
f.close()


pack_kbytes = pack_src_bytes + pack_dst_bytes

price_per_mbyte = 1.0
free_kbytes = 1000

def internet(amount, price):
	return amount*price

pack_cost = internet(((pack_kbytes-free_kbytes+999999)//1000000), price_per_mbyte)

print(f'Data sent: {pack_src_bytes/1000} MB')
print(f'Data received: {pack_dst_bytes/1000000} MB')
print(f'Internet cost: {pack_cost} руб')

