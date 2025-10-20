import cowsay
from art import tprint
import datetime

def rot(st, n):
    return "".join(chr((ord(i)-n-97+26)%26+97) if i.isalpha() and i.islower() else i for i in st)

def get_challenge_message(rrrrr):

    flag1 = "NCKUCTF{elcelc_"
    flag2 = "o@H@H4_w@ukh_1u1u1u"
    flag3 = "_Cexii3kd3!}"

    message = f"Bravo! The first part of the flag is '{rot(flag1, rrrrr)}'\n"
    message += f"Keep digging! The second part is '{rot(flag2, rrrrr)}'\n"
    message += f"Almost there! The final part is '{rot(flag3, rrrrr)}'\n"
    message += "Welcome, Challenger! Look closely at the code for hints."

    return message

def main():
    tprint("HELLO Challenger")

    rrr = int(input("get hint:"))
    challenge_message = get_challenge_message(rrr)

    cowsay.cow(challenge_message)


if __name__ == "__main__":
    main()
