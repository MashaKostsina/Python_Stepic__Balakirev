phone = input()
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
number_format = ["+", "7", "(", number, number, number, ")", number, number, number, "-", number, number, "-", number, number]

flag = ""
if phone[0] == "+" and phone[1] == "7":
    for i in range(len(phone)):
        if phone[i] in number_format[:] or phone[i] in number[:]:
            flag = "ДА"
        else:
            flag = "НЕТ"
            break
else:
    flag = "НЕТ"
print(flag)

