from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Todo(models.Model):
    
    id = fields.IntField(pk=True)
    todo = fields.CharField(max_lenght=250)
    la_date = fields.CharField(max_lenght=250)
    
    class PydanticMeta:
        pass
    
TodoOut_Pydantic = pydantic_model_creator(Todo, name="TodoOut")
TodoIn_Pydantic = pydantic_model_creator(Todo, name="TodoIn", exclude_readonly=True)
