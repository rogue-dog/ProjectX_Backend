import jwt



def encode (id) :
    d = jwt.encode({"user_id" : id},"Random123","HS256")
    return d