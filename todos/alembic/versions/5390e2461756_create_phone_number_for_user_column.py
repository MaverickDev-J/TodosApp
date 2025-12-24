"""Create phone number for user column

Revision ID: 5390e2461756
Revises: 
Create Date: 2025-12-16 14:14:59.922410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5390e2461756'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True)) 


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')