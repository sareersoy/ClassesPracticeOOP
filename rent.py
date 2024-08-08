import datetime

#parent class

class VehicleRent:
    
    def __init__(self,stock):
        self.stock = stock
        self.now = 0
    
    def displayStock(self):
        print("{} vehicle available to rent".format(self.stock))
        return self.stock
    
    
    def rentHourly(self, n):
        if n <= 0:
            print("number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicle available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle for hourly at {} hours".format(n,self.now.hour))
            
            self.stock -= n
            return self.now
    
    def rentDaily(self, n):
        if n <= 0:
            print("number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicle available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle for daily at {} hours".format(n,self.now.hour))
             
            self.stock -= n
            return self.now
    
    def returnVehicle(self,request,brand):
       car_h__price = 10
       car_d_price = car_h__price*8/10*24
       bike_h_price = 5
       bike=d=price = bike_h_price*7/10*24
       
       rentalTime, rentalBasis, numberOfVehicle = request
       bill = 0
       
       
       if brand == "car":
           if rentalTime and rentalBasis and numberOfVehicle:
               self.stock += numberOfVehicle
               now = datetime.datetime.now()
               rentalPeriod = now - rentalTime
               
               if rentalBasis == 1:
                   bill = rentalPeriod.seconds/3600*car_h__price*numberOfVehicle
                   
               elif rentalBasis == 2:
                   bill = rentalPeriod.seconds/(3600*24)*car_d_price*numberOfVehicle
                   
               if(2<= numberOfVehicle):
                   print("You have extra 20% discount")
                   bill = bill*0.8
               print("Thank you for returning your vehicle")
               print("Price: $ {}".format(bill))
               
               
               
           
       elif brand == "bike":
           if rentalTime and rentalBasis and numberOfVehicle:
               self.stock += numberOfVehicle
               now = datetime.datetime.now()
               rentalPeriod = now - rentalTime
               
               if rentalBasis == 1:
                   bill = rentalPeriod.seconds/3600*bike_h__price*numberOfVehicle
                   
               elif rentalBasis == 2:
                   bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numberOfVehicle
                   
               if(4<= numberOfVehicle):
                   print("You have extra 20% discount")
                   bill = bill*0.8
               print("Thank you for returning your vehicle")
               print("Price: $ {}".format(bill))
               
       else:
           print("You do not rent a vehicle")
           return None
    
#childclass

class carRent(VehicleRent):
    
    global discount_rate
    discount_rate = 15
    
    
    def __init__(self,stock):
        super().__init__(stock)
        
    
    def discount(self,b):
        bill = b - (b*discount_rate)/100
        return bill
    
#child class 2

class bikeRent(VehicleRent):
    
    def __init__(self,stock):
        super().__init__(stock)
        
        
    

#customer 
class Customer:
    def __init__(self):
        self.bikes = 0
        self.cars = 0
        
        
        self.rentalBasis_b = 0
        self.rentalBasis_c = 0
        
        
        self.rentalTime_b = 0
        self.rentalTime_c = 0
    
    def requestVehicle(self,brand):
            if brand == "bike":
                try:
                    bikes = int(input("How many bikes would you like to rent"))
                except ValueError:
                    print("Entered value should be a number")
                    return -1
                
                if bikes <1:
                    print("Number of Bikes sgould be greater than 0")
                else:
                    self.bikes = bikes
                    return self.bikes
                
            elif brand == "car":
                try:
                    cars = int(input("How many cars would you like to rent"))
                except ValueError:
                    print("Entered value should be a number")
                    return -1
                
                if cars <1:
                    print("Number of cars sgould be greater than 0")
                else:
                    self.cars = cars
                    return self.cars
                
                
                
            else:
                print("Request vehicle error")
    
    def returnVehicle(self, brand):
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b , self.rentalBasis_b , self.bikes
            else:
                return 0,0,0
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c , self.rentalBasis_c , self.cars
            else:
                return 0,0,0
            
            
        else:
            print("Request vehicle error")
            
            
            
            
            
            