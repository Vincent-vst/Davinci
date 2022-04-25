import requests 

url = 'http://10.16.0.250:3001/workers'


"""
description : insert in API database 
parameters : dictionary -> {'task' : task, 'pwd' : pwd, 'audio_sample' : audio_sample, 'status' : status}
return : requests.Response Object 
"""
def insert(item) : 
    return requests.post(url, data=item)

"""
description : select * from workers; in API database  
parameters : None  
return : requests.Response Object 
"""
def get() : 
    #TODO : get with id 
    return requests.get(url)

"""
description : delete row in API database  
parameters : int -> the id of the row that needs to be deleted  
return : requests.Response Object 
"""
def delete(id_row) : 
    return requests.delete(url + '/' + str(id_row))

#TODO : update() method  

"""
description : ask user input to perfom various action {update | insert | delete} on a database
parameters : None 
type : None 
return : None 
"""
# def main() : 
#     cmd = input("action to perform : [get/delete/insert] ")
#     match(cmd) : 
#         case "get" : 
#             response = get()
#             print(response.json())
#         case "insert" :
#             task, pwd, audio_sample, status = input("insert task, pwd, audio_sample, status : ").split()
#             row = {'task' : task, 'pwd' : pwd, 'audio_sample' : audio_sample, 'status' : status}
#             print(insert(row).text)
#         case "delete" : 
#             id_row = input("which line do you want to delete ? ")
#             print(delete(id_row).text)

# print(delete(13))

task = input("insert task : ")
pwd = input("insert pwd : ")
audio_sample = input("insert audio_sample : ")
status = input("insert status : ")
row = {'task' : task, 'pwd' : pwd, 'audio_sample' : audio_sample, 'status' : status}
print(insert(row).text)

# if __name__ == '__main__' : 
#     main()
