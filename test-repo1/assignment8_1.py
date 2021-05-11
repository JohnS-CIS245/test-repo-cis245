'''
Assignment 8.1
CIS245-T302-T801
May 5, 2021
'''
#It took a lot more code than I may have needed, but I got it to work. 
'''
This week we will work with classes by creating a virtual garage. 

Your program will use the inheritance diagram from this week in order to create a parent class and two child classes.

Your program will prompt the user to create at least one object of each type (Car and Pickup). 

Using a menu system and capturing user input your program will allow the user the choice of adding a car or pickup truck and define the vehicle's attributes. 
The program will use user input to define the vehicle's attributes.

The options attribute in the parent class must be a python list containing a minimum of eight (8) options common to all vehicles. (i.e. power mirrors, 
power locks, remote start, backup camera, bluetooth, cruise control, etc).

The user will choose from a list of options to add to the vehicle's options list and can must choose a minimum of one vehicle option per vehicle. 
When the user is finished adding vehicles to their virtual garage the program will output the vehicles in their garage and their attributes.

Week 6 Class Diagram:

VehicleClass

The following information provides students with a breakdown of how this assignment will be assessed.

1. Object Oriented Programming and Inheritance - 30%
Create a Vehicle class with the attributes and functions detailed in the class diagram. - 10%
Create a Car class as a child of the Vehicle class with the attributes and functions detailed in the class diagram. - 10%
Create a Pickup class as a child of the Vehicle class with the attributes and functions detailed in the class diagram. - 10%
2. Demonstrate usage of previously studied programming constructs (functions, conditionals, loops)  - 60%
Using a function, display a menu prompting the user to add a Car or a Pickup to their virtual garage. - 15%

Your program will prompt the user to define the attributes of the vehicles in their garage. - 10%
The options attribute will be defined as a python list chosen by the user when presented with a menu of programmer chosen vehicle options that can apply to 
both cars and pickup trucks (i.e. power mirrors, power locks, remote start, backup camera, bluetooth, cruise control, etc) - 20%
3. When the user has finisheYour program must allow the user to have multiple vehicles in their virtual garage and must have at least one Car and one Pickup. - 15 %d adding and defining vehicles for their garage the program will output the vehicles with their accompanying attributes 
and options as specified by the user. -10 %
'''
#Your program will use the inheritance diagram from this week in order to create a parent class and two child classes.
#Create a Vehicle class with the attributes and functions detailed in the class diagram. - 10%
class Vehicle:
#Parent Class with options attribute

    #The options attribute in the parent class must be a python list containing a minimum of eight (8) options common to all vehicles. (i.e. power mirrors, 
    #power locks, remote start, backup camera, bluetooth, cruise control, etc).
    availableoptions = ["power windows", "power locks", "tilt steering", "cruise control", "power mirrors", "power seats", "remote start", "backup camera", "bluetooth"]
    #List of available options to take from for user choices

    def __init__(self,vehicletype,year,make,model,color,fueltype,vehicleoptions) :
        #Initialize attributes of the parent class
        self.vehicletype = vehicletype
        self.year = year
        self.make = make
        self.model = model 
        self.color = color 
        self.fueltype = fueltype
        self.options = vehicleoptions [:]

    def GetVehicletype(self):
        return self.vehicletype

    def getYear(self):
        return self.year

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getFueltype(self):
        return self.fueltype

    def getOptions(self):
        return self.options

#Create a Car class as a child of the Vehicle class with the attributes and functions detailed in the class diagram. - 10%
class Car (Vehicle):
    #Child class Car, Parent is Vehicle
    def __init__(self,vehicletype,year,make,model,color,fueltype,vehicleoptions,enginesize,numberofdoors,) :
        super().__init__(vehicletype,year,make,model,color,fueltype,vehicleoptions)
        self.enginesize = enginesize
        self.numberofdoors = numberofdoors

    def getEnginesize(self):
        return self.enginesize

    def getNumberofdoors(self):
        return self.numberofdoors

    
#Create a Pickup class as a child of the Vehicle class with the attributes and functions detailed in the class diagram. - 10%
class Pickup (Vehicle):
    #Child class Pickup, Parent is Vehicle
    def __init__(self,vehicletype,year,make,model,color,fueltype,vehicleoptions,cabstyle,bedlength,twoorfour,) :
        super().__init__(vehicletype,year,make,model,color,fueltype,vehicleoptions)
        self.cabstyle = cabstyle
        self.bedlength = bedlength
        self.twoorfour = twoorfour

    def getCabstyle(self):
        return self.cabstyle

    def getBedlength(self):
        return self.bedlength 

    def getTwoorfour(self):
        return self.twoorfour


    
