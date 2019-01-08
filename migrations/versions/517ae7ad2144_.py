"""empty message

Revision ID: 517ae7ad2144
Revises: e25b84e122c2
Create Date: 2019-01-08 21:35:07.454234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '517ae7ad2144'
down_revision = 'e25b84e122c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('serverStats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=4096), nullable=True),
    sa.Column('value', sa.String(length=4096), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('serverStats')
    # ### end Alembic commands ###
