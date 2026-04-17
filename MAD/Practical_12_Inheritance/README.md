# Practical 12: Inheritance

## Passing Down Abilities
Instead of writing the exact same code twice, we use **Inheritance**. It works just like adopting traits from a parent. You might inherit your mother's eye color and your father's height.

In programming, let's say we wrote a bunch of complicated code for a `Camera` on how to focus lenses and take photos. 

Now, we want to create a `Smartphone`. A smartphone *has* a camera feature inside it. Instead of re-writing all that complicated photo-taking code from scratch, our `Smartphone` simply **extends** (inherits from) the `Camera` class!

Instantly, without writing a single line of photo-taking code inside the `Smartphone` class, it already knows exactly how to shoot photos! It "adopted" the ability from the parent `Camera`, while remaining free to also create its own new abilities, like making phone calls. Inheritance saves us massive amounts of time.
