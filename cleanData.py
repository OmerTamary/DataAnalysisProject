import csv
import re 
from more_itertools import unique_everseen

def cleanData(): 
    filename = "dataset_raw.csv"
    csvreader = csv.reader(open(filename))
    clean_data = []
    clean_data.append(['address','area','buildYear','date','floor','numOfRooms','price','pricePerMeter','size'])
    
    for row in csvreader:
        clean_row = []
        address = row[0]   
        area = row[1]
        buildYear = row[2]
        date = row[3]
        floor = row[4]
        numOfRooms = row[5]
        price = row[6]
        pricePerMeter = row[7]
        size = row[8]

        if address == "None":
            continue

        if area == "None":
            continue
        elif area == "פלורנטין":
            area = "Florentin"
        elif area == "עזרא":
            area = "Ezra"
        elif area == "התקווה":
            area = "Hatikva"
        elif area == "שפירא":
            area = "shapira"
        elif area == "נוה חן":
            area = "Neve Hen"

        elif area == "נוה ברבור":
            area = "Neve Barbor"

        if date == "None":
            continue

        if re.findall("\d+\.\d+", numOfRooms) == []: #extract number of rooms
            if re.findall(r'\d+', numOfRooms) == []:
                continue
            numOfRooms = re.findall(r'\d+', numOfRooms)[0]
            if len(numOfRooms) != 1:
                continue
        else:
            numOfRooms = re.findall("\d+\.\d+", numOfRooms)[0]

        if float(numOfRooms) > 8:
            continue

        price = re.sub('[^0-9,]', "", price).replace(",", "")#extract price
        if int(price) >= 15000000:
            continue
        if price == "None":
            continue 
        
        pricePerMeter = re.sub('[^0-9,]', "", pricePerMeter).replace(",", "")#extract pricePerMeter

        size = re.findall('\d+', size)[0]
        if int(size) >= 300:
            continue
        elif size == "None":
            continue
        
        if buildYear == "None":
            buildYear= ""
        if floor == "None":
            floor= ""
        if pricePerMeter == "None":
            pricePerMeter= ""
            
        clean_row.append(address)
        clean_row.append(area)
        clean_row.append(buildYear)
        clean_row.append(date)
        clean_row.append(floor)
        clean_row.append(numOfRooms)
        clean_row.append(price)
        clean_row.append(pricePerMeter)
        clean_row.append(size)

        clean_data.append(clean_row)
        
    with open("full_dataset_before.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(clean_data)
    
    with open('full_dataset_before.csv', 'r') as f, open('dataset_ready.csv', 'w') as out_file:
        out_file.writelines(unique_everseen(f))

    
cleanData()