#Using a function, display a menu prompting the user to add a Car or a Pickup to their virtual garage. - 15%
def vehiclechoicemenu (carcount,truckcount):
    #vehicle choice menu function to accept user input of what kind of vehicle they wish to add
    vehicle_type = 0
    while vehicle_type != 3 :

        vehicle_type = int(input("\nPlease choose a vehicle type to add to your garage :\n1) Pickup\n2) Car\n3) Quit\nType '1' or '2' or '3' : "))
        #When the user has finished, Your program must allow the user to have multiple vehicles in their virtual garage and must have at least one Car and one Pickup. - 15%
        #Your program will prompt the user to create at least one object of each type (Car and Pickup).
        if vehicle_type == 3 :
            if carcount < 1 or truckcount < 1 :
                vehicle_type = 0
                vehicle_type = int(input("You must enter at least one truck and one car to finish your garage.\nPlease type '3' to quit or any other NUMBER to continue : "))
                if vehicle_type != 3 :
                    continue
                elif vehicle_type == 3 :
                    exit()
            else :
                break
        elif vehicle_type == 2 or vehicle_type == 1 :
            return vehicle_type
                    
        else :
            print ("\nInvalid entry, please try again.\n")
            continue
        #If, if-elif, else statements to make sure user has 1 truck and 1 car in garage before quitting.  Also option to exit program with no output.


#Your program will prompt the user to define the attributes of the vehicles in their garage. - 10%
#Using a menu system and capturing user input your program will allow the user the choice of adding a car or pickup truck and define the vehicle's attributes. 
#The program will use user input to define the vehicle's attributes.
def vehicleinformation(vehicle_type) :
    #Vehicle information function takes the vehicle year, make, model
    
    vehicleyear = input(f"\nWhat year is your {vehicle_type} you are adding to your garage? ")
    vehiclemake= input(f"\nWhat is the make of your {vehicle_type}? ")
    vehiclemodel = input(f"\nWhat model is your {vehiclemake.title()}? ")
    color = input(f"\nWhat color is your {vehiclemake.title()}? ")
    fueltype = input(f"\nWhat type of fuel is does your {vehiclemake.title()} use? Gas or Diesel? ")

    return vehicleyear, vehiclemake, vehiclemodel, color, fueltype


#The options attribute will be defined as a python list chosen by the user when presented with a menu of programmer chosen vehicle options that can apply to 
#both cars and pickup trucks (i.e. power mirrors, power locks, remote start, backup camera, bluetooth, cruise control, etc) - 20%
def vehicleoptionsmenu(vehicleyear, vehiclemake, vehiclemodel) :
    #vehicleoptionsmenu function takes user input via a menu of options from the list provided in Vehicle Class

    optionchoice = "0"
    vehicleoptions = []
    
    #The user will choose from a list of options to add to the vehicle's options list and can must choose a minimum of one vehicle option per vehicle. 
    while optionchoice != 10 :
        counter = 0
        optionchoice = 0
        print (f"\nPlease choose which option you would like to add to your {vehicleyear} {vehiclemake.title()} {vehiclemodel.title()} :")
        for option in Vehicle.availableoptions : 
            print (f"{counter}) {option.title()}")
            counter += 1
        print ("10) I am done with options.")
        optionchoice = int(input("Please choose which option to add to your vehicle : "))
        if optionchoice == 10 :
            if vehicleoptions == [] : 
                print ("You MUST choose at least ONE option for this vehicle!")
                optionchoice = 0
                continue
            elif vehicleoptions != [] :
                break
        vehicleoptions.append(Vehicle.availableoptions[optionchoice])
        
        #if, if-elif statements make sure the user chooses at least 1 option
    return vehicleoptions


def caroptions():
    #car options function takes information information specific to cars

    enginesize = input(f"\nWhat size engine does your car have? ")
    numberofdoors = input(f"\nHow many doors does your car have? ")

    return enginesize, numberofdoors

        
