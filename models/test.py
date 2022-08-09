import uuid
from datetime import datetime

# # # id = uuid.uuid1()

# # version4 = str(uuid.uuid4())

# # time = datetime.now()

# # # print("this is the generated id {}".format(id))

# # print("this is thee second version of id4 {}".format(version4))

# # print(time)
# # # print(hex(uuid.getnode()))


# # my_dict = {
# #     "name": "ifeanyi Ifediniru",
# #     "Age" : 25,
# # }

# # print(my_dict)
# # my_dict["Age"] = str(my_dict["Age"])

# # print(my_dict)


# class Gost:
    

#     def __init__(self):
#         pass

#     def __str__(self):
#         return f"({self.__dict__})"
    

# ife = Gost()
# ife.age = 27
# print(ife)





class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"