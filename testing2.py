import pydantic


def to_camel(string: str) -> str:
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])


class Tenant(pydantic.BaseModel):
    display_name: str
    name: str

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class Site(pydantic.BaseModel):
    display_name: str
    name: str

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class Field(pydantic.BaseModel):
    name: str


class Device(pydantic.BaseModel):
    display_name: str
    name: str

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


myDevice = Device(display_name="DLLM", name="on99")
print(myDevice.json(by_alias=True))


q = f"{myDevice.json(by_alias=True)}"


print("123")
print("123")
print("123")
print("123")
print("123")
print("123")
print("123")
print("123")
