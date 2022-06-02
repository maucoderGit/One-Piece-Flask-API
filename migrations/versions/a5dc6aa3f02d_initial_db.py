"""Initial_db

Revision ID: a5dc6aa3f02d
Revises: 9a1cc5d8f12b
Create Date: 2022-06-02 16:09:06.472844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5dc6aa3f02d'
down_revision = '9a1cc5d8f12b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('character', sa.Column('devil_fruit', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'character', type_='foreignkey')
    op.create_foreign_key(None, 'character', 'devil_fruit', ['devil_fruit'], ['id'])
    op.drop_column('character', 'devil_fruit_id')
    op.drop_column('devil_fruit', 'status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('devil_fruit', sa.Column('status', sa.VARCHAR(), nullable=True))
    op.add_column('character', sa.Column('devil_fruit_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'character', type_='foreignkey')
    op.create_foreign_key(None, 'character', 'devil_fruit', ['devil_fruit_id'], ['id'])
    op.drop_column('character', 'devil_fruit')
    # ### end Alembic commands ###