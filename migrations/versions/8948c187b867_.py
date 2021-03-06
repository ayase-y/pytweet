"""empty message

Revision ID: 8948c187b867
Revises: dcd9991e4c21
Create Date: 2020-01-25 07:58:40.280149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8948c187b867'
down_revision = 'dcd9991e4c21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('comment', sa.String(length=1000), nullable=False))
    op.add_column('comment', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('comment', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('comment', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'comment', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'user_id')
    op.drop_column('comment', 'id')
    op.drop_column('comment', 'created_at')
    op.drop_column('comment', 'comment')
    # ### end Alembic commands ###
