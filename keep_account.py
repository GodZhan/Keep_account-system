import os,ast
import datetime
now = datetime.datetime.today()
date_dt = str(now.month) + '/' + str(now.day)
data = dict()

def meau():
    os.system('cls')
    print('Keep account system')
    print('-------------------')
    print('1. Add item & fee')
    print('2. Check item')
    print('3. Change fee')
    print('4. Delet item & fee')
    print('5. How much I paid this month?')
    print('6. Reset data')
    print('0. Leave system')
    print('-------------------')

def ReadData():
    with open ('Mpay.txt',mode='r',encoding='utf-8-sig') as file:
        filedata = file.read()
        if filedata != '':
            data = ast.literal_eval(filedata)
            return data
        else:
            return dict()

def input_data():
    while True:
        item = input('item name:') + date_dt
        if item == date_dt:
            break
        elif item in data:
            print('{} is been used!'.format(item))
            continue
        fee = input('Input fee:')
        data[item] = fee
        with open('Mpay.txt',mode='w',encoding='utf-8-sig') as file:
            file.write(str(data))
        print('{} has saved'.format(item))            

def check_data():
    print ('item\tfee')
    print ('-----------------')
    for key in data:
        print('{}\t{}'.format(key,data[key]))
    input('press any key back to meau')

def edit_data():
    date3 = input('Input the date(MMDD,ex:4/10):')
    while True:
        item = input('Input item to change:') + date3
        if item == date3:
            break
        elif not item in data:
            print('{} item is not exist!'.format(item))
            continue
        print('Orignal fee is:{}'.format(data[item]))
        fee = input('Input new fee')
        data[item]=fee
        with open ('Mpay.txt',mode='w',encoding='utf-8-sig')as file:
            file.write(str(data))
            input('Fee is changed! Press any key back to meau')
            break
            
def delet_data():
    date2 = input('Input the Date(MMDD,Ex:0410):')
    while True:
        item = input('Input the item to delet:') + date2
        if item == date2:
            break
        if not item in data:
            print('{} is not exist!'.format(item)) 
            continue
        print('Sure to delet the item:{}?'.format(item))
        yn = input('Y/N?')
        if (yn=='Y' or yn =='y'):
            del data[item]
            with open ('Mpay.txt',mode='w',encoding='utf-8-sig') as file:
                file.write(str(data))
                input('Delet successed! Press any key back to the meau')
                break

def tatal():
    sum = 0
    result = list(data.values())
    for i in result:
        sum = sum + int(i)
    print('You have spent {} in this month!'.format(sum))
    input('Press any key back to meau')

def clear():
    Sure = input('Reset data?(Y/N)')
    if (Sure == 'Y' or Sure == 'y'):
        data.clear()
        with open ('Mpay.txt',mode='w',encoding='utf-8-sig') as file:
            file.write(str(data))
            input('Delet successed! Press any key back to the meau')

data = ReadData()
while True:
    meau()
    choise = int(input('Select your service:'))
    if choise == 1:
        input_data()
    elif choise == 2:
        check_data()
    elif choise == 3:
        edit_data()
    elif choise == 4:
        delet_data()
    elif choise == 5:
        tatal()
    elif choise == 6:
        clear()
    else:break

print('Program executed successed!')