print("Zooey's (College Fund) Car Shop Services: ")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

def select_svc():
    Tire = 19
    Oil = 35
    Wash = 7
    Wax = 12
    svc_1 = input('Select first service :')
    svc_2 = input('Select second service :')
    return svc_1, svc_2
    
def make_invoice(svc_1, svc_2):
    total = 0
    total_1 = 0
    if svc_1 == 'Oil change':
        total = total + 35
        print('Service 1:', svc_1, ",", Oil)
    if svc_1 == 'Tire rotation':
        total = total + 19
        print('Service 1:', svc_1, ",", Tire)
    if svc_1 == 'Car wash':
        total = total + 7
        print('Service 1:', svc_1, ",", Wash)
    if svc_1 == 'Car wax':
        total = total + 12
        print('Service 1:', svc_1, ",", Wax)
    if svc_1 == 'No service':
        print('-')
    if svc_2 == 'Oil change':
        total_1 = total_1 + 35
        print('Service 2:', svc_2, ",", Oil)
    if svc_2 == 'Tire rotation':
        total_1 = total_1 + 19
        print('Service 2:', svc_2, ",", Tire)
    if svc_2 == 'Car wash':
        total_1 = total_1 + 7
        print('Service 2:', svc_2, ",", Wash)
    if svc_2 == 'Car wax':
        total_1 = total_1 + 12
        print('Service 2:', svc_2, ",", Wax)
    if svc_2 == 'No service':
        print('-')
    total_2 = total  + total_1
    print("Zooey's (College Fund) Car Shop Invoice")
    print('Service 1:', svc_1, ",")
    print('Service 2:', svc_2)
    print('Total: $', total_2)
    return total_2
    
def main():
    svc_1, svc_2 = select_svc()
    total_2 = make_invoice(svc_1, svc_2)
    
main()
