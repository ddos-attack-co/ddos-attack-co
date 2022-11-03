# ----------------Info Developer-------------
# -Last Name : Lecheheb
# -First Name : Djaafar
# -Country : Algeria
# -age : 26
# -Skills : Python - HTML - CSS - C
# -instagram : @ddos_attack_co
# ------------Fallowed Me for instagram-------

from click import clear
def num_str(word, x):
    list_num = []
    text = word[x:]
    for com in text:
        if com in "0123456789.":
            list_num.append(com)
        else:
            return "".join(list_num)
    return "".join(list_num)
def Tp_3(text="a+b=c"):
    car = ""
    tp = []
    list_text = text.split()
    for word in list_text:
        x = 0
        while x < len(word):
            if len(word)-1 < 1:
                tp.append((word[x]).center(3, '#'))
                break
            elif (x == 0 and word[x] == '-') or (x == 0 and word[x] == '+'):
                tp.append((word[x]+word[x+1]).center(4, '#'))
                x += 1
            elif (word[x] in "0123456789"):
                number = num_str(word, x)
                for car in number:
                    x += 1
                tp.append((number).center(len(number)+2, '#'))
                x -= 1
            elif word[x] in "+-*/!=<>" and word[x+1] == "=":
                tp.append((word[x]+word[x+1]).center(4, '#'))
                x += 1
            elif word[x] == "=" and word[x+1] in "+-":
                tp.append((word[x]).center(3, '#'))
                x += 1
                tp.append((word[x]+word[x+1]).center(4, '#'))
                x += 1
            elif word[x] == "(" and word[x+1] in "+-":
                tp.append((word[x]).center(3, '#'))
                x += 1
                tp.append((word[x]+word[x+1]).center(4, '#'))
                x += 1
            else:
                tp.append((word[x].center(3, '#')))
            x += 1
    return " ".join(tp)


while True:
  password = input("Type Password :")
  if password != '@ddos_attack_co':
    print("Password Error pleas Go instagram:@ddos_attack_co")
  else:
      
      text = input("Pleas enter your Text :")
      clear()
      print(f"Old Text :\n{text}")
      print(f"New Text :\n{Tp_3(text)}")

