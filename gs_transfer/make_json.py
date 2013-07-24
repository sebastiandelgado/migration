import sys

input_file = sys.argv[1]
present_fields = ['transaction_id', 'click_id', 'install_id', 'date_created', 'unix_time', 'date_short', 'from_user', 'to_user', 'initial', 'final', 'commission', 'source_type']
absent_fields = ['from_app', 'from_campaign', 'from_condition_set', 'to_app', 'to_campaign', 'to_condition_set', 'ad_type', 'creative', 'event_location', 'uuid', 'sdk', 'meta_country','ctr','ir']

f = open(input_file, "r")
o = open(input_file[11:]+".json", "w")
line = f.readline()


while line:
	split_line = line.split(',')
	i = 0
	record = '{'
	for field in present_fields:
		value = split_line[i]
		if value == "0\n": value = "\"0\""
		if value == "": value = "\"\""
		if value[-1] == '\n': value = value[:-1] 
		record += '\"' + field + '\":' + value + ','
		i+=1
	for field in absent_fields:
		comma = ','
		if i == 25: comma = ''
		record += '\"' + field + '\":\"\"' + comma
		i+=1
	record += '}\n'
	o.write(record)
	line = f.readline()

print "generated: " + input_file + ".json"

"""

"4f0014565c2b945d2d000092", -> transaction_id
"4f0014565c2b945d2d000091", -> click_id
, -> install_id
"2012-01-01 00:07:50", -> date_created
"1325405270", -> unix_time
"2012-01-01", -> date_short
"4ebb41a1bcc1fb063b000001", -> from_user
"4e2043f735c6d3803900007d", -> to_user
"0.06", -> initial
"0.042", -> final
"0.018", -> commission
0 -> source_type (?)


transaction_id,
click_id,
install_id,
from_app,
from_campaign,
from_condition_set,
to_app,
to_campaign,
to_condition_set,
ad_type,
creative,
event_location,
uuid,
sdk,
meta_country,
meta_model,
meta_os,
date_created,
unix_time,
date_short,
from_user,
to_user,
initial,
final,
commission,
source_type

"""