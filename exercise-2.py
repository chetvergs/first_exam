# Вы являетесь разработчиком банка в отделе депозитов. Вам пришла команда создать программу, которая будет высчитывать
# \сложные проценты. На вход программа должна получать сумму депозита, желаемую конечную сумму и годовой процент.
# На выходе должно выдаваться количество месяцев нужных для накопления этой суммы при этом годовом проценте.
#
# Пример: если я положу 1000000 единиц под 12% годовых на 6 месяцев, то в первый месяц моя сумма превратится по формуле
# ( годовой процент / 12 * основная сумма + основная сумма). То есть 0.12/121000000 + 1000000 = 10010000. Следующий
# месяц процент будет от уже увеличенной суммы 0.12/121010000 + 1010000 = 1020100