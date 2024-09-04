# task 1

fwr=[['shoe',1,8,'adidas',2999,6],['slider',2,7,'nike',1299,8],['boots',3,9,'woodland',5999,7]]
import datetime
while True:
 print('''
1.product details
2.view product details
3.update product details
4.search product details
5.delete product details
6.add details      
7.exit
          ''')
 
 choice=int(input("enter your choice :"))
 if choice==1:
         product=str(input("enter product :"))
         id=int(input("enter id :"))
         size=int(input("enter size :"))
         brand=str(input("enter brand :"))
         price=str(input("enter price :"))
         stock=int(input("enter stock :"))
         fwr.append([product,id,size,price,brand,stock])
 elif choice==2:
      for i in fwr:
           print(i)
 elif choice==3:
    id=int(input("enter id :"))
    f=0
    for i in fwr:
        if id in i:                                                                            
            while True:
                 print('''
                    1.product
                    2.size
                    3.brand
                    4.price
                    5.stock
                    6.exit
                    ''')
                 choice=int(input('enter the choice :'))
                 if choice == 1:
                        product=str(input('enter product :'))
                        i[0]=product
                 elif choice == 2:
                        size=int(input('enter size :'))
                        i[2]=size                                                                      
                 elif choice==3:
                        brand=str(input('enter brand :'))
                        i[3]=brand
                 elif choice==4:
                        price=int(input('enter price :'))
                        i[4]=price
                 elif choice==5:
                        stock=str(input('enter stock :'))
                        i[5]=stock
                 elif choice==6:
                        break
                 else:
                        print('invalid choice')
                 f=1
        if f==0:
            print('invalid name')
 elif choice==4:
      id=int(input("enter id :"))
      f=0
      for i in fwr:
           if id in i:
             print(i)
             f=1
      if f==0:
               print('invalid name')
 elif choice==5:
      id=int(input("enter id :"))
      f=0
      for i in fwr:
           if id in i:
             fwr.remove(i)
             f=1
      if f==0:
               print('invalid name')


 elif choice==6:
     id=int(input('enter an id :'))
     for i in fwr:
         if id in i:
             
             date=datetime.datetime.now().strftime('%x')
             i.append([date])


 elif choice==7:
     break
 else:
     print('invalid choice')