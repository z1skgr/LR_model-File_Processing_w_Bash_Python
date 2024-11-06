# Python
> Program for processing input files in the format of receipts.

 
 ## Table of contents
* [General Info](#general-information)
* [Features](#features)
* [How to run](#how-to-run)

## General Information
`computeSales.py` reads `.txt` files, makes correctness check, and can print requested statistics.


### Text format: <br />


```
------------------- 
AFM:AAAAAAAA 
PRODUCT_NAME: QUANTITY UNIT_PRICE TOTAL_VALUE 
... 
PRODUCT_NAME: QUANTITY UNIT_PRICE TOTAL_VALUE 
TOTAL: TOTAL VALUE 
-------------------- 
AFM:AAAAAAAB 
PRODUCT_NAME: QUANTITY UNIT_PRICE TOTAL_VALUE 
... 
PRODUCT_NAME: QUANTITY UNIT_PRICE TOTAL_VALUE 
TOTAL: TOTAL VALUE 
-------------------- 
```

A sample of a good receipt
```
--------------------------
ΑΦΜ: 0123456789
ΧΩΡΙΑΤΙΚΗ: 2   5.50    11.00
ΚΡΕΑΤΑ:   4   12.25    49.00
ΚΡΑΣΙ:    2   3.50      7.00
ΣΥΝΟΛΟ: 67.00
--------------------------
ΑΦΜ: 0123456780
ΧΩΡΙΑΤΙΚΗ: 2   2.00    4.00
ΚΡΕΑΤΑ:   4   12.00    48.00
ΣΥΝΟΛΟ: 52.00
--------------------------
```


## Features
### .TXT files [^1]:
1. 1 or more receipts in file(but at least 1)
2. Begins/Ends with lines containing the ‘-’ character.
3. Separated by lines containing the ‘-’ character.
4. First line contains the AFM number(10-digit number).
5. Last line contains the total purchases.
6. There can be receipts of different companies (AFM).
7. Receipts of multiple products (1 or more).
8. Reappearance of a product in a receipt. [^2]
9. No problem with space characters in receipts
10. Error in receipt => receipt ignored
                     => file preserved

### Program
Prints the following user menu repeatedly[^3]:
1. Read input file[^4]. 
2. Print statistics for a specific product.
3. Print statistics for a specific AFM. 




## How to run
* In Linux
1. Refresh repository lists
```
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
```
2. Install latest versions of python
```
$ sudo apt-get install python3.8
```
3. Verify installation and compile
```
$ python3.8
$ python3.8 computeSales.py
```
* In any python IDE
1. Install Python packages from website
```
 https://www.python.org/downloads/ 
 ```
 and choose version [^5]
 
 2. Install Pycharm (or any Python Platform you are familiar with)
 3. Import project to PyCharm workspace
 4. Make sure you have python interpreter detected (or install it)
 5. Run your `computeSales.py`
 
 
 





[^1]: Every input file satisfies constraints about numerical values and format it sustains.
[^2]: In the proof, the product XORIATIKI may appear again later in the same proof.
[^3]: There must be data in order to be able to be read (or input files).
[^4]: The program works for a non-specific archive length.
[^5]: Make sure you include python version as PATH variable. Select it on installation process