def truckoptions():
    #truck options function takes information specific to a truck from user

    cabstyle = 0
    bedlength = 0
    twoorfour = 0

    while cabstyle != 1 or cabstyle != 2 or cabstyle != 3:
        cabstyle = int(input("\nWhat size cab does your truck have?\n1) Standard\n2) Extended\n3) Crew\nType '1', '2', or '3' : "))
        if cabstyle == 1 :
            cabstyle = "standard cab"
            break
        elif cabstyle == 2 :
            cabstyle = "extended cab"
            break
        elif cabstyle == 3 :
            cabstyle = "crew cab"
            break
        else :
            print ("\nPlease enter either '1','2', or '3'.\n")
            continue
    #while loop to make sure user answers in the format given

    while bedlength != 1 or bedlength != 2 :
        bedlength = int(input("\nWhat size bed does your truck have?\n1) Short\n2) Long\nType '1' or '2' : "))
        if bedlength == 1 :
            bedlength = "short bed"
            break
        elif bedlength == 2 :
            bedlength = "long bed"
            break
        else :
            print ("\nPlease enter either '1' or '2'.\n")
            continue
    #while loop to make sure user answers in the format given

    while twoorfour != 1 or twoorfour != 2 :
        twoorfour = int(input("\nIs your truck 2-wheel drive or 4-wheel drive?\n1) Two Wheel Drive\n2) Four Wheel Drive\nType '1' or '2' : "))
        if twoorfour == 1 :
            twoorfour = "two wheel drive"
            break
        elif twoorfour == 2 :
            twoorfour = "four wheel drive"
            break
        else :
            print ("\nPlease enter either '1' or '2'.\n")
            continue
    #while loop to make sure user answers in the format given
    
    return cabstyle,bedlength,twoorfour

#adding and defining vehicles for their garage the program will output the vehicles with their accompanying attributes 
    #and options as specified by the user. -10 %

def vehicleprintout(garage):
    #Function for printout of vehicles
    
    for v in garage : #For loop to loop through vehicles in garage collection
        if v.vehicletype == "truck" :
            print (f"\nYour garage has a {v.getYear()} {v.getMake().title()} {v.getModel().title()} in it! The color is {v.getColor().lower()}.")
            print (f"Your truck has a {v.getCabstyle()} and {v.getBedlength()}. It is {v.getTwoorfour()}.")
            print (f"Your truck runs on {v.getFueltype()}.")
            print (f"The {v.getYear()} {v.getMake().title()} {v.getModel().title()} has the options of : ")
            for option in v.getOptions() :
                print (option.title())
            continuetrucks = input("\nPress enter to see the next vehicle...")
        elif v.vehicletype == "car" :
            print (f"\nYour garage has a {v.getYear()} {v.getMake().title()} {v.getModel().title()} in it! The color is {v.getColor().lower()}.")
            print (f"Your car has a {v.getEnginesize()} engine and is a {v.getNumberofdoors()} door model.")
            print (f"Your car runs on {v.getFueltype()}.")
            print (f"The {v.getModel()} has the options of : ")
            for option in v.getOptions() :
                print (option.title())
            continuecars = input("\nPress enter to see the next vehicle...")
    


def main():
    #Main function makes the calls on all other functions to make the program function as it should

    garage = []
    carcount = 0
    truckcount = 0
    vehiclechoice = 0

    while vehiclechoice != 3 :

        vehiclechoice = vehiclechoicemenu(carcount,truckcount)
        if vehiclechoice == 1 :
            vehicletype = "truck"
            year, make, model, color, fueltype = vehicleinformation(vehicletype)
            vehicleoptions = vehicleoptionsmenu(year,make,model)
            cabstyle, bedlength, twoorfour = truckoptions()
            garage.append(Pickup(vehicletype,year,make,model,color,fueltype,vehicleoptions,cabstyle,bedlength,twoorfour))
            truckcount += 1
        #If statement to handle if the user chooses a truck or a car

        elif vehiclechoice == 2 :
            vehicletype = "car"
            year, make, model, color, fueltype = vehicleinformation(vehicletype)
            vehicleoptions = vehicleoptionsmenu(year,make,model)
            enginesize, numberofdoors = caroptions()
            garage.append(Car(vehicletype,year,make,model,color,fueltype,vehicleoptions,enginesize,numberofdoors))
            carcount +=1
        #If statement to handle if the user chooses a truck or a car

        else :
            break
    #while loop continues taking vehicle information until the user chooses to quit

    #When the user is finished adding vehicles to their virtual garage the program will output the vehicles in their garage and their attributes.
    vehicleprintout(garage)
    #call vehicleprintout with the objects to print all information for each vehicle
    
    exit()
    #exit program when finished
            

main()
#call main function to do all the work