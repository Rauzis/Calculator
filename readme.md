# Calculator

A simple calculator to perform basic arithmetic operations.

## Description

Performs addition, subtraction, multiplication, division and root extraction

### Installing

Place calculator.py in folder it will be used in. <br>
Start it by importing ```from calculator import Calculator```<br>
Set initial value Calculator(n), default 0 if None.

### Classifiers

Operating System : OS Independent <br>
Programming Language : Python : 3

### Executing program

* ```from calculator import Calculator```<br>
 Assign value
* ```calc = Calculator(n)```
```
.add(n) #addition. n defaults to current memory value if None.
.sub(n) #subtraction. n defaults to current memory value if None.
.multi(n) #multiplication. n defaults to current memory value if None.
.div(n) #division. n defaults to current memory value if None, cannot divide by zero.
.root(n) #root extraction. n defaults to 2 if None, cannot extract root from negative numbers.
.reset(n) #memory reset. n defaults to 0 if None.
.memory() #returns calculator memory.
```

## Authors

Gytis Razokas

Discord: Rauzi#2378

## Version History

* 0.1
    * Initial Release

## License

[MIT]
