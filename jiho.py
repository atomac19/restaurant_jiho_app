tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes',
      'total': [534.50, 20.0, 5]
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print('table total= ' + str(total))
    print('total tip= ' + str(total_tip))
    print(split_price)

def remove_table_guest(*table_number):
  for number in table_number:
    tables[number] = {}

def add_order_items(table_number, *total_tip_split, **order_items):
     # first separate food items and drink item from order_items
  add_food = order_items.get('food')
  add_drinks = order_items.get('drinks')
     # add_food to food_items and add_drinks to drinks in order
  tables[table_number]['order']['food_items'] += ', ' + add_food
  tables[table_number]['order']['drinks'] += ', ' + add_drinks
    # Add new order's prices to total order prices
  bill_checkbox = 0
  for price in total_tip_split:
    tables[table_number]['order']['total'][bill_checkbox] += price
    bill_checkbox += 1
  # print corrected order
  print("after adding new items")
  print(tables[table_number])

def remove_order_items(table_number, *total_tip_split, **order_items):
  # deleted prices for removed order items from total prices
  position = 0
  for number in total_tip_split:
    tables[table_number]['order']['total'][position] -= number
    position += 1
  # remove items from order
  remove_food = order_items.get('food').split(', ')
  # remove selected food from order
  for food in remove_food:
    tables[table_number]['order']['food_items'] = tables[table_number]['order']['food_items'].replace(food, '', 1).strip(' , ').replace(' , ', ' ')
  # remove selected drinks from order
  remove_drinks = order_items.get('drinks').split(', ')
  for drink in remove_drinks:
    tables[table_number]['order']['drinks'] = tables[table_number]['order']['drinks'].replace(drink, '', 1).strip(' , ').replace(' , ', ' ')

  print('after removing order items ')
  print(tables[1])
  
 # Add the ability to queue reservations for later times for specific tables.
def reservation_table(table_number, reservation='no', date='today'):
  isTableReserved = tables[table_number].get('reservation', 'no')
  if isTableReserved == 'no':
    tables[table_number]['reservation'] = reservation
    tables[table_number]['date'] = date
  else:
    print(f'The table {table_number} is already reserved.')

add_order_items(1, 100, 20, 0, food='Hamburger, Ceasar Salad', drinks='Mohito, Choko milk, 7up, Orange juice')
remove_order_items(1, 100, 20, 0, food='Hamburger, Ceasar Salad', drinks='Mohito, Choko milk, 7up, Orange juice')
reservation_table(1, 'yes', '1st april 2025')
print(tables[1])
reservation_table(1, 'yes', '1st april 2025')
