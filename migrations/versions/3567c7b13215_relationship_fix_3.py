"""RELATIONSHIP-FIX-3

Revision ID: 3567c7b13215
Revises: a46478a00224
Create Date: 2023-12-12 00:43:06.882303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3567c7b13215'
down_revision: Union[str, None] = 'a46478a00224'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
