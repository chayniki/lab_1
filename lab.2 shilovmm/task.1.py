money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен


months = 0

while money_capital > 0:

    budget = money_capital + salary

    if spend >= budget:
        break

    money_capital = budget - spend
    spend += spend * increase
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)