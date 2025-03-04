# Calculator

A simple calculator to perform basic arithmetic operations.

## Description

Set initial value Calculator(n), default 0 if None.<br>
Reset value .reset(n), default 0 if None.<br>
Performs addition, subtraction, multiplication, division and root extraction
### Installing

pip install git+https://github.com/Rauzis/Calculator.git

### Classifiers

Operating System : OS Independent
Programming Language : Python : 3

### Executing program

* ```from calculator import Calculator```
 Assign value
* ```calc = Calculator(n)```
```
.add(n) #n defaults to current memory value if None
.sub(n) #n defaults to current memory value if None
.multi(n) #n defaults to current memory value if None
.div(n) #n defaults to current memory value if None, cannot be zero
.root(n) #n defaults to 2 if None, cannot extract root from negative numbers
```

## Authors

Gytis Razokas

Discord: Rauzi#2378

## Version History

* 0.1
    * Initial Release

## License

[MIT]
