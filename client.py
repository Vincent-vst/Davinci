import requests 

url = 'http://127.0.0.1:3002/workers'
# example_item = {'task' : 'TRAP', 'pwd' : '/tmp', 'audio_sample' : 'bea.json', 'status' : 'success'}


def insert(item) : 
    return requests.post(url, data=item)

def get() : 
    return requests.get(url)

def delete(id_row) : 
    return requests.delete(url + '/' + str(id_row))


def main() : 
    cmd = input("action to perform : [get/delete/insert] ")
    match(cmd) : 
        case "get" : 
            response = get()
            print(response.json())
        case "insert" :
            print("inserting into database ")
            task = input("task : ")
            pwd = input("pwd : ")
            audio_sample = input("audio_sample : ")
            status = input("status : ")
            row = {'task' : task, 'pwd' : pwd, 'audio_sample' : audio_sample, 'status' : status}
            print(insert(row).text)
        case "delete" : 
            id_row = input("which line do you want to delete ? ")
            print(delete(id_row).text)

main()


# print(get_db.json())
# def update(): 
# update_item = { 'id' : 3, 'task' : 'TRAP', 'pwd' : '/tmp', 'audio_sample' : 'bea.json', 'status' : 'success'}
# update_in_db = requests.put (url, data=update_item) #Method not allowed : 405 

# print(update_in_db.text)

# print(delete_in_db.text)