import csv, json

csvFilePath = "data.csv"
jsonFilePath = "data.json"

# Read the CSV and add the data to dictionary ...
with open(csvFilePath) as f:
    reader = csv.DictReader(f)
    rows = list(reader)
#print the list of records with key value pairs
print(rows)
#create an empty dictionary for storing updated data records
newrows = []
for record in rows:
    #loop through each row, which is a dicttionary
    for key,val in record.items():
        #update the records of specific key
        if key == 'plancode':
            updatedvalue = ''.join(str(val).split('-')).strip()
            record[key] = updatedvalue
        if key.startswith('flg'):
            print('updating flg columns')
            if val == 'N':
                record[key] = 'No'
            elif val == 'Y':
                record[key] = 'Yes'
            print('updated record')
    newrows.append(record)
print(newrows)


# Write data to a JSON file ...
with open(jsonFilePath, "w") as f:
    json.dump(rows, f, indent=4)