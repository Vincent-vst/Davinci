import requests 

# url = 'http://127.0.0.1:3001/workers'

# test = {'task':'test', 'pwd':'oui', 'audio_sample':'ha', 'status':'nope'}


# requests.post(url, data=test)
# var = input("input var : ")
# print(var)
var = 3

# if (not isinstance(var, int)) or (0 <= var <=2): 
#     print("not int or not in range [0,2]")

if not (isinstance(var, int) and (0 <= var <= 2)) :
    print('not int or not in [0,2]')


# if (not isinstance(var, int)) : 
#     print('not int')
#     # if not (0 <= int(var) <= 2) : 
#     #     print('not in range [0,2]') 


# if not (0 <= int(var) <= 2) or (not isinstance(var, int)): 
#     print("not in range [0,2] or not int ")

