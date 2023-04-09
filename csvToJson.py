import csv
import json

def make_json(csvFilePath, jsonFilePath):
    data = []
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf)
        count = 0
        Category = {}
        for rows in csvReader:
            tdata = {}
            # for i in rows.keys():
            #     tdata[i] = rows[i]
            # tdata['Name'] = rows['Name']
            # tdata['Description'] = rows['Description']
            # tdata['Homepage'] = rows['Homepage']
            # tdata['Category'] = rows['Category']
            # tdata['Subcategory'] = rows['Subcategory']
            # tdata['Twitter'] = rows['Twitter']
            # tdata['Github Repo'] = rows['Github Repo']
            # tdata['Github Stars'] = rows['Github Stars']
            # tdata['Crunchbase Linkedin'] = rows['Crunchbase Linkedin']
            tdata['name'] = rows['Name']
            tdata['homepage'] = rows['Homepage']
            tdata['twitter'] = rows['Twitter']
            tdata['pricing'] = rows['Pricing']
            tdata['category'] = rows['Category']
            tdata['sub_category'] = rows['Subcategory']
            tdata['description'] = rows['Description chatGPT']
            data.append(tdata)
            Category[tdata['category']] = Category.get(tdata['category'],[])
            Category[tdata['category']].append(tdata['sub_category'])
            count += 1
        # print(Category)
        # print(data)
        print("count",count)
        for i in Category:
            Category[i] = list(set(Category[i]))
        print(Category)
        
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

csvFilePath = r'toConvertCloud.csv'
jsonFilePath = r'filteredCloud.json'

make_json(csvFilePath, jsonFilePath)