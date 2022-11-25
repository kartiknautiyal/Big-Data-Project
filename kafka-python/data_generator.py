import random 
import string

user_id = list(range(1,101))
rec_id = list(range(1,101))

def generate_message():
    random_user_id = random.choice(user_id)
    
    rec_id_copy = rec_id.copy()
    rec_id_copy.remove(random_user_id)

    random_rec_id = random.choice(rec_id_copy)

    mesg = ''.join(random.choice(string.ascii_letters) for i in range(32))

    return {
        'user_id' : random_user_id,
        'recipient_id': random_rec_id,
        'message': mesg
    }

# # test 
# if __name__ == '__main__':
#     print(generate_message())