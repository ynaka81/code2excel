from openpyxl import load_workbook
import yaml
import re

data_regex = re.compile("^data")
description_regex = re.compile("^description")
attribute_regex = re.compile("\[\"(.*?)\"\]")
data = yaml.load(open("output/directory.yml"))
description = yaml.load(open("test_data/description.yml"))
wb = load_workbook("test_data/directory_template.xlsx")
ws = wb.active
for row in ws.rows:
    for c in row:
        if c.value is not None:
            if data_regex.search(c.value) is not None:
                attributes = attribute_regex.findall(c.value)
                value = data
                for a in attributes:
                    if a in value:
                        value = value[a]
                    else:
                        value = None
                        break
                if value is not None:
                    if value != True:
                        c.value = value
                    else:
                        c.value = "o"
                else:
                    c.value = "x"
            elif description_regex.search(c.value) is not None:
                attributes = attribute_regex.search(c.value).group(1)
                c.value = description[attributes]
wb.save(filename="output/directory.xlsx")
