"""Added ON DELETE CASCADE to foreign keys

Revision ID: 34949dc48a66
Revises: 52a5e947a08d
Create Date: 2013-03-16 05:28:25.420229

"""

# revision identifiers, used by Alembic.
revision = '34949dc48a66'
down_revision = '52a5e947a08d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_constraint("unlocked_achievements_athlete_id_fkey", "unlocked_achievements")
    op.drop_constraint("unlocked_achievements_achievement_id_fkey", "unlocked_achievements")
    op.create_foreign_key("unlocked_achievements_athlete_id_fkey", "unlocked_achievements",
            "athletes", ["athlete_id"], ["id"], ondelete="CASCADE");
    op.create_foreign_key("unlocked_achievements_achievement_id_fkey", "unlocked_achievements",
            "athletes", ["athlete_id"], ["id"], ondelete="CASCADE");

    op.drop_constraint("activities_athlete_id_fkey", "activities")
    op.create_foreign_key("activities_athlete_id_fkey", "activities", "athletes",
            ["athlete_id"], ["id"], ondelete="CASCADE");

    op.drop_constraint("goals_athlete_id_fkey", "goals")
    op.create_foreign_key("goals_athlete_id_fkey", "goals", "athletes",
            ["athlete_id"], ["id"], ondelete="CASCADE");

    op.drop_constraint("health_athlete_id_fkey", "health")
    op.create_foreign_key("health_athlete_id_fkey", "health", "athletes",
            ["athlete_id"], ["id"], ondelete="CASCADE");

    op.drop_constraint("health_athlete_id_fkey", "health")
    op.create_foreign_key("health_athlete_id_fkey", "health", "athletes",
            ["athlete_id"], ["id"], ondelete="CASCADE");

def downgrade():
    pass
