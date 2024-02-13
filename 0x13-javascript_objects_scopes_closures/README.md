# 0x13. JavaScript - Objects, Scopes and Closures

This project is part of the Holberton School curriculum on JavaScript. It covers the topics of objects, scopes, and closures in JavaScript.

## Learning Objectives

By the end of this project, you should be able to:

- Create and use objects, prototypes, and inheritance in JavaScript
- Understand and use scopes and closures in JavaScript
- Write JavaScript code that follows the Airbnb style guide and passes the semistandard linter
- Test your code using the checker tool

## Requirements

- All your files should have the extension `.js`
- You are not allowed to use `var`
- You are not allowed to use the `this` keyword
- You are not allowed to use `import` or `require`
- You are not allowed to use `class`
- You are not allowed to use `try/catch/finally`
- You are not allowed to use `async/await`
- You are not allowed to use `for/in` or `for/of`
- You are not allowed to use `continue` or `break`
- You are not allowed to use `console.log` or `alert`
- You are not allowed to use `Math.random`

## Tasks

0. Rectangle #0
Write an empty class `Rectangle` that defines a rectangle.

1. Rectangle #1
Write a class `Rectangle` that defines a rectangle. The constructor should take two arguments: `width` and `height`. If either argument is not a positive integer, create an empty object.

2. Rectangle #2
Write a class `Rectangle` that defines a rectangle. The constructor should take two arguments: `width` and `height`. If either argument is not a positive integer, create an empty object. The class should have an instance method called `print()` that prints the rectangle using the character `X`.

3. Rectangle #3
Write a class `Rectangle` that defines a rectangle. The constructor should take two arguments: `width` and `height`. If either argument is not a positive integer, create an empty object. The class should have an instance method called `print()` that prints the rectangle using the character `X`. The class should also have a static method called `rotate()` that exchanges the `width` and the `height` of the rectangle. The class should also have a static method called `double()` that multiplies the `width` and the `height` of the rectangle by 2.

4. Square #0
Write a class `Square` that defines a square and inherits from `Rectangle` of `0-rectangle.js`. The constructor should take one argument: `size`. If `size` is not a positive integer, create an empty object. The `width` and `height` of the square should be equal to `size`.

5. Square #1
Write a class `Square` that defines a square and inherits from `Rectangle` of `0-rectangle.js`. The constructor should take one argument: `size`. If `size` is not a positive integer, create an empty object. The `width` and `height` of the square should be equal to `size`. The class should have an instance method called `charPrint(c)` that prints the square using the character `c`. If `c` is undefined, use the character `X`.

6. Singly linked list
Write a class `Node` that represents a node of a singly linked list. The constructor should take one argument: `data`. The class should have two instance attributes: `data` and `next`. The `data` attribute should store the value of the node. The `next` attribute should store the reference to the next node or `null` if it is the last node. The class should also have a `toString()` method that returns the string representation of the node.

Write a class `LinkedList` that represents a singly linked list. The constructor should take no arguments and initialize an empty list. The class should have an instance attribute called `head` that stores the reference to the first node or `null` if the list is empty. The class should have an instance method called `add(data)` that adds a new node at the end of the list with the given `data`. The class should also have a `toString()` method that returns the string representation of the list.

7. Queue
Write a class `Queue` that defines a queue and uses a `Node` class from `6-linked_list.js`. The constructor should take no arguments and initialize an empty queue. The class should have an instance attribute called `head` that stores the reference to the first node or `null` if the queue is empty. The class should also have an instance attribute called `tail` that stores the reference to the last node or `null` if the queue is empty. The class should have an instance method called `enqueue(data)` that adds a new node at the end of the queue with the given `data`. The class should also have an instance method called `dequeue()` that removes and returns the first node of the queue or `null` if the queue is empty. The class should also have an instance method called `isEmpty()` that returns `true` if the queue is empty or `false` otherwise.

8. Stack
Write a class `Stack` that defines a stack and uses a `Node` class from `6-linked_list.js`. The constructor should take no arguments and initialize an empty stack. The class should have an instance attribute called `head` that stores the reference to the first node or `null` if the stack is empty. The class should have an instance method called `push(data)` that adds a new node at the beginning of the stack with the given `data`. The class should also have an instance method called `pop()` that removes and returns the first node of the stack or `null` if the stack is empty. The class should also have an instance method called `isEmpty()` that returns `true` if the stack is empty or `false` otherwise.

9. Prime numbers & timing execution
Write a function `countPrimeNumbers()` that returns the number of prime numbers from 2 to 100. A prime number is a natural number that has exactly two distinct natural number divisors: 1 and itself.

Write a script that measures the execution time of `countPrimeNumbers()` and prints it in the console. Use the `performance` API to measure the time.

10. Factorial & timing execution
Write a function `factorial(n)` that returns the factorial of a positive integer `n`. The factorial of `n` is the product of all positive integers less than or equal to `n`. If `n` is not a positive integer, return `null`.

Write a script that measures the execution time of `factorial(5)` and prints it in the console. Use the `performance` API to measure the time.

11. Execution stack & timing execution
Write a function `log(str)` that prints a string `str` in the console.

Write a function `me()` that calls `log("Hello...")` and then `log("Me")`.

Write a function `you()` that calls `log("Hello...")` and then `log("You")`.

Write a script that measures the execution time of `me()` and `you()` and prints it in the console. Use the `performance` API to measure the time.

12. Binding
Write a function `welcomeMessage(fullName)` that takes one argument `fullName` and returns a function that alerts `Welcome <fullName>`.

Write three constants: `guillaume`, `alex`, and `fred`. Each constant should be initialized to a function that is the result of calling `welcomeMessage()` with the respective full name.

13. Simple callback
Write a function `isPrime(number)` that checks if a number is prime or not. A prime number is a natural number that has exactly two distinct natural number divisors: 1 and itself. If `number` is not a positive integer, return `false`.

Write a function `processArray(array, callback)` that takes an array of numbers and a function as arguments and returns a new array with each element processed by the function. If the function cannot be applied to an element, return the element as is.

14. Complex callback
Write a function `createMacroProcessor()` that returns an object with a property called `process(str, callback)` that takes a string `str` and a function `callback` as arguments and returns a new string with each word that starts with `+` processed by the callback. If the callback cannot be applied to a word, return the word as is.

Write a function `increment(n)` that takes a string `n` and returns the string representation of the next natural number. If `n` is not a natural number, return `null`.

Write a function `upperCase(str)` that takes a string `str` and returns the upper case version of the string. If `str` is not a string, return `null`.

Write a script that creates a macro processor using `createMacroProcessor()` and uses it to process the string `+2 eggs +1 bread +4 butter` with the functions `increment()` and `upperCase()`. The script should print the result in the console.
