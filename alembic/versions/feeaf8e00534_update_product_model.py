"""Update Product model

Revision ID: feeaf8e00534
Revises: 0b53295458a5
Create Date: 2023-06-06 20:20:44.428347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'feeaf8e00534'
down_revision = '0b53295458a5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_products_name', table_name='products')
    op.create_index(op.f('ix_products_name'), 'products', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_name'), table_name='products')
    op.create_index('ix_products_name', 'products', ['name'], unique=False)
    # ### end Alembic commands ###
