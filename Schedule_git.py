import random
from datetime import date
import calendar
from twilio.rest import Client

client = Client("####", "####")

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_r = 'whatsapp:+447983994891'


td = date.today()
dow = calendar.day_name[td.weekday()]
chores_daily = ['Empty the dishwasher', 'Make lunch', 'Make dinner', 'Clean the kitchen surfaces']
chores_bi_weekly = ['Hoover the flat', 'Make lunch', 'Make dinner',
                    'Take the bins out',
                    'Do the food shop',
                    'Clean the bathroom',
                    'Do the washing',
                    'Put away the washing']

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element + "\n")
    return result

def define_chore_list(ls):

    total_to_do=len(ls)
    each = int((total_to_do)/2)

    r_list = list()
    for i in range(each):
        randomChore = random.choice(ls)
        ls.remove(randomChore)
        r_list.append(randomChore)
    r_list = concatenate_list_data(r_list)


    e_list = list()
    for i in range(each):
        randomChore = random.choice(ls)
        ls.remove(randomChore)
        e_list.append(randomChore)


    e_list = concatenate_list_data(e_list)
    ruairi_str = str('Daily chores for Ruairi are: \n' + '\n'  +r_list)
    ella_str = str('\nDaily chores for Ella are: \n' + '\n' +  e_list)
    chore_str = str(ruairi_str + ella_str)
    return chore_str



if dow == 'Wednesday' or dow == 'Sunday':
    both_str = define_chore_list(chores_bi_weekly)
else:
    both_str = define_chore_list(chores_daily)

print(both_str)

client.messages.create(body = both_str, from_ = from_whatsapp_number, to = to_whatsapp_r)
