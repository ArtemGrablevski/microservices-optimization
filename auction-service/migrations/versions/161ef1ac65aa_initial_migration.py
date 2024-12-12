"""initial migration

Revision ID: 161ef1ac65aa
Revises: 
Create Date: 2024-12-10 23:06:26.264951

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "161ef1ac65aa"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "auctions",
        sa.Column("auction_id", sa.UUID(), nullable=False),
        sa.Column("number_of_slots", sa.Integer(), nullable=False),
        sa.Column("entrance_ticket_price", sa.SMALLINT(), nullable=False),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("auction_id"),
    )


def downgrade() -> None:
    op.drop_table("auctions")
