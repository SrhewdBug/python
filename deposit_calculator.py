import datetime
import calendar

deposit_amount = int(input('Введите сумму вклада: '))
deposit_term   = int(input('Введите срок вклада в месяцах: '))
interest_rate  = int(input('Введите годовой процент: '))
deposit_type   = input('Вклад с капитализацией (y)/(n)\n')

current_year   = int(datetime.datetime.now().year)
current_month  = int(datetime.datetime.now().month)

if(deposit_type.lower() == 'y'):
    
    for i in range(1, deposit_term + 1):
        days_month = int(calendar.monthrange(current_year, current_month)[1])
        deposit_amount = deposit_amount + (deposit_amount / 100 * interest_rate /365 * days_month)
        if(current_month == 12):
            current_year += 1
            current_month = 1
            continue
        current_month += 1

    print('Сумма по вкладу с капитализацией за период ' + str(deposit_term) + ' месяцев, с процентной ставкой ' + str(interest_rate) +'% составляет ' + str(int(deposit_amount)) + ' рублей')

elif(deposit_type.lower() == 'n'):

    days_year = 0

    for i in range(1, deposit_term + 1):
        days_month = int(calendar.monthrange(current_year, current_month)[1])
        days_year += days_month
        if(current_month == 12):
            current_year += 1
            current_month = 1
            continue
        current_month += 1  

    deposit_amount = deposit_amount + (deposit_amount / 100 * interest_rate) / 365 * days_year
    print('Сумма по вкладу за период ' + str(deposit_term) + ' месяцев, с процентной ставкой ' + str(interest_rate) +'% составляет ' + str(int(deposit_amount)) + ' рублей')

else:
    print('Введено неверное значение')