import time
from pygame import mixer
from receipt_generator import receipt

def summary_printing(Lays, Minute_Maid, Dairy_Milk, total_spent, result):
    print("\nPlease wait ", end=' ')
    for counter in range(3):
        print(".", end=' ', flush=True)
        time.sleep(0.5)

    # Playing dispatch sound if purchased
    if (Lays or Minute_Maid or Dairy_Milk) != 0:
        mixer.music.load("soda-machine.wav")
        mixer.music.play()
        time.sleep(3)
    else:
        mixer.music.load("scanner.wav")
        mixer.music.play()


    # Printing receipt
    receipt(Lays, Minute_Maid, Dairy_Milk, total_spent, result)

    print("\n\nYour Summary ****************")
    time.sleep(1)
    print("Total spent : $", total_spent)
    print("Balance : $", result)
    print("You have purchased :",Lays,"lays,",Minute_Maid,"Minute Maid,",Dairy_Milk,"Dairy Milk")
    time.sleep(1)
    print("\nPlease check your receipt once this program quits\nThank You :)")

    time.sleep(8)

