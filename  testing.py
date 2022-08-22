import pydantic

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1]
myset2 = list(set(mylist))


print(myset2)
print(type(myset2))

my_dict = {"a": 1, "b": 2, "c": 3}


class Mymodel(pydantic.BaseModel):
    a: int
    b: int
    c: int
    d: int = 999
    e: int = -999
    f: int = 999


myobj = Mymodel(**my_dict)

print(myobj.a)
print(myobj.b)
