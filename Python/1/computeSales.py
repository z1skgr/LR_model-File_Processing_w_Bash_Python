from copy import deepcopy
# import time
import math
import sys

def menu():  # Menu implemented dictionary
    answer = 0
    menu_r = {
        0: "Give your preference:",
        1: "read new input file",
        2: "print statistics for a specific product",
        3: "print statistics for a specific AFM",
        4: "exit the program",
        5: "Your answer:",
    }
    # For each dictionary key the corresponding value is printed
    try:
        for key in menu_r:
            if key == 0:
                print(f"\n{menu_r[key]}")
                continue
            if key!=5:
                print(f"{key}: {menu_r[key]}")
            if key == 5:
                answer = int(input(f'{menu_r[key]}'))  # Answer of the user
            #  Answer return
        return answer
    except KeyboardInterrupt:
        print("\nUnexpected error:", sys.exc_info()[0])


def func_2(nm, dc):  #Arguments the option and the dictionary
    k_list = [n for (n, v) in dc.items() if nm.upper() in v]  # Check which internal dictionaries the product is in
    # None or more entries may be found
    if bool(k_list):  # Entries found from the product to customers
        for s in sorted(dc.items(), key=lambda k_v: k_v[1]['ΑΦΜ']):  # Sort based  ΑΦΜ
            for l in range(len(k_list)):
                if k_list[l] in s:
                    print(s[1]["ΑΦΜ"], end=" ")
                    # Sorted. If it exists in the k_list I display the VAT number and the amount
                    print("{:.2f}".format(s[1][nm.upper()]), end="€" + "\n")
                    break
                else:
                    pass
    else:  # Not found. do nothing
        pass


def func_3(nm, dc):  # #Arguments the VAT number and the dictionary
    k_list = [n for (n, v) in dc.items() if v['ΑΦΜ'] == nm]
    # None or more entries may be found
    if bool(k_list):
        # For the single entry sort by key
        for i, pp in sorted(dc.get(k_list[0]).items()):
            if "ΑΦΜ" == i:
                #  ΑΦM ignored
                pass
            else:
                print(i, "{:.2f}".format(pp), end="€" + "\n")
    else:
        pass


