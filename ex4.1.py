
temperatureType=input("Choose temperature type-\n1.Farenheit\n2.Centigrade\nEnter option no:")

if int(temperatureType) <1 or int(temperatureType)>2:
    print("invalid option")
    exit()

temperature=input("Enter temperature:")

def convertToFarenheit():
    farenheit=(int(temperature) * 1.8)+32
    print(farenheit,"F")

def converToCentigrade():
    centigrade=(int(temperature)-32)/1.8
    print(centigrade,"C")

operation=convertToFarenheit if int(temperatureType) == 1 else converToCentigrade
operation()