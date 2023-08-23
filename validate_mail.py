import re



def validating_email_id(mail_id):
    pattern=r"^[a-zA-Z0-9]+(|a-zA-Z0-9)+\@[a-z]+\.[a-z]+"
    out=re.search(pattern,mail_id)

    if out:
        data=out.group().split("@")
        print(len(data[0]))
        if len(data[0])>8:
            print(out.group(),"inside mail")
            fw=open(r"C:\Users\Thippeswamy U-3061\PycharmProjects\pythonProject\ramp_up_python\email_data.txt","a")
            fw.write(out.group()+"\n")
            fw.close()
#validating_email_id("thippeswamy95655@gmail.com")
def read_data_from_ext_file():

    fr = open(r"C:\Users\Thippeswamy U-3061\PycharmProjects\pythonProject\ramp_up_python\email_data.txt", "r")
    out=fr.read()

    fr.close()
    return out
while True:
    enter_mail = input("enter email address:")

    user_inputs = input("Enter your answer Yes/No for this mail  " + enter_mail)

    if user_inputs == "Yes" or user_inputs=="yes" or user_inputs=="Y":
        print(enter_mail)
        validating_email_id(enter_mail)
    if user_inputs == "No" or user_inputs == 'no' or user_inputs == "N":
        out = read_data_from_ext_file()
        print(out)
        break







