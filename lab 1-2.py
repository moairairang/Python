score = int(input("ใส่คะเเนน : "))
if(score > 100):
    print("กรุณาใส่ข้อมูล 0-100")
elif(score < 0):
    print("กรุณาใส่ข้อมูล 0-100")
elif(score >= 80):
    print("Grade A")
elif(score >= 70):
    print("Grade B")
elif(score >= 60):
    print("Grade C")
elif(score >= 50):
    print("Grade D")
elif(score < 50):
    print("Grade F")


