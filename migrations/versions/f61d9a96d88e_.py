"""empty message

Revision ID: f61d9a96d88e
Revises: 
Create Date: 2024-09-25 12:20:51.163117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f61d9a96d88e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.String(length=16), nullable=False),
    sa.Column('category', sa.String(length=16), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###
