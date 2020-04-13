import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-csv', default = 'data.csv')
namespace = parser.parse_args(sys.argv[1:])

import csv

phone_number = '968247916'

sms = 0
call_out_duration = 0
call_in_duration = 0

with open (namespace.csv) as f:
	reader = csv.DictReader(f)
	for row in reader:
		if row['msisdn_origin'] == phone_number:
			sms = sms + int(row['sms_number'])
			call_out_duration += int((float(row['call_duration']) + 0.99)//1)
		if row['msisdn_dest'] == phone_number:
			call_in_duration += int((float(row['call_duration']) + 0.99)//1)

def telephonia(dur, price):
	return dur*price

def messaging(amount, price):
	return amount*price

price_call_out = 3
price_call_in = 1
price_sms = 1

call_out_cost = telephonia(call_out_duration, price_call_out)
call_in_cost = telephonia(call_in_duration, price_call_in)
sms_cost = messaging(sms, price_sms)

print(f'Outgoing calls cost: {call_out_cost}')
print(f'Incoming calls cost: {call_in_cost}')
print(f'SMS cost: {sms_cost}')
print(f'Overall: {call_out_cost + call_in_cost + sms_cost}')
