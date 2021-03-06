"""Added Login Credentials In Athlete

Revision ID: 19b2d915e52a
Revises: b463f0358d6
Create Date: 2013-03-03 16:57:18.904837

"""

# revision identifiers, used by Alembic.
revision = '19b2d915e52a'
down_revision = 'b463f0358d6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('athletes', sa.Column('username', sa.String(length=50), nullable=True))
    op.add_column('athletes', sa.Column('password', sa.String(length=200), nullable=True))
    ### end Alembic commands ###


def downgrade():
    pass
