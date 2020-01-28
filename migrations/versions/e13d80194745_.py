"""empty message

Revision ID: e13d80194745
Revises: 2ee0bd8b8d3a
Create Date: 2020-01-27 14:35:40.867092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e13d80194745'
down_revision = '2ee0bd8b8d3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('post_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'comments', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'post_id')
    # ### end Alembic commands ###