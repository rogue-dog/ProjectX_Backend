import jwt
Secret = "z%C&F)J@NcRfUjXn2D(G-KaP"
token = "eyJjE2MzUyNjczODYsImV4cCI6MTYzNzg1OTM4Nn0.Q6u03HX43LjLWbuvRR9q_9ynmlvNv5WQBtkzT9EIL2c"


def encode (id) :
    d = jwt.encode({"user_id" : id},Secret,"HS256")
    return d


def decode(id) :
    d = jwt.decode(id,"Secret",['HS256'])
    print(d)


