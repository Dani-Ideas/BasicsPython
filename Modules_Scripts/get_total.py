import functools

def get_total(orders):
  total = functools.reduce(lambda conunter, order:conunter+order['total'],orders,0)
  return total
orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]


total = get_total(orders)
print(total)