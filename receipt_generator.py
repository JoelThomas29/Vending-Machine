""" This Program generates a text file """

def receipt(Lays, Minute_Maid, Dairy_Milk, total_spent, result):
    file = open('RECEIPT.txt', 'w')
    file.write("+-----------------------------+\n"
               "|  Receipt for you purchase   |\n"
               "+-----------------------------+\n"
               "| 1. Lays -  {0}                |\n"
               "| 2. Minute Maid -  {1}         |\n"
               "| 3. Dairy Milk -  {2}          |\n"
               "+-----------------------------+\n"
               "  # Total spent : $ {3} \n"
               "  # Balance : $ {4} \n"
               "           ********\n"
               " ** Thank You! Visit us soon ** ".format(Lays, Minute_Maid, Dairy_Milk, total_spent, result))
    file.close()

if __name__ == '__main__':
    print("This program generates receipt")

