                        ####Object Oriented Programming####


#defining class animal

class animal:
    "Contains animal information of age name and type"
    #instance attributes
    def __init__(self,name,age,types):
        self.name=name
        self.age=age
        self.types=types
    
    #method in class
    def sound(self):
        if self.types=="Cat":
            print("Meow")
        elif self.types=="Dog":
            print("bark")
        else:
            print("No such animal found")

#create objects dog and cat
dog=animal("Draco",10,"Dog")
cat=animal("mcgonnel",15,"Cat")


#accessing Attributes
print("The animal is ",dog.types,"\nHis name is ",dog.name,"\nits age is ",dog.age)
print("The animal is ",cat.types,"\nHer name is ",cat.name,"\nits age is ",cat.age)


#call the method of class animal
cat.sound()
dog.sound()


#Built-In Class Attributes

print("animal.__doc__:", animal.__doc__)
print("animal.__name__:", animal.__name__)
print("animal.__module__:", animal.__module__)
print("animal.__bases__:", animal.__bases__)
print("animal.__dict__:", animal.__dict__)


####Inheritance

class birds(animal):
    pass
sparrow=birds("phoenix",20,"bird")
print("The animal is ",sparrow.types,"\nHis name is ",sparrow.name,"\nits age is ",sparrow.age)

#overiding init of parent class
class birds(animal):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
sparrow=birds("phoenix",20)
print("The animal is ",sparrow.types,"\nHis name is ",sparrow.name,"\nits age is ",sparrow.age)


#super function
class birds(animal):
    def __init__(self,name,age,types):
        super().__init__(name,age,types)
    
sparrow=birds("phoenix",20,"bird")
print("The animal is ",sparrow.types,"\nHis name is ",sparrow.name,"\nits age is ",sparrow.age)


#single level inheritance
class parent:
    parent1="anderson"
    
    def __init__(self,name,age,lastname):
        self.name=name
        self.age=age
        self.lastname=lastname
        
class child(parent):
    pass

child1=child("dan",20,child.parent1)

print("Child's Name: ",child1.name,"\nChild's age: ",child1.age,"\nChild's Lastname: ",child1.lastname)



#Mutliple inheritance
class parent1:
    parent1="anderson"
    
    def __init__(self,name,age,lastname):
        self.name=name
        self.age=age
        self.lastname=lastname
        
class parent2:
    parent2="Meyers"
    
    def __init__(self,name,age,lastname):
        self.name=name
        self.age=age
        self.lastname=lastname
        
class child(parent1,parent2):
    pass

child1=child("dan",20,child.parent1)
child2=child("Tim",30,child.parent2)
print("1st Child Name: ",child1.name,"\n 1st Child's age: ",child1.age,"\n 1st Child's Lastname: ",child1.lastname)
print("2nd Child Name: ",child2.name,"\n 2nd Child's age: ",child1.age,"\n 2nd Child's Lastname: ",child1.lastname)


#Multilevel inheritance
class grandparent:
    grandparent="anderson"
    def __init__(self,name,age):
        self.name=name
        self.age=age
   
class parent(grandparent):
    parent="Dan"
    pass
     
class child(parent):
    pass
        

child=child("Tom",20)
print("Child Name: ",child.name,"\nChild's age: "
      ,child.age,"\nDad's Name: ",child.parent,"\nGrandDad's Name: ",child.grandparent)

#Hiearchical

class parent:
    parent="anderson"
    def __init__(self,name,age):
        self.name=name
        self.age=age
   
class child1(parent):
    pass

class child2(parent):
    pass
         

child1=child1("Tom",20)
child2=child2("Daenarys",20)
print("Son Name: ",child1.name,"\nSon's age: ",child1.age,"\nDaughter's Name: ",child2.name,"\nDaughter's age: ",child2.age,"\nFather's Name: ",child2.parent)




#Hybrid (Multilevel +Multiple)
class grandparent:
    grandparent="anderson"
    def __init__(self,name,age):
        self.name=name
        self.age=age
   
class parent1(grandparent):
    parent1="Dan"
    pass

class parent2:
    parent2="Tina"
    pass
         
class child(parent1,parent2):
    pass
        

child=child("Tom",20)
print("Child Name: ",child.name,"\nChild's age: ",child.age,"\nDad's Name: ",child.parent1,"\nMom's name: ",child.parent2,"\nGrandDad's Name: ",child.grandparent)


#method overriding

class Parent:
   def method1(self):
      print('Calling parent method')

class Child(Parent): 
   def method1(self):
      print('Calling child method')

c = Child()
c.method1()


####Encapsulation
class parent:
    def __init__(self):
        self._name="Dan"
         
class child(parent):
    def _init__(self):
        parent.__init__(self) #passing parent init method
        print(self._name)

object2=child() 
object1=child._name  #directly accessing the parent attribute through child.

print(object2._name) #accessing parent attribute through parent constructor present in child class