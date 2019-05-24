"""This program is the heart of the vending machine application
   Important variables are defined, logic executed and returns the result for printing"""

import time
from pygame import mixer
import sys

LARGE_FONT= ("Verdana", 12)
count = 0  # counter to terminate program if >3 wrong input provided
flag = False  # Flag when set to true terminates the program
critical = False # Flag when set to true terminates the program
empty = False

print("\n******** Silver Moon Vending Machine Program ********")
time.sleep(1)

mixer.init()
mixer.music.load('vending-machine-spinning.wav')
mixer.music.play(-1)

# Counting invalid attempts
def terminate(count):
    global flag
    if count <= 3:
        mixer.music.load("error-signal-2.wav")
        mixer.music.play()
        time.sleep(1)

        mixer.music.load('vending-machine-spinning.wav')
        mixer.music.play(-1)
        print("You have {} retry(s) left\n".format(3-count))
        return flag
    else:
        mixer.music.load("error.wav")
        mixer.music.play()
        time.sleep(1)
        flag = True
        return flag

# User Input
def user_input(balance):
    global wallet
    global critical
    global count
    coins = input("\nValues acceptable : 5, 10, 20"
                  "\nPlease insert token - ")
    # Validating User Input
    accepted_values = [5, 10, 20]
    try:
        accepted_values.index(int(coins))

        mixer.music.load('coins-1.wav')
        mixer.music.play()

        print("Token accepted!!\n")
        wallet = balance+int(coins)
        time.sleep(1)

        mixer.music.load('vending-machine-spinning.wav')
        mixer.music.play(-1)

        print("Balance :", wallet)
        return wallet
    except:
        print("Token unacceptable\n")
        count += 1
        check1 = terminate(count)
        if check1 == True and balance == 0 and empty != True:
            print("Invalid input exceeded three times.\nExiting the program\n")
            return 'EXIT'
        elif check1 == True and balance == 0 and empty == True:
            print("Invalid input exceeded three times.\nExiting the program\n")
            return '0'
        elif check1 == True and balance != 0:
            print("Invalid input exceeded three times.\nExiting the program\n")
            critical = True
            sys.exit()
        else:
            return user_input(balance)

# Initializing variables
Lays = Minute_Maid = Dairy_Milk = 0
Lays_count = Minute_Maid_count = Dairy_Milk_count = 5
inventory_check_retry = 0

# Buying an item from inventory
def buy(wallet):
    # Selection
    global coins
    global count
    coins = wallet
    mapping_value = {1: 5, 2: 10, 3: 20}
    mapping_item = {1: 'Lays', 2: 'Minute Maid', 3: 'Dairy Milk'}
    item = input("### Make your selection 1/2/3/4/5 ### \n"
          "1. Lays - $5             {0} in stock\n"
          "2. Minute Maid - $10     {1} in stock\n"
          "3. Dairy Milk - $20      {2} in stock\n"
          "4. Load more $$\n"
          "5. Exit \n\n".format(Lays_count, Minute_Maid_count, Dairy_Milk_count))
    try:
        # Validating if eligible to buy
        if item == '4':
            load_more = user_input(wallet)
            return buy(load_more)
        elif item == '5':
            print("See You Again")
            return wallet
        elif mapping_value[int(item)] > wallet:
            print("Insufficient token")
            def purchase():
                global count
                ask = input("Type 1 to load more or 2 to make another selection ")
                if ask == '1':
                    updated_balance = user_input(wallet)
                    return buy(updated_balance)
                if ask == '2':
                    return buy(wallet)
                else:
                    print("\nWrong selection")
                    count += 1
                    check2 = terminate(count)
                    if check2 == True:
                        return wallet
                    else:
                        return purchase()
            return purchase()

        elif mapping_value[int(item)] <= wallet:

            # Checking if there are items left to buy for the selection made
            if (((mapping_item[int(item)]) == 'Lays') and (Lays_count == 0)) or (((mapping_item[int(item)]) == 'Minute Maid') and (Minute_Maid_count == 0)) or (((mapping_item[int(item)]) == 'Dairy Milk') and (Dairy_Milk_count == 0)):
                mixer.music.load("error-signal-2.wav")
                mixer.music.play()
                time.sleep(1)

                mixer.music.load('vending-machine-spinning.wav')
                mixer.music.play(-1)

                def inventory_check():
                    global count
                    global inventory_check_retry
                    print("{} has no inventory left\n".format(mapping_item[int(item)]))
                    inventory_exhausted = input("Would you like to continue (Y/N) : ")
                    if (inventory_exhausted == 'Y' or inventory_exhausted == 'y'):
                        inventory_check_retry += 1
                        if inventory_check_retry == 2:
                            print("This is you final stock retry\n")
                            return buy(wallet)
                        elif inventory_check_retry == 3:
                            print("Stock retry limit reached")
                            return wallet
                        else:
                            return buy(wallet)
                    elif (inventory_exhausted == 'N' or inventory_exhausted == 'n'):
                        print("Thank you! Have a nice day")
                        return wallet
                    else:
                        print("Wrong selection")
                        count += 1
                        check_exhaust = terminate(count)
                        if check_exhaust == True:
                            return wallet
                        else:
                            return inventory_check()
                return inventory_check()

            # Continues purchasing since there are items available in the inventory
            else:
                mixer.music.load("cash-register.mp3")
                mixer.music.play()
                time.sleep(1)

                print("You get one", mapping_item[int(item)])

                mixer.music.load('vending-machine-spinning.wav')
                mixer.music.play(-1)

                # Keeping count of items purchased
                def mappping():
                    if mapping_item[int(item)] == 'Lays':
                        global Lays
                        global Lays_count
                        Lays += 1
                        Lays_count -= 1
                    if mapping_item[int(item)] == 'Minute Maid':
                        global Minute_Maid
                        global Minute_Maid_count
                        Minute_Maid += 1
                        Minute_Maid_count -= 1
                    if mapping_item[int(item)] == 'Dairy Milk':
                        global Dairy_Milk
                        global Dairy_Milk_count
                        Dairy_Milk += 1
                        Dairy_Milk_count -= 1
                mappping()
                time.sleep(1)

                # calculate balance
                balance = wallet - mapping_value[int(item)]
                def balance_checking():
                    global count
                    global empty
                    global flag
                    print("\nBalance : ", balance)
                    if balance > 0:
                        more = input("\nDo you want to buy something else? (Y/N) ")
                        if (more == 'Y' or more == 'y'):
                            return buy(balance)
                        elif (more == 'N' or more == 'n'):
                            print("Thank You! Have a nice day")
                            return balance
                        else:
                            print("Wrong selection")
                            count += 1
                            check3 = terminate(count)
                            if check3 == True:
                                return balance
                            else:
                                return balance_checking()

                    if balance == 0:
                        empty = True # Flag to state the balance has reduced to zero
                        query = input("\nDo you want to load more and continue purchasing? (Y/N) ")
                        if (query == 'Y' or query == 'y'):
                            coins = user_input(balance)
                            if flag == True:
                                return 0
                            else:
                                return buy(coins)
                        elif (query == 'N' or query == 'n'):
                            print("Thank You! Have a nice day")
                            return balance
                        else:
                            print("Wrong selection")
                            count += 1
                            check4 = terminate(count)
                            if check4 == True:
                                return balance
                            else:
                                return balance_checking()
                return balance_checking()

    except:
        if critical == True:
            return coins
        else:
            print("Wrong selection")
            count += 1
            check5 = terminate(count)
            if check5 == True:
                print("Invalid input exceeded three times.\nExiting the program\n")
                return coins
            else:
                return buy(coins)
