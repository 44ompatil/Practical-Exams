# Practical 10: Constructor

## The Setup Crew
In the last practical, we built a car box, and then manually went inside and assigned the color and the brand one by one. This works, but it's slow.

A **Constructor** is a special feature inside a class. Imagine going to buy a new computer from Apple. You don't take it home, order the parts separately, and hand-screw the RAM into the motherboard. Apple "Constructs" it for you based on the options you choose before taking it out of the box.

In our code, `Person(this.name, this.age);` is the constructor. The split second the `Person` is born into our program, it requires that you hand it a name and an age right away! 

When we say `Person("David", 30)`, the constructor catches "David" and 30, and instantly wires them up inside the newly created Object for us. It guarantees that our objects are born "fully setup" and ready to use!
