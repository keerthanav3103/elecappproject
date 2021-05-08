import random
import string
import json
mydatabase={}
idx=0
def bookingappliance(myname):
    print("Hi",myname,'!')
    myuserdict={}
    Appliance={1:'TV',2:'Washing machine',3:'AC',4:'Refrigerator'}
    Brands={'TV':{1:'Samsung',2:'Sony',3:'LG',4:'Panasonic'},'WashingMachine':{1:'Samsung',2:'Whirlpool',3:'LG',4:'Bosch'},'AC':{1:'Samsung',2:'Voltas',3:'Bluestar',4:'Daikin'},'Refrigerator':{1:'Samsung',2:'KitchenAid',3:'Maytag',4:'LG'}}
    TV_Samsung={'Type':{1:'Full HD',2:'4K UHD',3:'QLED'},'Size':{1:'42 inches',2:'55 inches',3:'75 inches'},'Price':{1:'20000-40000',2:'40000-75000',3:'75000-100000'}}
    TV_Sony={'Type':{1:'Full Array LED',2:'4K UHD',3:'OLED'},'Size':{1:'38 inches',2:'42 inches',3:'70 inches'},'Price':{1:'20000-30000',2:'30000-60000',3:'60000-80000'}}
    TV_LG={'Type':{1:'4K UHD',2:'8K UHD',3:'OLED'},'Size':{1:'48 inches',2:'55 inches',3:'80 inches'},'Price':{1:'20000-40000',2:'40000-70000',3:'70000-95000'}}
    TV_Panasonic={'Type':{1:'Full HD LED',2:'4K UHD',3:'QLED'},'Size':{1:'40 inches',2:'52 inches',3:'70 inches'},'Price':{1:'10000-30000',2:'30000-50000',3:'50000-75000'}}
    WM_Samsung={'Type':{1:'SemiAutomatic',2:'FullyAutomatic'},'LoadType':{1:'FrontLoad',2:'TopLoad'},'CapacityinKg':{1:'5.5-6.5',2:'6.5-7.5'},'Price':{1:'10000-15000',2:'15000-20000',3:'20000-25000'}}
    WM_Whirlpool={'Type':{1:'SemiAutomatic',2:'FullyAutomatic'},'LoadType':{1:'FrontLoad',2:'TopLoad'},'CapacityinKg':{1:'5.0-6.0',2:'6.0-7.0'},'Price':{1:'10000-14000',2:'14000-19000',3:'19000-25000'}}
    WM_LG={'Type':{1:'SemiAutomatic',2:'FullyAutomatic'},'LoadType':{1:'FrontLoad',2:'TopLoad'},'CapacityinKg':{1:'5.5-6.5',2:'6.5-7.5'},'Price':{1:'10000-15000',2:'15000-25000',3:'25000-30000'}}
    WM_Bosch={'Type':{1:'SemiAutomatic',2:'FullyAutomatic'},'LoadType':{1:'FrontLoad',2:'TopLoad'},'CapacityinKg':{1:'5.0-6.0',2:'6.0-7.0'},'Price':{1:'10000-15000',2:'15000-20000',3:'20000-25000'}}
    AC_Samsung={'Type':{1:'SplitType',2:'WindowType'},'Tonnage':{1:'1 ton',2:'1.5ton',3:'2ton',4:'2.5ton'},'StarRating':{1:'3 star',2:'4 star',3:'5 star'},'Price':{1:'20000-25000',2:'25000-30000',3:'30000-40000'}}
    AC_Voltas={'Type':{1:'SplitType',2:'WindowType'},'Tonnage':{1:'1 ton',2:'1.5ton',3:'2ton',4:'2.5ton'},'StarRating':{1:'3 star',2:'4 star',3:'5 star'},'Price':{1:'25000-30000',2:'30000-40000',3:'40000-50000'}}
    AC_Bluestar={'Type':{1:'SplitType',2:'WindowType'},'Tonnage':{1:'1 ton',2:'1.5ton',3:'2ton',4:'2.5ton'},'StarRating':{1:'3 star',2:'4 star',3:'5 star'},'Price':{1:'20000-25000',2:'25000-30000',3:'30000-50000'}}
    AC_Daikin={'Type':{1:'SplitType',2:'WindowType'},'Tonnage':{1:'1 ton',2:'1.5ton',3:'2ton',4:'2.5ton'},'StarRating':{1:'3 star',2:'4 star',3:'5 star'},'Price':{1:'25000-30000',2:'30000-40000',3:'40000-50000'}}
    FR_Samsung={'Design':{1:'SingleDoor',2:'DoubleDoor'},'StarRating':{1:'3 star',2:'4 star',3:'5 star'},'Price':{1:'25000-30000',2:'30000-40000',3:'40000-50000'}}
    FR_KitchenAid={'Design':{1:'SingleDoor',2:'DoubleDoor'},'StarRating':{1:'3 star',2:'4 star',3:'5 star'},'Price':{1:'25000-30000',2:'30000-40000',3:'40000-50000'}}
    FR_Maytag={'Design':{1:'SingleDoor',2:'DoubleDoor'},'StarRating':{1:'3 star',2:'4 star',3:'5 star'},'Price':{1:'25000-30000',2:'30000-40000',3:'40000-50000'}}
    FR_LG={'Design':{1:'SingleDoor',2:'DoubleDoor'},'StarRating':{1:'3 star',2:'4 star',3:'5 star'},'Price':{1:'25000-30000',2:'30000-40000',3:'40000-50000'}}
    myuserdict['Customer name']=myname
    print('What do you want to view ?')
    for key,val in Appliance.items():
        print (key,'-',val)
    print("Enter your choice...")
    c1=int(input())
    if c1==1:
        print("Here are the top TV brands!!")
        for i, j in Brands.items():
            if i=='TV':
                for key in j:print(key ,'-', j[key])
        print("Choose your favorite brand...")
        b1=int(input())
        print('Let us get into ',Brands['TV'][b1])
        if b1==1:
            for i, j in TV_Samsung.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])    
            print('Do you want to got by\n1.Type of TV\n2.Screen size\n3.Price\n')
            d1=int(input())
            if d1==1:
                TV_Samsung_type={1:['Full HD' ,'55inches', 50000],2:['4K UHD','55inches',45000],3:['QLED', '75inches',60000]}
                for key,val in TV_Samsung_type.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(TV_Samsung_type.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-')
            elif d1==2:
                TV_Samsung_size={1:['Full HD' ,'42inches', 55000],2:['QLED','55inches',70000],3:['QLED', '75inches',80000]}
                for key,val in TV_Samsung_size.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(TV_Samsung_size.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-')
            elif d1==3:
                TV_Samsung_price={1:['Full HD' ,'42inches', 50000],2:['4K UHD','55inches',65000],3:['QLED', '75inches',85000]}
                for key,val in TV_Samsung_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(TV_Samsung_price.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-')
        elif b1==2:
            for i, j in TV_Sony.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Type of TV\n2.Screen size\n3.Price\n')
            d1=int(input())
            if d1==1:
                TV_Sony_type={1:['Full Array LED','42inches', 55000],2:['4K UHD','70inches',70000],3:['OLED', '38inches',45000]}
                for key,val in TV_Sony_type.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(TV_Sony_price.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-')
            elif d1==2:
                TV_Sony_size={1:['Full Array LED' ,'42inches', 55000],2:['OLED', '38inches',60000],3:['4K UHD','38inches',50000]}
                for key,val in TV_Sony_size.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(TV_Sony_size.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-')
            elif d1==3:
                TV_Sony_price={1:['4K UHD','38inches',30000],2:['OLED', '38inches',55000],3:['Full Array LED' ,'55inches', 50000]}
                for key,val in TV_Sony_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(TV_Sony_price.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-')
        elif b1==3:
            for i, j in TV_LG.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Type of TV\n2.Screen size\n3.Price\n')
            d1=int(input())
            if d1==1:
                TV_LG_type={1:['4K UHD','48inches',40000],2:['8K UHD' ,'55inches', 75000],3:['OLED', '80inches',80000]}
                for key,val in TV_LG_type.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(TV_LG_type.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-')
            elif d1==2:
                TV_LG_size={1:['8K UHD' ,'48inches', 50000],2:['4K UHD','55inches',45000],3:['OLED', '80inches',80000]}
                for key,val in TV_LG_size.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(TV_LG_size.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-')
            elif d1==3:
                TV_LG_price={1:['4K UHD','80inches',75000],2:['OLED', '55inches',60000],3:['8K UHD' ,'55inches', 60000]}
                for key,val in TV_LG_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(TV_LG_price.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-')
        elif b1==4:
            for i, j in TV_Panasonic.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Type of TV\n2.Screen size\n3.Price\n')
            d1=int(input())
            if d1==1:
                TV_Panasonic_type={1:['Full HD' ,'40inches', 35000],1:['QLED', '52inches',60000],3:['4K UHD','52inches',50000]}
                for key,val in TV_Panasonic_type.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(TV_Panasonic_type.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-')
            elif d1==2:
                TV_Panasonic_size={1:['Full HD' ,'52inches', 50000],2:['4K UHD','52inches',50000],3:['QLED', '70inches',70000]}
                for key,val in TV_Panasonic_size.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(TV_Panasonic_size.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-')
            elif d1==3:
                TV_Panasonic_price={1:['4K UHD','40inches',45000],2:['QLED', '70inches',70000],3:['Full HD' ,'40inches', 35000]}
                for key,val in TV_Panasonic_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(TV_Panasonic_price.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-')

    elif c1==2:
        print("Here are the top WashingMachine brands!!")
        for i, j in Brands.items():
            if i=='WashingMachine':
                for key in j:print(key ,'-', j[key])
        print("Choose your favorite brand...")
        b1=int(input())
        print('Let us get into ',Brands['WashingMachine'][b1])
        if b1==1:
            for i, j in WM_Samsung.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Type\n2.LoadType\n3.CapacityinKg\n4.Price')
            d1=int(input())
            if d1==1:
                WM_Samsung_type={1:['SemiAutomatic','FrontLoad',5.5,15000],2:['SemiAutomatic' ,'TopLoad',6.0,20000],3:['FullyAutomatic' ,'FrontLoad',6.5,25000]}
                for key,val in WM_Samsung_type.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_Samsung_type.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-') 
            elif d1==2:
                WM_Samsung_loadtype={1:['SemiAutomatic','FrontLoad',5.5,15000],2:['SemiAutomatic' ,'TopLoad',6.0,20000],3:['FullyAutomatic' ,'FrontLoad',6.0,20000]}
                for key,val in WM_Samsung_loadtype.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_Samsung_loadtype.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==3:
                WM_Samsung_capacity={1:['FullyAutomatic' ,'FrontLoad',6.5,23000],2:['SemiAutomatic','FrontLoad',5.5,15000],3:['FullyAutomatic' ,'TopLoad',7.0,25000]}
                for key,val in WM_Samsung_capacity.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_Samsung_capacity.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==4:
                WM_Samsung_price={1:['FullyAutomatic' ,'FrontLoad',5.0,17000],2:['SemiAutomatic','FrontLoad',5.5,19000],3:['FullyAutomatic' ,'TopLoad',6.5,24000]}
                for key,val in WM_Samsung_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_Samsung_price.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
        elif b1==2:
            for i, j in WM_Whirlpool.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Type\n2.LoadType\n3.CapacityinKg\n4.Price')
            d1=int(input())
            if d1==1:
                WM_Whirlpool_type={1:['SemiAutomatic','FrontLoad',5.0,10000],2:['SemiAutomatic' ,'TopLoad',6.0,20000],3:['FullyAutomatic' ,'FrontLoad',6.5,25000]}
                for key,val in WM_Whirlpool_type.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_Whirlpool_type.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==2:
                WM_Whirlpool_loadtype={1:['SemiAutomatic','FrontLoad',5.5,15000],2:['SemiAutomatic' ,'TopLoad',5.0,17000],3:['FullyAutomatic' ,'FrontLoad',6.0,20000]}
                for key,val in WM_Whirlpool_loadtype.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_Whirlpool_loadtype.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==3:
                WM_Whirlpool_capacity={1:['FullyAutomatic' ,'FrontLoad',6.5,23000],2:['SemiAutomatic','FrontLoad',5.5,15000],3:['FullyAutomatic' ,'TopLoad',7.0,25000]}
                for key,val in WM_Whirlpool_capacity.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_Whirlpool_capacity.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==4:
                WM_Whirlpool_price={1:['FullyAutomatic' ,'FrontLoad',5.0,17000],2:['SemiAutomatic','FrontLoad',5.5,19000],3:['FullyAutomatic' ,'TopLoad',6.5,24000]}
                for key,val in WM_Whirlpool_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_Whirlpool_price.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
        elif b1==3:
            for i, j in WM_LG.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Type\n2.LoadType\n3.CapacityinKg\n4.Price')
            d1=int(input())
            if d1==1:
                WM_LG_type={1:['SemiAutomatic','FrontLoad',5.5,15000],2:['SemiAutomatic' ,'TopLoad',6.0,20000],3:['FullyAutomatic' ,'FrontLoad',6.5,25000]}
                for key,val in WM_LG_type.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_LG_type.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-') 
            elif d1==2:
                WM_LG_loadtype={1:['SemiAutomatic','FrontLoad',5.5,15000],2:['SemiAutomatic' ,'TopLoad',6.0,20000],3:['FullyAutomatic' ,'FrontLoad',6.0,20000]}
                for key,val in WM_LG_loadtype.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_LG_loadtype.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==3:
                WM_LG_capacity={1:['FullyAutomatic' ,'FrontLoad',6.5,23000],2:['SemiAutomatic','FrontLoad',5.5,15000],3:['FullyAutomatic' ,'TopLoad',7.0,25000]}
                for key,val in WM_LG_capacity.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_LG_capacity.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==4:
                WM_LG_price={1:['FullyAutomatic' ,'FrontLoad',5.0,17000],2:['SemiAutomatic','FrontLoad',5.5,19000],3:['FullyAutomatic' ,'TopLoad',6.5,24000]}
                for key,val in WM_LG_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_LG_price.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
        elif b1==4:
            for i, j in WM_Bosch.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Type\n2.LoadType\n3.CapacityinKg\n4.Price')
            d1=int(input())
            if d1==1:
                WM_Bosch_type={1:['SemiAutomatic','FrontLoad',5.0,10000],2:['SemiAutomatic' ,'TopLoad',6.0,20000],3:['FullyAutomatic' ,'FrontLoad',6.5,25000]}
                for key,val in WM_Bosch_type.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_Bosch_type.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-') 
            elif d1==2:
                WM_Bosch_loadtype={1:['SemiAutomatic','FrontLoad',5.5,15000],2:['SemiAutomatic' ,'TopLoad',5.0,17000],3:['FullyAutomatic' ,'FrontLoad',6.0,20000]}
                for key,val in WM_Bosch_loadtype.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_Bosch_loadtype.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==3:
                WM_Bosch_capacity={1:['FullyAutomatic' ,'FrontLoad',6.5,23000],2:['SemiAutomatic','FrontLoad',5.5,15000],3:['FullyAutomatic' ,'TopLoad',7.0,25000]}
                for key,val in WM_Bosch_capacity.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_Bosch_capacity.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==4:
                WM_Bosch_price={1:['FullyAutomatic' ,'FrontLoad',5.0,17000],2:['SemiAutomatic','FrontLoad',5.5,19000],3:['FullyAutomatic' ,'TopLoad',6.5,24000]}
                for key,val in WM_Bosch_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(WM_Bosch_price.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
        
    elif c1==3:
        print("Here are the top AC brands!!")
        for i, j in Brands.items():
            if i=='AC':
                for key in j:print(key ,'-', j[key])
        print("Choose your favorite brand...")
        b1=int(input())
        print('Let us get into ',Brands['AC'][b1])
        if b1==1:
            for i, j in AC_Samsung.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Type\n2.Tonnage\n3.StarRating\n4.Price\n')
            d1=int(input())
            if d1==1:
                AC_Samsung_type={1:['split','1.5ton',4,23000],2:['window' ,'2.0ton',3,28000],3:['window','2.5ton',5,50000]}
                for key,val in AC_Samsung_type.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Samsung_type.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==2:
                AC_Samsung_tonnage={1:['split','1.5ton',4,23000],2:['window' ,'2.0ton',3,28000],3:['window','2.5ton',5,50000]}
                for key,val in AC_Samsung_tonnage.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Samsung_tonnage.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==3:
                AC_Samsung_starrating={1:['split','1.5ton',3,20000],2:['window' ,'2.0ton',4,35000],3:['split','2.5ton',5,45000]}
                for key,val in AC_Samsung_starrating.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Samsung_starrating.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==4:
                AC_Samsung_price={1:['window' ,'2.0ton',4,35000],2:['split','1.5ton',3,20000],3:['split','2.5ton',5,45000]}
                for key,val in AC_Samsung_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Samsung_price.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
        elif b1==2:
            for i, j in AC_Voltas.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Type\n2.Tonnage\n3.StarRating\n4.Price\n')
            d1=int(input())
            if d1==1:
                AC_Voltas_type={1:['split','1.5ton',4,23000],2:['window' ,'2.0ton',3,28000],3:['window','2.5ton',5,50000]}
                for key,val in AC_Voltas_type.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Voltas_type.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')  
            elif d1==2:
                AC_Voltas_tonnage={1:['split','1.5ton',4,23000],2:['window' ,'2.0ton',3,28000],3:['window','2.5ton',5,50000]}
                for key,val in AC_Voltas_tonnage.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Voltas_tonnage.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==3:
                AC_Voltas_starrating={1:['split','1.5ton',3,20000],2:['window' ,'2.0ton',4,35000],3:['split','2.5ton',5,45000]}
                for key,val in AC_Voltas_starrating.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Voltas_starrating.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-')
            elif d1==4:
                AC_Voltas_price={1:['window' ,'2.0ton',4,35000],2:['split','1.5ton',3,20000],3:['split','2.5ton',5,45000]}
                for key,val in AC_Voltas_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Voltas_price.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-') 
        elif b1==3:
            for i, j in AC_Bluestar.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Type\n2.Tonnage\n3.StarRating\n4.Price\n')
            d1=int(input())
            if d1==1:
                AC_Bluestar_type={1:['split','1.5ton',4,23000],2:['window' ,'2.0ton',3,28000],3:['window','2.5ton',5,50000]}
                for key,val in AC_Bluestar_type.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Bluestar_type.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-') 
            elif d1==2:
                AC_Bluestar_tonnage={1:['split','1.5ton',4,23000],2:['window' ,'2.0ton',3,28000],3:['window','2.5ton',5,50000]}
                for key,val in AC_Bluestar_tonnage.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Bluestar_tonnage.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-') 
            elif d1==3:
                AC_Bluestar_starrating={1:['split','1.5ton',3,20000],2:['window' ,'2.0ton',4,35000],3:['split','2.5ton',5,45000]}
                for key,val in AC_Bluestar_starrating.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Bluestar_starrating.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-') 
            elif d1==4:
                AC_Bluestar_price={1:['window' ,'2.0ton',4,35000],2:['split','1.5ton',3,20000],3:['split','2.5ton',5,45000]}
                for key,val in AC_Bluestar_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Bluestar_price.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-') 
        elif b1==4:
            for i, j in AC_Daikin.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Type\n2.Tonnage\n3.StarRating\n4.Price\n')
            d1=int(input())
            if d1==1:
                AC_Daikin_type={1:['split','1.5ton',4,23000],2:['window' ,'2.0ton',3,28000],3:['window','2.5ton',5,50000]}
                for key,val in AC_Daikin_type.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Daikin_type.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-') 
            elif d1==2:
                AC_Daikin_tonnage={1:['split','1.5ton',4,23000],2:['window' ,'2.0ton',3,28000],3:['window','2.5ton',5,50000]}
                for key,val in AC_Daikin_tonnage.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Daikin_tonnage.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-') 
            elif d1==3:
                AC_Daikin_starrating={1:['split','1.5ton',3,20000],2:['window' ,'2.0ton',4,35000],3:['split','2.5ton',5,45000]}
                for key,val in AC_Daikin_starrating.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Daikin_starrating.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-') 
            elif d1==4:
                AC_Daikin_price={1:['window' ,'2.0ton',4,35000],2:['split','1.5ton',3,20000],3:['split','2.5ton',5,45000]}
                for key,val in AC_Daikin_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(AC_Daikin_price.get(e))
                print('Your selection :',val)
                amt=val[3]
                print('Grand total:Rs',val[3],'/-') 
            
    elif c1==4:
        print("Here are the top Refrigerator brands!!")
        for i, j in Brands.items():
            if i=='Refrigerator':
                for key in j:print(key ,'-', j[key])
        print("Choose your favorite brand...")
        b1=int(input())
        print('Let us get into ',Brands['Refrigerator'][b1])
        if b1==1:
            for i, j in FR_Samsung.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Design\n2.StarRating\n3.Price')
            d1=int(input())
            if d1==1:
                FR_Samsung_design={1:['SingleDoor' ,3, 25000],2:['DoubleDoor',3,27000],3:['SingleDoor',5,35000]}
                for key,val in FR_Samsung_design.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(FR_Samsung_design.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-') 
            elif d1==2:
                FR_Samsung_starrating={1:['SingleDoor' ,3, 25000],2:['DoubleDoor',4,35000],3:['DoubleDoor',5,48000]}
                for key,val in FR_Samsung_starrating.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(FR_Samsung_starrating.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-') 
            elif d1==3:
                FR_Samsung_price={1:['SingleDoor' ,4, 30000],2:['DoubleDoor',4,35000],3:['DoubleDoor',5,48000]}
                for key,val in FR_Samsung_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(FR_Samsung_price.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-') 
        elif b1==2:
            for i, j in FR_KitchenAid.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Design\n2.StarRating\n3.Price')
            d1=int(input())
            if d1==1:
                FR_KitchenAid_design={1:['SingleDoor' ,3, 25000],2:['DoubleDoor',3,27000],3:['SingleDoor',5,35000]}
                for key,val in FR_KitchenAid_design.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(FR_KitchenAid_design.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-') 
            elif d1==2:
                FR_KitchenAid_starrating={1:['SingleDoor' ,3, 25000],2:['DoubleDoor',4,35000],3:['DoubleDoor',5,48000]}
                for key,val in FR_KitchenAid_starrating.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(FR_KitchenAid_starrating.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-') 
            elif d1==3:
                FR_KitchenAid_price={1:['SingleDoor' ,4, 30000],2:['DoubleDoor',4,35000],3:['DoubleDoor',5,48000]}
                for key,val in FR_KitchenAid_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(FR_KitchenAid_price.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-') 
        elif b1==3:
            for i, j in FR_Maytag.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Design\n2.StarRating\n3.Price')
            d1=int(input())
            if d1==1:
                FR_Maytag_design={1:['SingleDoor' ,3, 25000],2:['DoubleDoor',3,27000],3:['SingleDoor',5,35000]}
                for key,val in FR_Maytag_design.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(FR_Maytag_design.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-') 
            elif d1==2:
                FR_Maytag_starrating={1:['SingleDoor' ,3, 25000],2:['DoubleDoor',4,35000],3:['DoubleDoor',5,48000]}
                for key,val in FR_Maytag_starrating.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(FR_Maytag_starrating.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-') 
            elif d1==3:
                FR_Maytag_price={1:['SingleDoor' ,4, 30000],2:['DoubleDoor',4,35000],3:['DoubleDoor',5,48000]}
                for key,val in FR_Maytag_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(FR_Maytag_price.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-') 
        elif b1==4:
            for i, j in FR_LG.items():
                print(i)
                for key in j:
                    print(key ,'-', j[key])
            print('Do you want to got by\n1.Design\n2.StarRating\n3.Price')
            d1=int(input())
            if d1==1:
                FR_LG_design={1:['SingleDoor' ,3, 25000],2:['DoubleDoor',3,27000],3:['SingleDoor',5,35000]}
                for key,val in FR_LG_design.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(FR_LG_design.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-') 
            elif d1==2:
                FR_LG_starrating={1:['SingleDoor' ,3, 25000],2:['DoubleDoor',4,35000],3:['DoubleDoor',5,48000]}
                for key,val in FR_LG_starrating.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(FR_LG_starrating.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-') 
            elif d1==3:
                FR_LG_price={1:['SingleDoor' ,4, 30000],2:['DoubleDoor',4,35000],3:['DoubleDoor',5,48000]}
                for key,val in FR_LG_price.items():
                    print(key,'---',val)
                e=int(input('My order is :'))
                print("Your selection!!!")
                val=list(FR_LG_price.get(e))
                print('Your selection :',val)
                amt=val[2]
                print('Grand total:Rs',val[2],'/-') 
    
    else:
        print("No such option exists.Please enter the correct one")
    
    print('Please enter your mobile number and address')
    mb=int(input('Mobile : '))
    ad=input('Delivery Address : ')
    productid=random.randint(1000,10000)
    myuserdict['mobilenum']=mb
    myuserdict['address']=ad
    myuserdict['productid']=productid
    print('Enter 1 for cash and 2 for emi')
    payment=int(input())
    if payment==1:
        myuserdict['amount']=amt
    else:
        print('Your EMI starts from 6 months')
        safe=amt
        safe=safe//6
        print("Amount to be paid per month",safe)
        myuserdict['amount']=amt
    global idx
    idx=idx+1
    mydatabase[idx]=myuserdict
    print(mydatabase)
    f=open("electronicsdatabase.json","w")
    json.dump(mydatabase,f)
    f.close()
    
