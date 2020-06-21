# [OOPs-in-Python](https://github.com/Ankit-Khule/OOPs-in-Python/blob/master/oops.py)
Object oriented programming in pythons

* One of the ways of solving programming problems is by creating objects.
* In python objects has two characteristics 
  * attributes - features of the objects
  * behaviour - functions of the objects
  
 * Object consist of Class. Class is a blueprint of the object defined.
![class](https://github.com/Ankit-Khule/OOPs-in-Python/blob/master/images/oops.JPG)

> * Here we have created class animal.
> * animalcount is a class variable. It can be used inside and outside the class as an attribute
> * It consist of instance attributes, means which are created on the go and not predefined.
> * A function sound is defined under the class,which is method used by the object or behaviour of the object. 
> * **\_\_init\_\_** is a constructor to create the instances for the particular class
 
## Built in class attributes
  * __dict__ − Dictionary which contains the class's namespace.
  * __doc__ − Documentation string inside the class. if undefined it returns none.
  * __name__ − Retuns Class name.
  * __module__ − Returns Module name in which the class is defined. The attribute is "__main__" in interactive mode.
  * __bases__ − Retuns the base classes, in the order of their occurrence in the base class list.
  
  ![builtin](https://github.com/Ankit-Khule/OOPs-in-Python/blob/master/images/builtin%20oops.JPG)


## Inheritance
* Inhertance is acquiring attributes and methods from another class.
* class subclass(parent class) -->all the attributes of the parent class is inherited by the subclass.
![Inheritance](https://github.com/Ankit-Khule/OOPs-in-Python/blob/master/images/basicinheritance.JPG)

* if child class doesn't have a \_\_init\_\_ of its own it will inherit it from parent. if the constructor is present it will overide the constructor of parent class
![Inheritanceinit](https://github.com/Ankit-Khule/OOPs-in-Python/blob/master/images/initoverride.JPG)

* super() --> the function is used to inherit the attributes and methods from parent class even if subclass consist of init method to overide it.
![super](https://github.com/Ankit-Khule/OOPs-in-Python/blob/master/images/super.JPG)

## Types of Inheritance
 * Single Inheritance - One parent --> one child
![Single](https://github.com/Ankit-Khule/Functions/blob/master/images/singlelevel.JPG)

 * Multilevel Inheritance - Parent--> sub Parent-->child
 ![Multilevel](https://github.com/Ankit-Khule/Functions/blob/master/images/Mutlilevel.JPG)
 
 * Multiple Inheritance - Two parents --> one child
 ![Multiple](https://github.com/Ankit-Khule/Functions/blob/master/images/mutiple.JPG)
 
 * Hierarchical Inheritance - One parent--> two child
 ![hierarchical](https://github.com/Ankit-Khule/Functions/blob/master/images/Hierarchical.JPG)
 
 * Hybrid Inheritance - two or more types of inheritance.
![Hybrid](https://github.com/Ankit-Khule/Functions/blob/master/images/Hybrid.JPG)

## Encapsulation
* Protecting attributes and methods inside the class to be used outside the class
![Encapsulation](https://github.com/Ankit-Khule/Functions/blob/master/images/Encapsulation.JPG)

Here you can see if i am directly calling the parent attribute it is not accessible. It throws an attribute error. But when i call it from the child class which consist of parent class method. the value is accesible.

## Method Overriding
* Creating similar method in the child class with respect to parent class, overrides the method of parent class. Means it will replace the method of parent class and execute its own method
![Method](https://github.com/Ankit-Khule/Functions/blob/master/images/Methodoverriding.JPG)
