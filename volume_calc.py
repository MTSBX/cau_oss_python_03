box_length=float(input("please input the length of the box:"))
box_width=float(input("please input the width of the box:"))
box_height=float(input("please input the height of the box:"))
box_volume=float(box_length*box_width*box_height)
print("The volume of the box is:"+str(box_volume))

#week3 update
total_length=box_length+box_width+box_height
send_place=int(input("The place you want to send the box to:0:제주 1:다른 구역 "))

if send_place==0:
    flag=True
if send_place==1:
    flag=False

if flag==False:
    if(total_length<80.0):    
        print("The price is 5000")
    elif(total_length<100.0):
        print("The price is 8000")
    elif( total_length<120.0):
        print("The price is 10000")
    elif( total_length<160.0):
        print("The price is 13000")

if flag==True:
    send_speed=int(input("you want send your bag in: 1.oneday 2.D+2days"))
    if send_speed==1:
        if(total_length<80.0):
           print("The price is 7500")
        elif( total_length<100.0):
           print("The price is 10500")
        elif( total_length<120.0):
           print("The price is 12500")
        elif( total_length<160.0):
           print("The price is 15500")

    if send_speed==2:
        if(total_length<80.0):
           print("The price is 5000")
        if(80.0<total_length and total_length<100.0):
           print("The price is 8000")
        if(100.0<total_length and total_length<120.0):
           print("The price is 10000")
        if(120.0<total_length and total_length<160.0):
           print("The price is 13000")
    elif send_speed!=1 and send_speed!=2:
        print("please rewrite your choice")
