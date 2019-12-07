from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,Session,sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, CheckConstraint

from datetime import datetime

metadata = MetaData()
engine = create_engine("sqlite:///web/Sqlite-Data/example.db")
customers = Table('customers', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('first_name', String(100), nullable=False),
                  Column('last_name', String(100), nullable=False),
                  Column('username', String(50), nullable=False),
                  Column('email', String(200), nullable=False),
                  Column('address', String(200), nullable=False),
                  Column('town', String(50), nullable=False),
                  Column('created_on', DateTime(), default=datetime.now),
                  Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
                  )

items = Table('items', metadata,
              Column('id', Integer(), primary_key=True),
              Column('name', String(200), nullable=False),
              Column('cost_price', Numeric(10, 2), nullable=False),
              Column('selling_price', Numeric(10, 2), nullable=False),
              Column('quantity', Integer(), nullable=False),
              CheckConstraint('quantity > 0', name='quantity_check')
              )

orders = Table('orders', metadata,
               Column('id', Integer(), primary_key=True),
               Column('customer_id', ForeignKey('customers.id')),
               Column('date_placed', DateTime(), default=datetime.now),
               Column('date_shipped', DateTime())
               )

order_lines = Table('order_lines', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('order_id', ForeignKey('orders.id')),
                    Column('item_id', ForeignKey('items.id')),
                    Column('quantity', Integer())
                    )

metadata.create_all(engine)

c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

c1, c2
session.add(c1)
session.add(c2)

session.add_all([c1, c2])

session.new
session.commit()

c1.id, c2.id

c1.orders, c2.orders

c3 = Customer(
    first_name="John",
    last_name="Lara",
    username="johnlara",
    email="johnlara@mail.com",
    address="3073 Derek Drive",
    town="Norfolk"
)

c4 = Customer(
    first_name="Sarah",
    last_name="Tomlin",
    username="sarahtomlin",
    email="sarahtomlin@mail.com",
    address="3572 Poplar Avenue",
    town="Norfolk"
)

c5 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c6 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

session.add_all([c3, c4, c5, c6])
session.commit()

i1 = Item(name='Chair', cost_price=9.21, selling_price=10.81, quantity=5)
i2 = Item(name='Pen', cost_price=3.45, selling_price=4.51, quantity=3)
i3 = Item(name='Headphone', cost_price=15.52, selling_price=16.81, quantity=50)
i4 = Item(name='Travel Bag', cost_price=20.1, selling_price=24.21, quantity=50)
i5 = Item(name='Keyboard', cost_price=20.1, selling_price=22.11, quantity=50)
i6 = Item(name='Monitor', cost_price=200.14, selling_price=212.89, quantity=50)
i7 = Item(name='Watch', cost_price=100.58, selling_price=104.41, quantity=50)
i8 = Item(name='Water Bottle', cost_price=20.89, selling_price=25, quantity=50)

session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
session.commit()

o1 = Order(customer=c1)
o2 = Order(customer=c1)

line_item1 = OrderLine(order=o1, item=i1, quantity=3)
line_item2 = OrderLine(order=o1, item=i2, quantity=2)
line_item3 = OrderLine(order=o2, item=i1, quantity=1)
line_item3 = OrderLine(order=o2, item=i2, quantity=4)

session.add_all([o1, o2])

session.new
session.commit()


o3 = Order(customer=c1)
orderline1 = OrderLine(item=i1, quantity=5)
orderline2 = OrderLine(item=i2, quantity=10)

o3.order_lines.append(orderline1)
o3.order_lines.append(orderline2)

session.add_all([o3])

session.commit()

c1.orders

o1.customer

c1.orders[0].order_lines, c1.orders[1].order_lines


for ol in c1.orders[0].order_lines:
    ol.id, ol.item, ol.quantity

print('-------')

for ol in c1.orders[1].order_lines:
    ol.id, ol.item, ol.quantity


session.query(Customer).all()
print(session.query(Customer))

q = session.query(Customer)

for c in q:
    print(c.id, c.first_name)

session.query(Customer.id, Customer.first_name).all()


session.query(Customer).count() # get the total number of records in the customers table
session.query(Item).count()  # get the total number of records in the items table
session.query(Order).count()  # get the total number of records in the orders table

session.query(Customer).first()
session.query(Item).first()
session.query(Order).first()

session.query(Customer).get(1)
session.query(Item).get(1)
session.query(Order).get(100)


session.query(Customer).filter(Customer.first_name == 'John').all()

print(session.query(Customer).filter(Customer.first_name == 'John'))

