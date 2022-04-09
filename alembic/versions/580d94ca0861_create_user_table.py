"""create user table

Revision ID: 580d94ca0861
Revises: 
Create Date: 2022-04-04 14:56:08.203070

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '580d94ca0861'
down_revision = None
branch_labels = None
depends_on = None
#command migration up: alembic upgrade head
#command migration down: alembic downgrade base
def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True,unique=True),
        sa.Column('user', sa.String(255), nullable=False,unique=True),
        sa.Column('password', sa.String(255), nullable=False),


        sa.Column('created_at',  sa.types.DateTime(timezone=True), default=datetime.datetime.utcnow),
        sa.Column('updated_at',  sa.types.DateTime(timezone=True), default=datetime.datetime.utcnow),

    )


def downgrade():
    op.drop_table('users')
    
