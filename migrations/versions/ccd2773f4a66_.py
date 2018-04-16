"""empty message

Revision ID: ccd2773f4a66
Revises: 
Create Date: 2018-04-17 00:20:23.649502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccd2773f4a66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('birth', sa.DateTime(), nullable=True),
    sa.Column('hire_date', sa.DateTime(), nullable=True),
    sa.Column('sex', sa.String(length=1), nullable=True),
    sa.Column('payment', sa.Integer(), nullable=True),
    sa.Column('children', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('voice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('actor',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('voice_range', sa.Integer(), nullable=True),
    sa.Column('best_genre', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['best_genre'], ['genre.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['voice_range'], ['voice.id'], ),
    sa.PrimaryKeyConstraint('employee_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('actor')
    op.drop_table('voice')
    op.drop_table('genre')
    op.drop_table('employee')
    # ### end Alembic commands ###
