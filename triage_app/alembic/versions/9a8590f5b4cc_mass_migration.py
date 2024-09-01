"""mass migration

Revision ID: 9a8590f5b4cc
Revises: 523b6a0f5e8d
Create Date: 2024-06-24 12:58:26.431551

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a8590f5b4cc'
down_revision: Union[str, None] = '523b6a0f5e8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('agents', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))

    with op.batch_alter_table('tickets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('group_id', sa.Integer(), nullable=True))
        batch_op.drop_column('team_id')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tickets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('team_id', sa.INTEGER(), nullable=False))
        batch_op.drop_column('group_id')

    with op.batch_alter_table('agents', schema=None) as batch_op:
        batch_op.drop_column('updated')

    # ### end Alembic commands ###
