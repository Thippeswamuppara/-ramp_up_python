import yaml
import sys
from colorama import Fore, Style
import tkinter as tk

def toggle_blink():


    if label.cget("font") == "helvetica 12 bold":
        label.config(font=("helvetica", 12, "normal"))
    else:
        label.config(font=("helvetica", 12, "bold"))
    root.after(500, toggle_blink)

root = tk.Tk()
root.title("Blinking Text Example")




#
d = {"notes": {200: 2, 500: 10, 100: 80, 50: 2}}

l1 = []
BLINK = '\033[5m'
class ATM():
    while True:
        flag = False

        try:
            user_input = int(input("Enter amount"))
            if isinstance(user_input,int) and (user_input % 100==0 or user_input % 50==0):
                init = user_input
                break
            print(Fore.RED+"please enter amount interms of 100rs  0r 50s"+Style.RESET_ALL)

        except:
            print(Fore.GREEN+"you Entered invalid amount"+Style.RESET_ALL)
            print("*********************************\n")
            print(Fore.YELLOW+"still you want to continue hit yes else no"+Style.RESET_ALL)
            user_choice=input("enter your choice")
            if user_choice=="yes":
                pass
            elif user_choice=="no" or user_choice=="":

                #print("you are Exited from the operation")
                sys.exit(Fore.GREEN+"you are Exited from the operation")






    def __init__(self,dict1):
        self.dict1=dict1
    def ascending_notes_from_max_to_min(self):
        note=list(self.dict1['notes'].keys()) #[500,200,100,50]

        note.sort()
        notes=note[::-1]

        return notes
    def check_and_pick_notes_according_to_enter_money(self):
        notes=self. ascending_notes_from_max_to_min()
        l1 = []
        while True:
            note=[note for note in notes if note<=self.user_input]

            if len(note)!=0:
                l1.append(note[0])

                self.user_input=self.user_input-note[0]

            if self.user_input==0 or len(note)==0:

                break

        return l1








    def get_notes(self):
        parsing_and_count_notes=self.check_and_pick_notes_according_to_enter_money()
        d={i:parsing_and_count_notes.count(i) for i in parsing_and_count_notes}

        dict_notes=yaml.dump(d)
        return f"you withdrawl notes count of each note is \n {dict_notes} ".title()


obj=ATM(d)
l1=obj.get_notes()
label = tk.Label(root, text=Fore.BLUE+l1, font=("helvetica", 12, "bold"))
label.pack()
toggle_blink()  # Start the blinking animation
root.mainloop()




#
