import datetime
from decimal import Decimal
DATE_FORMAT = '%Y-%m-%d'
goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 10, 12)},
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}
def add(items, title, amount, expiration_date=None):
    description = dict()
    description['amount'] = Decimal(str(amount))
    if expiration_date is not None:
        expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()
    description['expiration_date'] = expiration_date
    
    if title not in items:
        description_list = list()
        description_list.append(description)
        items[title] = description_list
        
    else:
        items[title].append(description)

#add(goods,'Кола', 0.5, '2019-12-8')
def add_by_note(items, note):
    note_list = str.split(note)
    date = None
    count = None
    title = []
    for word in reversed(note_list):
        if date is None and len(word) == 10 and word[4] == '-' and word[7] == '-':
            year, month, day = word.split('-')
            if year.isdigit() and month.isdigit() and day.isdigit():  #Метод isdigit() возвращает True, если все символы в строке являются цифрами.
                date = word 
                continue
        
        if count is None:
            if word.replace('.', '', 1).isdigit():  
                count = word 
                continue        
        title.append(word) 
    title =' '.join(reversed(title)) 
    count = Decimal(count)
    add(items, title, count, date)

def find(items, needle):
    find_list = list()
    find_num = -1
    
    for title in items:
        find_num = str.lower(title).find(str.lower(needle))
        if find_num >= 0:
            find_list.append(title)   
        find_num = -1   
        
    return find_list
              
def amount(items, needle):
    found_items = find(items, needle)
    amount_count = Decimal('0')
    for item in found_items:
        for title in items[item]:
            amount_count += title['amount']    

    return amount_count

print(amount(goods, 'Пельмени Универсальные'))
def expire(items, in_advance_days=0):
    today_data = datetime.date.today()
    expiration_date = today_data + datetime.timedelta(days=in_advance_days)
    overdue = list()
    for item in items:
        total_amount = Decimal('0.0')
        
        for dict_item in items[item]:
            if dict_item['expiration_date'] is not None:
                if dict_item['expiration_date'] <= expiration_date:
                    total_amount += dict_item['amount']
                   
        if total_amount > 0:
            overdue.append((item,total_amount))
        
    return overdue
    
