t = eval(input())
new_dict = dict()
while(t):
    t-=1
    x = input()
    y = x.split(" ")
    new_dict.update({y[0].lower():y[1]})
z = input()
new_list = list()
while True:
    new_list.append(z)
    try:
        z = input()
    except:
        break
for i in new_list:
    if(new_dict.get(i)):
        print(i+"="+new_dict[i])
    else:
        print("Not found")
