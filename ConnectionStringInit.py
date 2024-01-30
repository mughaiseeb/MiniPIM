from Models import connectionString as conn

def  GetConText():

    myfile = open("ConText.txt" ,"r")

    # print(myfile.read())

    data = myfile.readlines()
    
    myfile.close()

    for con in data:
       temp = con.split(":")
       if temp[0].lower()=="host":
        _host=temp[1]
       elif temp[0].lower()=="user":
        username = temp[1]
       elif temp[0].lower()=="password":
        password = temp[1]

    connection = conn(_host , username , password)

    return connection