session.query(Customer).filter(Customer.id <= 5, Customer.town == "Norfolk").all()

print(session.query(Customer).filter(Customer.id <= 5, Customer.town.like("Nor%"))

# find all customers who either live in Peterbrugh or Norfolk

session.query(Customer).filter(or_(
    Customer.town == 'Peterbrugh',
    Customer.town == 'Norfolk'
)).all()

# find all customers whose first name is John and live in Norfolk

session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    Customer.town == 'Norfolk'
)).all()

# find all johns who don't live in Peterbrugh

session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    not_(
        Customer.town == 'Peterbrugh',
    )
)).all()

session.query(Order).filter(Order.date_shipped == None).all()
session.query(Order).filter(Order.date_shipped == None).all()
session.query(Customer).filter(Customer.first_name.in_(['Toby', 'Sarah'])).all()
session.query(Customer).filter(Customer.first_name.notin_(['Toby', 'Sarah'])).all()
session.query(Item).filter(Item.cost_price.between(10, 50)).all()
session.query(Item).filter(not_(Item.cost_price.between(10, 50))).all()

session.query(Item).filter(Item.name.like("%r")).all() #like
session.query(Item).filter(Item.name.ilike("w%")).all()
#NOT LIKE
session.query(Item).filter(not_(Item.name.like("W%"))).all()
session.query(Customer).limit(2).all()
session.query(Customer).filter(Customer.address.ilike("%avenue")).limit(2).all()

print(session.query(Customer).limit(2))
print(session.query(Customer).filter(Customer.address.ilike("%avenue")).limit(2))

#offset() method
session.query(Customer).limit(2).offset(2).all()
print(session.query(Customer).limit(2).offset(2))
#order_by() method
session.query(Item).filter(Item.name.ilike("wa%")).all()
session.query(Item).filter(Item.name.ilike("wa%")).order_by(Item.cost_price).all()
#join() method
session.query(Customer).join(Order).all()
print(session.query(Customer).join(Order))
session.query(Customer.id, Customer.username, Order.id).join(Order).all()
session.query(Table1).join(Table2).join(Table3).join(Table4).all()
session.query(
    Customer.first_name,
    Item.name,
    Item.selling_price,
    OrderLine.quantity
).join(Order).join(OrderLine).join(Item).filter(
    Customer.first_name == 'John',
    Customer.last_name == 'Green',
    Order.id == 1,
).all()
session.query(
    Customer.first_name,
    Item.name,
    Item.selling_price,
    OrderLine.quantity
).join(Order).join(OrderLine).join(Item).filter(
    Customer.first_name == 'John',
    Customer.last_name == 'Green',
    Order.id == 1,
).all()
#outerjoin() method
session.query(
    Customer.first_name,
    Order.id,
).outerjoin(Order).all()
#
session.query(
    Customer.first_name,
    Order.id,
).outerjoin(Order, full=True).all()
#group_by() method
from sqlalchemy import func
session.query(func.count(Customer.id)).join(Order).filter(
    Customer.first_name == 'John',
    Customer.last_name == 'Green',
).group_by(Customer.id).scalar()
#having() method
session.query(
    func.count("*").label('town_count'),
    Customer.town
).group_by(Customer.town).having(func.count("*") > 2).all()

# Dealing with Duplicates SECTION
from sqlalchemy import distinct

session.query(Customer.town).filter(Customer.id < 10).all()
session.query(Customer.town).filter(Customer.id < 10).distinct().all()

session.query(
    func.count(distinct(Customer.town)),
    func.count(Customer.town)
).all()

#Casting
from sqlalchemy import cast, Date, distinct, union

session.query(
    cast(func.pi(), Integer),
    cast(func.pi(), Numeric(10, 2)),
    cast("2010-12-01", DateTime),
    cast("2010-12-01", Date),
).all()

# Unions
s1 = session.query(Item.id, Item.name).filter(Item.name.like("Wa%"))
s2 = session.query(Item.id, Item.name).filter(Item.name.like("%e%"))
s1.union(s2).all()

s1.union_all(s2).all()

# Updating Data
i = session.query(Item).get(8)
i.selling_price = 25.91
session.add(i)
session.commit()
session.query(Item).filter(
    Item.name.ilike("W%")
).update({"quantity": 60}, synchronize_session='fetch')
session.commit()

# Deleting Data
i = session.query(Item).filter(Item.name == 'Monitor').one()
i
session.delete(i)
session.commit()

session.query(Item).filter(
    Item.name.ilike("W%")
).delete(synchronize_session='fetch')
session.commit()

