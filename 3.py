tuple1=(2,3,4,5,6)
tuple2=(2,11,7,8)

def Check(c,e):
    for i in c:
        for v in e:
            if i == v:
                return True
                break
            return False
if Check(tuple1,tuple2) == False:
    print("Khong trung")
else:
    print("trung")

