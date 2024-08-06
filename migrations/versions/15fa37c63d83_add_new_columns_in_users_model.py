"""Add new columns in users model

Revision ID: 15fa37c63d83
Revises: da2867bc8f2e
Create Date: 2024-08-06 22:03:14.834523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.libs.sql_alchemy_lib import Base

# revision identifiers, used by Alembic.
revision: str = '15fa37c63d83'
down_revision: Union[str, None] = 'da2867bc8f2e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fullname', sa.String(length=50), nullable=True))
    op.add_column('users', sa.Column('phone', sa.String(length=20), nullable=True))
    op.add_column('users', sa.Column('profession', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('address', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('photo', sa.String(), nullable=True))
    op.add_column('users', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.create_index(op.f('ix_users_fullname'), 'users', ['fullname'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_fullname'), table_name='users')
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'photo')
    op.drop_column('users', 'address')
    op.drop_column('users', 'profession')
    op.drop_column('users', 'phone')
    op.drop_column('users', 'fullname')
    # ### end Alembic commands ###
