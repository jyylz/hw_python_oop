import datetime as dt
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)
    
    def get_today_stats(self):
        s = 0
        for record in self.records:
            s = (s + record.amount) if record.date == dt.datetime.today().date() else s
        return s
    
    def get_today_remained(self):
        left = self.limit - self.get_today_stats()
        return left
    
    def get_week_stats(self):
        s = 0
        low_boundary = dt.datetime.today().date() - dt.timedelta(days = 7)
        print(low_boundary)
        for record in self.records:
            s = (s + record.amount) if record.date >= low_boundary else s
        return s

class Record:
    date_format = '%d.%m.%Y'

    def __init__(self, amount, comment, date = None):
        self.amount = amount
        if date is not None:
            self.date = dt.datetime.strptime(date, self.date_format).date()
        else: self.date = dt.datetime.today().date()
        self.comment = comment

class CashCalculator(Calculator):
    USD_RATE = 70.0
    EURO_RATE = 60.0
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        left = super().get_today_remained()
        currencies = {
            'rub' : ('руб', self.RUB_RATE),
            'usd' : ('USD', self.USD_RATE),
            'eur' : ('Euro', self.EURO_RATE)
        }
        if currency not in currencies:
            return 'No such currency'
        sign, rate = currencies.get(currency)
        left = round(left/rate,2)
        if left%10==0: left = int(left)
    
        if left > 0: return f'На сегодня осталось {left} {sign}'
        elif left == 0: return 'Денег нет, держись'
        else: return f'Денег нет, держись: твой долг - {abs(left)} {sign}'

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        left = super().get_today_remained()
        if left > 0: return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {left} кКал'
        else: return 'Хватит есть!'