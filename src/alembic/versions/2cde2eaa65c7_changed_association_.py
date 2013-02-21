"""changed association table

Revision ID: 2cde2eaa65c7
Revises: 90eb1c6b45e
Create Date: 2013-02-20 13:31:45.239342

"""

# revision identifiers, used by Alembic.
revision = '2cde2eaa65c7'
down_revision = '90eb1c6b45e'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from datetime import datetime
from sqlalchemy.sql.expression import text

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('unlocked_achievements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('athlete_id', sa.Integer(), nullable=False),
    sa.Column('achievement_id', sa.Integer(), nullable=False),
    sa.Column('unlocked_date', sa.DateTime(), nullable=False, server_default=sa.sql.expression.text('current_timestamp')),
    sa.ForeignKeyConstraint(['achievement_id'], ['achievements.id'], ),
    sa.ForeignKeyConstraint(['athlete_id'], ['athletes.id'], ),
    sa.PrimaryKeyConstraint('id', 'athlete_id', 'achievement_id')
    )
    op.drop_table(u'athlete_achievements')
    op.drop_column('achievements', u'creation_date')
    op.execute("DELETE FROM achievements")
    op.create_unique_constraint("uq_achievements_title", "achievements", ["title"])
    op.alter_column('achievements', 'image_url',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)

    op.execute("INSERT INTO achievements (title, description, image_url) VALUES ('Runner', 'Yay! You have achieved the title of runner', '../img/achievements/unlocked_achievement4.jpeg')")
    op.execute("INSERT INTO achievements (title, description, image_url) VALUES ('Crazy', 'Yaaaahaaa, WOwhooo, beepee beepee', '../img/achievements/unlocked_achievement3.jpeg')")
    op.execute("INSERT INTO achievements (title, description, image_url) VALUES ('Local', 'You must know all the locals by now - you are always running around!', '../img/achievements/unlocked_achievement5.jpeg')")
    op.execute("INSERT INTO achievements (title, description, image_url) VALUES ('Adventurer', 'Walk through the same route everyday? Thats not for you - congratulations, you have acquired the adventurer badge', '../img/achievements/unlocked_achievement6.jpeg')")
    op.execute("INSERT INTO achievements (title, description, image_url) VALUES ('Inspired', 'You have been biking everyday since 1993! That deserves a celebrtion!','../img/achievements/unlocked_achievement7.jpeg')")
    op.execute("INSERT INTO achievements (title, description, image_url) VALUES ('Forest Gump', 'Run Forest, RUN!', '../img/achievements/unlocked_achievement8.jpeg')")


    ### end Alembic commands ###


def downgrade():
    pass
