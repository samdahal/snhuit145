# Type your code here
print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')
service1 = input('Select first service: \n');
service2 = input('\nSelect second service: \n');

price_map = {'Tire rotation': '$19', 'Oil change': '$35', 'Car wash': '$7', 'Car wax': '$12', '-':'$0'}

print('\n\nDavy\'s auto shop invoice')
if service1 != '-':
    print('\nService 1: ' + service1 + ', ' + str(price_map[service1]))
else:
    print('\nService 1: No service')

if service2 != '-':
    print('Service 2: ' + service2 + ', ' + str(price_map[service2]))
else:
    print('Service 2: No service')
price = (int(price_map[service1].replace('$', '')) + int(price_map[service2].replace('$', '')))
result = '$' + str(price)
print('\nTotal:', result)