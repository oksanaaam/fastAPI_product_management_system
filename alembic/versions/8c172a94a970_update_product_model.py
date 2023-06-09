"""Update Product model

Revision ID: 8c172a94a970
Revises: 9239de02a775
Create Date: 2023-06-06 18:42:25.451460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c172a94a970'
down_revision = '9239de02a775'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_products_name', table_name='products')
    op.create_index(op.f('ix_products_name'), 'products', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_name'), table_name='products')
    op.create_index('ix_products_name', 'products', ['name'], unique=False)
    # ### end Alembic commands ###
