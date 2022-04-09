from math import fabs
from tortoise import Tortoise,Model, fields


#https://tortoise-orm.readthedocs.io/en/latest/fields.html

class Users(Model):
    __tablename__ = 'users'
    
    id = fields.IntField(pk=True,unique=True)
    user = fields.CharField(255,nullable=False,unique=True)
    password = fields.CharField(255,nullable=False)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    

    def __str__(self):
        return f"User {self.id}: {self.user}"
    
 