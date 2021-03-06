"""Insert column for title

Revision ID: 2f30ddaa501b
Revises: 5373c447ddf5
Create Date: 2018-02-06 12:01:52.591327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f30ddaa501b'
down_revision = '5373c447ddf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitch', 'title')
    # ### end Alembic commands ###
