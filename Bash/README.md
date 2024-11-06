# Process Files

* Linear Regression
* File processing (.txt format)

## Table of contents
* [General Info](#general-information)
* [How to run](#how-to-run)



## General Information
### Regr


| $$ sum_x = \sum_{i=0}^{length-1}X[i]$$        | $$sum_y = \sum_{i=0}^{length-1}Y[i]$$                                                                 | $$ sum_{xy} = \sum_{i=0}^{length-1}X[i]Y[i] $$  |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| $$sum_{x^2} = \sum_{i=0}^{length-1}(X[i])^2$$ | $$ a = \frac{length \cdot sum_{xy} - sum_x \cdot sum_y}{length \cdot sum_{x^2} - sum_x \cdot sum_x}$$ | $$ b = \frac{ sum_{y}-a \cdot sum_x }{length}$$ |
|                                               | $$ err = \sum_{i=0}^{length-1}(Y[i] - (aX[i]+b))^2$$                                                  |                                                 |

Calculate the linear regression parameters that minimize the total square err error of the approach 
* Accepts as program parameters a list of files. 
* Each file contains at least 3 lines.
* The data are numbered from position 0
* The cases of vertical and horizontal vectors are also taken into account (test files 4h, 5h)

#### Input format
```
num1:num2
``` 
where `num1 => X` <br> &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp; 
      `num2 => Y` <br>

Sample of a test file
```
10.7:15.6
5.6:20.5
3.5:15.4
2.4:10.3
1.3:6.2
8.2:10.1
9.1:25
```


#### Output format
In the general case, parameters and output are decimal numbers with 2 decimal digits. (if decimal places are needed)
```
FILE: input1, a=5.31 b=2.32 c=1 err=1340.32
FILE: input2, a=-2.31 b=1.23 c=1 err=13.25
FILE: input3, a=0 b=3 c=1 err=0
```
where `input1 => file name #1` etc <br>
<br><br><br><br><br>




### Results
Calculate scores of teams and points. The teams must be ordered based on scores.
In tie, ascending order to name.
A win gives 3 points, a win gives 3 points, the tie gives 1 point and a loss gives 0 points.


#### Input format
> Team1-Team2: Score1-Score2
```
Portugal-Greece:1-2
Greece-Spain:2-1
```

#### Output format
```
1.    Portugal  6 3-2
2.    Greece  4 4-4
3.    Spain 4 2-2
```


<br><br><br><br>


## How to run
### Linux
1. Open terminal and create a Bash file
```
$ touch regr.sh
$ touch results.sh
```

2. Open your script and add the following commands
```
#!/bin/bash
```
3. Save and close

4. Set executable permissions
```
$ chmod u+x regr.sh
$ chmod u+x results.sh
```
5. Run executable scripts
```
$ ./regr.sh
$ ./results.sh
```
or 
```
$ bash regr.sh
$ bash results.sh
```
or
```
$ sh regr.sh
$ sh results.sh
```

6. Make sure you include the required parameters for execution to each file
```
./regr 1h 2h 3h 4h 5h 6h
./results <test file>.txt
```

### Windows 
Tested on Pycharm IDE using bash
1. Install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) shell
2. On PyCharm
```File->Settings->Tools->Terminal```
3. Change shell on application settings to `bash.exe`
4. Execute on terminal
```
./regr <test file 1> <test file 2> <test file 3>
./results <test>.txt
```
```
where <test file 1> => 1h etc
      <test> => test1.txt

```
