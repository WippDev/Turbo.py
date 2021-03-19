import json 


async def open_account(user):
    users = await get_bank_data()
     
    

    if str(user.id) in users:
        return False

    else :
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
        users[str(user.id)]["commisions"] = 0
        users[str(user.id)]["negative"] = 0
        users[str(user.id)]["about"] = "None"
        users[str(user.id)]["portofolio"] = "None"
        users[str(user.id)]["timezone"] = "None"

    
    with open("bank.json" , "w") as f:
        json.dump(users,f)
    
    return True

async def get_bank_data():
    with open("bank.json" , "r") as f:
        users = json.load(f)
    
    return users
    
async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json" , "w") as f:
        json.dump(users,f)
    
    bal = [ users[str(user.id)]["wallet"] , users[str(user.id)]["bank"] , users[str(user.id)]["commisions"]]
    return bal  


