import requests 

# url = 'http://10.16.0.250:3002/api'
url = 'http://127.0.0.1:3001/api'


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
# data={'user':'tom', 'task':'trap', 'pwd':'/usr',  'occ_id':'bea2022', 'audio_sample':'{"name": "tom"}', 'priority' : 2, 'eta':'timedate()', 'status':'pending'}
# print(insert(data)) 
# print(delete(13))

# if __name__ == '__main__' : 
#     main()


# user_update={'user':'test'}
print(requests.put('http://127.0.0.1:3001/api/1' , data={"user":"test"}))



