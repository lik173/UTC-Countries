import csv

utcsearch = str(input("UTC (Format: \"+01:00\" or \"-01:30\"): "))
s = utcsearch
if(":" not in utcsearch):
    if (utcsearch[0] == "-"):
        if (len(utcsearch) == 2):
            s = "-" + "0" + utcsearch[1] + ":00"
        if (len(utcsearch) == 3): 
             s = "-" + utcsearch[1:2] + ":00"
    if (utcsearch[0] != "-"):
        if (len(utcsearch) == 2):
            s = utcsearch + ":00"
        if (len(utcsearch) == 1):
            s = "+" + "0" + utcsearch[0] + ":00"
print(s)
with open('timezone_list.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
	    if(row[1][5:11] == s):
             if ("/" in row[0]):
                print(row[0].split("/",1)[1].replace("_", " ") + "  -  " + row[2].replace("\"", ""))
             else:
                print(row[0] + "  -  " + row[2].replace("\"", ""))
		    #print(row[0].split("/",1)[1])