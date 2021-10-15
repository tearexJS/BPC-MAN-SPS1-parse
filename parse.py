#made by InspektorKiddo_VUC :)

import pandas as pd
import re

def main():
    
    data = pd.read_excel('Zdroj.xlsx', skiprows=7)
    data = data.apply(str)
    data = str(data)
    data = data.replace("            ", ",").replace(", ",",").replace(",-.",",0.").replace(",-,",",0,")
    data = data[:-43]
    #print(data)
    pattern = r"([^\d.,]+)[,. ]([^\d,]+)[,]([^\d,.]+)[,.](\d)[,](\d)"
    matches = re.findall(pattern, data)

    df = {
        'Name':[],
        'University':[],
        'Country':[],
        'Number of publications':[],
        'Number of citations':[]

    }

    for match in matches:
        df['Name'].append(match[0])
        df['University'].append(match[1])
        df['Country'].append(match[2])
        df['Number of publications'].append(match[3])
        df['Number of citations'].append(match[4])

    df = pd.DataFrame(df,columns=['Name', 'University', 'Number of publications', 'Number of citations'])
    writer = pd.ExcelWriter("output.xlsx")
    df.to_excel(writer)
    writer.save()

if __name__ == '__main__':
    main()