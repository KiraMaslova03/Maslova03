money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

svobody_money=money_capital+salary-spend
month = 0
while svobody_money>0:
    spend=spend+spend*increase
    svobody_money= svobody_money + salary - spend
    month += 1

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", month)
