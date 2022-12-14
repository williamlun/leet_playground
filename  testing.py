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



nums = [-1,0,3,5,9,12]
target = 12


def search(nums: list[int], target: int) -> int:
    upper = len(nums)
    lower = 0
    while(True):
        middle = int((upper - lower)/2)
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            upper = middle
        elif nums[middle] < target:
            lower = middle
        if middle == upper or middle == lower:
            for i in range(lower, upper):
                if nums[i] == target:
                    return i
            return -1
        
print(search(nums,target))