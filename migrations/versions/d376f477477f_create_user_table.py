"""create_user_entity_table

Revision ID: d376f477477f
Revises: c8fff73b87c6
Create Date: 2022-03-13 02:18:47.324857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd376f477477f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column('mac', sa.String(120), nullable=False, unique=True),
        sa.Column('name', sa.String(120), index=True, nullable=False),
        sa.Column('email', sa.String(120), nullable=False, unique=True),
        sa.Column('key', sa.String(120), nullable=False, unique=True),
        sa.Column('teste', sa.String(120), nullable=False, unique=True),
        sa.Column('validity', sa.String(120), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    )


def downgrade():
    op.drop_table('user')
