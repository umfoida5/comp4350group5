"""added health table

Revision ID: 52a5e947a08d
Revises: 466668de7dee
Create Date: 2013-03-08 15:12:22.450192

"""

# revision identifiers, used by Alembic.
revision = '52a5e947a08d'
down_revision = '466668de7dee'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('health',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('athlete_id', sa.Integer(), nullable=False),
    sa.Column('health_date', sa.Date(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('resting_heart_rate', sa.Integer(), nullable=True),
    sa.Column('comments', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['athlete_id'], ['athletes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    pass