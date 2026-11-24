mystring = "my name is edward"
myfloat = float(54)
myint = 27

if mystring == "my name is edward":
    print("String: %s" % mystring)
    if isinstance(myfloat, float) and myfloat == 54:
        print("Float: %f" % myfloat)
        if isinstance(myint, int) and myint == 27:
            print("Integer: %d" % myint)