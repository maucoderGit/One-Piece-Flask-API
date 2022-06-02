"""Initial_db

Revision ID: 77029703dd02
Revises: 
Create Date: 2022-06-02 11:25:50.934018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77029703dd02'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crew',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('devil_fruit',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('origin', sa.String(), nullable=True),
    sa.Column('crew_id', sa.Integer(), nullable=True),
    sa.Column('devil_fruit_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['crew_id'], ['crew.id'], ),
    sa.ForeignKeyConstraint(['devil_fruit_id'], ['devil_fruit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('character')
    op.drop_table('devil_fruit')
    op.drop_table('crew')
    # ### end Alembic commands ###