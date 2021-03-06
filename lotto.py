import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/thekhenzie/pcso-lotto/master/6-58.csv"
names=['draw','draw_date','prize','wins']
data = pd.read_csv(url, names=names)

nums = range(1,59)
draw = data['draw']

draw_df = draw.str.split("-",expand=True)

list1 = draw_df[0].values.tolist()
list2 = draw_df[1].values.tolist()
list3 = draw_df[2].values.tolist()
list4 = draw_df[3].values.tolist()
list5 = draw_df[4].values.tolist()
list6 = draw_df[5].values.tolist()


list5.extend(list6)
list4.extend(list5)
list3.extend(list4)
list2.extend(list3)
list1.extend(list2)

flist = [int(s) for s in list1]

ctr = [];

for num in nums:
    ctr.insert(num,flist.count(num))

finalDf = pd.DataFrame({'Numbers': nums, 'Appearance': ctr}).sort_values('Appearance',ascending=False)

finalDf.plot(x='Numbers',y='Appearance', rot=0, kind='bar', legend=False)
plt.show()


def lotteryNo():
    import random
    integer = []
    for number in range(0 , 7):
        integer.append(random.randint(0, 58))
    return integer

list_draw = [];
for index,row in draw_df.iterrows():
    list_draw.append(row.values.tolist())

for ld in list_draw:
    ind = list_draw.index(ld);
    if ind !=456:
        for t in range(ind+1, 457):
            x = len(set(ld) & set(list_draw[t]))
            if x==5:
                print(ld+'-'+ind)

print('done')

    
    
