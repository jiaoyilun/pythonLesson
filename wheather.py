from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import


def buildclient():
    imp = Import("http://www.w3.org/2001/XMLSchema", location="http://www.w3.org/2001/XMLSchema.xsd")
    imp.filter.add("http://WebXml.com.cn/")
    doctor = ImportDoctor(imp)
    url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl"
    client = Client(url, doctor=doctor)
    return client.service


def getprovinces():
    result = buildclient().getRegionProvince()
    for name in result[0]:
        item = name.split(",")
        print(item[0] + "---" + item[1])
        getcities(item[1])
        break


def getcities(provincecode):
    result = buildclient().getSupportCityString(theRegionCode=provincecode)
    for name in result[0]:
        item = name.split(",")
        print(item[0] + "---" + item[1])
        getwearther(item[1])
        break
    print("--------------------------------")


def getwearther(citycode):
    result = buildclient().getWeather(theCityCode=citycode)
    print(result[0])
    for item in result[0]:
        print(item)
        print("==========")


getprovinces()
