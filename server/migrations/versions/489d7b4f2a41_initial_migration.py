"""initial migration

Revision ID: 489d7b4f2a41
Revises: 
Create Date: 2024-02-21 09:27:38.208027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '489d7b4f2a41'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sightings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('time', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('shape_of_craft', sa.String(), nullable=True),
    sa.Column('approximate_size', sa.Integer(), nullable=True),
    sa.Column('approximate_speed', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('reporter', sa.String(), nullable=True),
    sa.Column('reporter_sober', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sightings')
    # ### end Alembic commands ###