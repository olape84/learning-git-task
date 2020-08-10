shopping_list = {'Piekarnia' :  ['Chleb', 'Pączek', 'Bułki'], \
'Warzywniak' :  ['Marchew', 'Seler', 'Rukola']}
for  sklep in shopping_list:
    print(f'Idę do  {sklep} kupic następujące rzeczy {shopping_list[sklep]}')
Piekarnia =set()
Warzywniak=set()
sum_set=Piekarnia|Warzywniak
print(f'W sumie kupuje {sum_set} produktów.')
