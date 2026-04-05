import string
def check_email(email):
    num = "0123456789"
    answers = []
    answer = ""

    if "@" in email and "." in email:
        for i in email:
            if i in string.ascii_letters or i in num or i == "_" or i == "@" or i == ".":
                answers.append("ДА")
            else:
                answers.append("НЕТ")
    else:
        print("НЕТ")
    for i in answers:
        if i == "НЕТ":
            answer = "НЕТ"
            break
        else:
            answer = "ДА"
    print(answer)


check_email(input())

# def v_em(s):
#   if s.isascii() and s.count('@')==1 and s.count('.') == 1:
#       print('ДА')
#   else:
#       print('НЕТ')
#
# a = input()
# v_em(a)
