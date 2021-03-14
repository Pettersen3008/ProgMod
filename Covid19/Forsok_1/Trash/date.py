from datetime import *
import numpy as np

date_today = date.today()
print(date_today)

def get_date(x):
    new_date = date_today + timedelta(x)
    return new_date

print(get_date(28))