data = {}  # Variables
dt = {}
diction = {}
allaghlist = []
while True:
    ans: int
    try:
        ans = int(menu())  # Menu Function
    except ValueError:
        print("Please enter an integer\n")
    except TypeError:
        print("Unexpected error:", sys.exc_info()[0], end="\n")
        print("Forced Termination\n")
        break
    else:
        if ans == 1:
            f_name = input("Give filename:")  # File name
            check: int
            check = 0
            try:
                fp = open(f"examples/{f_name}", mode ='r', encoding='utf-8')  # FP for file opening
            except FileNotFoundError:
                print("File Not Found. Try again")
            except Exception as e:
                print(f"An error occurred while opening the file '{f_name}': {str(e)}")
                exit(1)
            else:
                print("-->Start Reading<--")
                # seconds = time.time()
                vat_list = []
                foodlist = []  # Variables
                food_priceList = []
                food_quantList = []
                total = 0
                total_flag = 0

                read_ln = fp.readline().strip('\n')  # Read line
                first = 0  # Auxiliary variables
                second = 0
                err_counter = 0  # Count Errors

                while read_ln:
                    vat_string = ""
                    if err_counter == 0 and second == 0:
                        print("ΛΑΘΗ:")
                        second = 1
                    else:
                        pass
                    if check == 1:  # Found (-), so expect the next line to contain the VAT number
                        if "ΑΦΜ" in read_ln:
                            check = 0  # We don't care about the VAT number from there on
                            for k in range((read_ln.find("ΑΦΜ")) + 3, len(read_ln)):  # Search for a 10-digit number
                                if read_ln[k].isdigit():  # Digits are kept
                                    vat_string = vat_string + read_ln[k]
                                    # Inappropriate characters are considered errors
                                elif ":" == read_ln[k] and (read_ln[k + 1 if k + 1 < len(read_ln) else k].isdigit()
                                                            or read_ln[k - 1].isdigit()):
                                    foodlist = []
                                    food_priceList = []
                                    food_quantList = []
                                    vat_list = []  # Each time an error occurs, new initializations
                                    total = 0
                                    total_flag = 0
                                    err_counter += 1  # Increase the error counter
                                    print(err_counter, ")Error problem#1 inside VAT number")
                                    print(read_ln)

                                    while True:
                                        read_ln = fp.readline().strip('\n')
                                        if '-' in read_ln:  # Search for the beginning of new receipt
                                            check = 1
                                            break
                                    break
                                elif " " == read_ln[k] or ":" == read_ln[k]:  # Spaces ignored
                                    pass
                                else:
                                    foodlist = []
                                    food_priceList = []
                                    food_quantList = []
                                    vat_list = []  # Each time an error occurs, new initializations
                                    total = 0
                                    total_flag = 0
                                    err_counter += 1  # Increase the error counter
                                    allaghlist.clear()
                                    print(err_counter, ")Error problem#2 inside VAT number")
                                    print(read_ln)
                                    while True:
                                        read_ln = fp.readline().strip('\n')
                                        if '-' in read_ln:  # Search for the beginning of new receipt
                                            check = 1
                                            break
                                    break
                            else:
                                if len(vat_string) != 10:  # Check the VAT number to be 10 digits
                                    foodlist = []
                                    food_priceList = []
                                    food_quantList = []
                                    vat_list = []
                                    total = 0
                                    total_flag = 0  # Each time an error occurs, new initializations
                                    err_counter += 1  # Increase the error counter
                                    allaghlist.clear()
                                    print(err_counter, ")Wrong VAT number.More or less digits")
                                    print(read_ln)
                                    while True:
                                        read_ln = fp.readline().strip('\n')
                                        if '-' in read_ln:  # Search for the beginning of new receipt
                                            check = 1
                                            break
                                else:
                                    vat_list.append("ΑΦΜ")  # Correct VAT number inserted to AFM list
                                    vat_list.append(vat_string)

                        else:
                            err_counter += 1  # Increase the error counter
                            print(err_counter, ")VAT number in wrong position")
                            print(read_ln)
                            foodlist = []
                            food_quantList = []
                            food_priceList = []
                            vat_list = []
                            total = 0  # Each time an error occurs, new initializations
                            total_flag = 0
                            allaghlist.clear()
                            while True:
                                read_ln = fp.readline().strip('\n')
                                if '-' in read_ln:  # Search for the beginning of new receipt
                                    check = 1
                                    total_flag = 0
                                    break
                    elif '-' in read_ln:
                        #  The first time is not a mistake that no symbol has been found. Check to the first
                        if total_flag == 0 and first == 1:
                            err_counter += 1  # Increase the error counter
                            print(err_counter, ")There is no total in the receipt")
                            foodlist = []
                            food_priceList = []  # Each time an error occurs, new initializations
                            food_quantList = []
                            vat_list = []
                            total = 0
                            allaghlist.clear()

                        total_flag = 0  # total_flag = 0 means that the field SYNOLΟ (total) has not yet been found
                        check = 1  # (-) means proof begins so check=1
                        first = 1
                        allaghlist.clear()
                    elif ':' in read_ln:  # (:) means PRODUCT(ΠΡΟΙΟΝ) or field TOTAL(ΣΥΝΟΛΟ)
                        if "ΣΥΝΟΛΟ" in read_ln:  # TOTAL(ΣΥΝΟΛΟ) found
                            if total_flag == 1:  # total_flag=1 means that the field TOTAL(ΣΥΝΟΛΟ) has been found again. Wrong
                                err_counter += 1  # Increase the error counter
                                print(err_counter, ")More totals found")
                                print(read_ln)  # Each time an error occurs, new initializations
                                foodlist = []
                                food_priceList = []
                                food_quantList = []
                                vat_list = []
                                total = 0
                                total_flag = 0
                                allaghlist.clear()
                                while True:
                                    read_ln = fp.readline().strip('\n')
                                    if '-' in read_ln:  # Search for the beginning of new receipt
                                        check = 1
                                        break
                            else:
                                total_flag = 1  # Otherwise it's the first time it was found
                                prices_list = []
                                num_str = ""
                                for k in range(read_ln.find('ΣΥΝΟΛΟ') + 7,
                                               len(read_ln)):  # Search the total in the file
                                    if read_ln[k] == ' ' or read_ln[k] == '\t':
                                        if "" != num_str:  # Space with a variable having a value, then it is listed
                                            prices_list.append(num_str)
                                            num_str = ""
                                        pass
                                    elif read_ln[k].isdigit() or (
                                            read_ln[k] == '.' and read_ln[k - 1].isdigit() and read_ln[k + 1].isdigit()):
                                        num_str = num_str + read_ln[k]  # The digits are reserved
                                    else:
                                        #  If a non-permitted character is found. Error
                                        err_counter += 1  # Increase the error counter
                                        print(err_counter, ')Something is wrong with the field TOTAL')
                                        print(read_ln)
                                        foodlist = []  # Each time an error occurs, new initializations
                                        food_priceList = []
                                        food_quantList = []
                                        vat_list = []
                                        total = 0
                                        total_flag = 0
                                        allaghlist.clear()
                                        while True:
                                            read_ln = fp.readline().strip('\n')
                                            if '-' in read_ln:  # Search for the beginning of new receipt
                                                check = 1
                                                break
                                        break
                                else:
                                    prices_list.append(num_str)  #  The price of the receipt was found
                                    dt = {}
                                    if len(prices_list) == 1:  # If a correct receipt has been found
                                        if float("{0:.2f}".format(total)) == float(prices_list[0]):
                                            # Values of products equal to the total in the file
                                            dt = {vat_list[0]: vat_list[1]}
                                            # Create a dictionary dt
                                            for g, j in zip(foodlist, food_priceList):
                                                # If a value exists, dt updated
                                                if g in dt:
                                                    dt[g] += j
                                                    temp = float("{0:.2f}".format(dt[g]))
                                                    dt[g] = temp
                                                else:
                                                    # If a value does not exist, updated
                                                    dt.update({g: j})
                                            #  Empty dictionary. Entry is made
                                            if not bool(data):
                                                diction = {"data" + str(len(data)): dt}
                                                # diction:if the set is before the end and is a correct receipt
                                                # used to undo the wrong entry
                                                data = {"data" + str(len(data)): dt}
                                                for u in range(len(foodlist)):
                                                    allaghlist.append(0)
                                            else:
                                                # Can be 0 or 1 entries in the key_list. Unique VAT number
                                                # If the customer already exists
                                                key_list = [n for (n, v) in data.items() if v['ΑΦΜ'] == vat_list[1]]
                                                if bool(key_list):  # Exists
                                                    diction = {key_list[0]: dt}
                                                    for p1, p2 in zip(foodlist, food_priceList):
                                                        if p1 in data.get(key_list[0]):
                                                            data[key_list[0]][p1.upper()] += p2 * 1
                                                            temp = float(
                                                                "{0:.2f}".format(data[key_list[0]][p1.upper()]))
                                                            data[key_list[0]][p1.upper()] = temp
                                                            allaghlist.append(1)
                                                            # 1 means that the price was updated
                                                            # Products updated
                                                        else:
                                                            data[key_list[0]][p1.upper()] = p2
                                                            allaghlist.append(0)
                                                            #  0 means first entry
                                                            # New entry added

                                                else:
                                                    #  New customer, new entry added
                                                    data.update({"data" + str(len(data)): dt})
                                                    diction = {"data" + str(len(data)): dt}
                                                    for u in range(len(foodlist)):
                                                        allaghlist.append(0)

                                            vat_list = []
                                            foodlist = []
                                            food_priceList = []  # Entry was made . Initialize
                                            food_quantList = []
                                            total = 0
                                            dt = {}
                                        else:
                                            # Different total cost of products from that of the proof
                                            err_counter += 1  # Increase the error counter
                                            print(err_counter, ")Different total cost from products' costs")
                                            print(read_ln)
                                            vat_list = []  # Each time an error occurs, new initializations
                                            foodlist = []
                                            food_priceList = []
                                            food_quantList = []
                                            total = 0
                                            total_flag = 0
                                            allaghlist.clear()
                                            while True:
                                                read_ln = fp.readline().strip('\n')
                                                if '-' in read_ln:  # Search for the beginning of new receipt
                                                    check = 1
                                                    break
                                    else:
                                        # More prices appeared on the receipt
                                        vat_list = []
                                        foodlist = []
                                        food_priceList = []
                                        food_quantList = []
                                        total = 0  # Each time an error occurs, new initializations
                                        total_flag = 0
                                        err_counter += 1  # Increase the error counter
                                        print(err_counter, ")More TOTAL(ΣΥΝΟΛΑ) fields than 1")
                                        print(read_ln)
                                        allaghlist.clear()
                                        while True:
                                            read_ln = fp.readline().strip('\n')
                                            if '-' in read_ln:  #  Search for the beginning of new receipt
                                                check = 1
                                                break
                        else:
                            #  TOTAL field and then new product. Error
                            if total_flag == 1:
                                num = 0  # Auxiliary variable
                                err_counter += 1  # Increase the error counter
                                print(err_counter, ")Error. Expected the end of the receipt")
                                print(read_ln)  # Each time an error occurs, new initializations
                                temp_dic = deepcopy(data)  # Used copy as an auxiliary dictionary
                                for w, o in diction.items():  # Cancel the previous update
                                    for p, kk in o.items():
                                        if "ΑΦΜ" in p:
                                            pass
                                        else:
                                            if allaghlist[num] == 1:  # 1: was there before. Updated prices
                                                temp_dic[w][p] -= kk  # Changes are made in the auxiliary
                                                temp = float("{0:.2f}".format(temp_dic[w][p]))
                                                temp_dic[w][p] = temp
                                            else:
                                                del temp_dic[w][p]  # 0: that it was the first entry of the product
                                            num += 1
                                data = temp_dic  # The data points to the modified data
                                foodlist = []
                                food_priceList = []
                                food_quantList = []
                                temp_dic = {}
                                vat_list = []
                                total = 0
                                total_flag = 0
                                allaghlist.clear()
                                while True:
                                    read_ln = fp.readline().strip('\n')
                                    if '-' in read_ln:  # Search for the beginning of new receipt
                                        check = 1
                                        break

                            else:
                                prices_list = []
                                num_str = ""
                                food_name = ""
                                for k in range(0, read_ln.find(':')):  # Product for the receipt
                                    food_name = food_name + read_ln[k]
                                for k in range((read_ln.find(':')) + 1, len(read_ln)):
                                    if read_ln[k] == ' ' or read_ln[k] == "\t":
                                        if "" != num_str:
                                            # Space and non-empty variable, stored in the list
                                            prices_list.append(num_str)
                                            num_str = ""
                                        pass
                                    elif read_ln[k].isdigit() or (
                                            read_ln[k] == '.' and read_ln[k - 1].isdigit() and read_ln[k + 1].isdigit()):
                                        num_str = num_str + read_ln[k]  # Digits are preserved
                                    elif ':' == read_ln[k]:
                                        pass
                                    else:
                                        # Invalid symbol
                                        err_counter += 1  # Increase the error counter
                                        print(err_counter, ")A mistake was made somewhere in the drafting of the receipt.")
                                        print(read_ln)
                                        vat_list = []  # Each time an error occurs, new initializations
                                        foodlist = []
                                        food_priceList = []
                                        food_quantList = []
                                        total = 0
                                        total_flag = 0
                                        allaghlist.clear()
                                        while True:
                                            read_ln = fp.readline().strip('\n')
                                            if '-' in read_ln:  # Search for the beginning of new receipt
                                                check = 1
                                                break
                                        break
                                else:
                                    prices_list.append(num_str)
                                    # More or less quantities are wrong
                                    if len(prices_list) != 3:
                                        err_counter += 1  # Increase the error counter
                                        print(err_counter, ")More or less quantities in a product")
                                        print(read_ln)
                                        vat_list = []  # Each time an error occurs, new initializations
                                        foodlist = []
                                        food_priceList = []
                                        food_quantList = []
                                        total = 0
                                        total_flag = 0
                                        allaghlist.clear()
                                        while True:
                                            read_ln = fp.readline().strip('\n')
                                            if '-' in read_ln:  # Search for the beginning of new receipt
                                                check = 1
                                                break
                                    else:
                                        num = float(prices_list[0]) if "." in prices_list[0] else int(prices_list[0])
                                        # print("num:",num)
                                        numb = math.floor(num)
                                        # print("numb:",numb)
                                        if num != numb:
                                            err_counter += 1  # Increase the error counter
                                            print(err_counter, ")Quantity is a real number")
                                            print(read_ln)  # Each time an error occurs, new initializations
                                            vat_list = []
                                            foodlist = []
                                            food_priceList = []
                                            food_quantList = []
                                            total = 0
                                            total_flag = 0
                                            allaghlist.clear()
                                            while True:
                                                read_ln = fp.readline().strip('\n')
                                                if '-' in read_ln:
                                                    check = 1  # Search for the beginning of new receipt
                                                    break
                                        else:

                                            calculate = float(
                                                "{0:.2f}".format(num * float(prices_list[1])))  # Posothta * timh = sinolo / quantity * value = cost

                                            # print("praksi:",praksi)
                                            if float("{0:.2f}".format(calculate)) == float(prices_list[2]):
                                                name: str = food_name.upper()
                                                if name in foodlist:
                                                    if float(prices_list[1]) != food_quantList[foodlist.index(name)]:
                                                        err_counter += 1  # Increase the error counter
                                                        print(err_counter,
                                                              ")Different product price in same receipt")
                                                        print(read_ln)  # Each time an error occurs, new initializations
                                                        vat_list = []
                                                        foodlist = []
                                                        food_priceList = []
                                                        food_quantList = []
                                                        total = 0
                                                        total_flag = 0
                                                        allaghlist.clear()
                                                        while True:
                                                            read_ln = fp.readline().strip('\n')
                                                            if '-' in read_ln:
                                                                check = 1  # Search for the beginning of new receipt
                                                                break
                                                    else:
                                                        foodlist.append(food_name.upper())  # Save to lists
                                                        food_priceList.append(float("{0:.2f}".format(calculate)))
                                                        food_quantList.append(float(prices_list[1]))
                                                        total += float(
                                                            "{0:.2f}".format(calculate))  # Update variables
                                                else:
                                                    foodlist.append(food_name.upper())  # Save to lists
                                                    food_priceList.append(float("{0:.2f}".format(calculate)))
                                                    food_quantList.append(float(prices_list[1]))
                                                    total += float(
                                                        "{0:.2f}".format(calculate))  # Update variables
                                            else:
                                                # Error in the calculation of the price of the product
                                                err_counter += 1  # Increase the error counter
                                                print(err_counter, ")Error in the calculation of the price of the product")
                                                print(read_ln)  # Each time an error occurs, new initializations
                                                vat_list = []
                                                foodlist = []
                                                food_priceList = []
                                                food_quantList = []
                                                total = 0
                                                total_flag = 0
                                                allaghlist.clear()
                                                while True:
                                                    read_ln = fp.readline().strip('\n')
                                                    if '-' in read_ln:
                                                        check = 1  # Search for the beginning of new receipt
                                                        break
                    else:
                        #   Invalid layout
                        vat_list = []
                        foodlist = []
                        food_priceList = []
                        food_quantList = []
                        total = 0
                        total_flag = 0  # Each time an error occurs, new initializations
                        allaghlist.clear()
                        err_counter += 1  # Increase the error counter
                        print(err_counter, ")Something went wrong")
                        print(read_ln)
                        while True:
                            read_ln = fp.readline().strip('\n')  # Search for the beginning of new receipt
                            if '-' in read_ln:
                                check = 1
                                break

                    read_ln = fp.readline().strip('\n')
                print("-->Finished Reading<--")
                fp.close()
                print("-->File Closed<--")
            # print("\nSeconds  =", round(time.time() - seconds, 2), end=" seconds")

        elif ans == 2:
            p_name = input("Give product name:")  #Search with Product name
            func_2(p_name, data)
        elif ans == 3:
            v_name = input('Give afm:')  # Search base VAT number
            func_3(v_name, data)
        elif ans == 4:
            print("\nExit Program!")  # Exit
            break
        elif ans > 4 or 1 > ans:
            print('Choice in range please')  # Options in range 1-5 valid
        else:
            pass
        print("\n")
exit(1)

