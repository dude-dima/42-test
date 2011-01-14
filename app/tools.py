from models import Customer

def get_default_context(request, menu_item=''):
    c = {}
    c['user'] = request.user
    if menu_item:
        c[menu_item] = 'menu-selected'
    return c
    
def get_default_customer():
    try:
        cust = Customer.objects.all()[0]
    except:
        ### Just for storing data into database
        cust = Customer()
        cust.name = "Dmitry"
        cust.surname = "Razumov"
        cust.bio = "Some bio"
        cust.contacts = "380500000000"
        cust.birth_date = "1983-07-12"
        cust.save()
    return cust
