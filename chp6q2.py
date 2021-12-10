sub1 = int(input("SUB1 marks:"))
sub2 = int(input("SUB2 marks:"))
sub3 = int(input("SUB3 marks:"))

tPer = (sub1+sub2+sub3)/3

if(sub1>=33 and sub2>=33 and sub3>=33):
    if tPer>=40:

        print("Pass");
    else:
        print("Fail");
else:
    print("You didnt make in one of the subjects");
