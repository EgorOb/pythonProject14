from pydantic import BaseModel, ConfigDict


class Obj(BaseModel):
    data: list|None = []
    value: int = 123
    model_config = ConfigDict(validate_assignment=True)


a = Obj(data=None, hello=435, value='123')
print(repr(a))

print(a.data)
print(type(a.value))
a.data = 'abc'
print(a.data)