
print("My first script.\nPowered by CSR. 2023")

def ip (ip="127.0.0.1",mask="/24"):
    return "Your adress is: "+ip+mask+";"
r1 = ip(mask="/27")
r2 = ip("1.1.1.10","/32")
print(r1+"\n"+r2)