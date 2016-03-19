"""empty message

Revision ID: 25d2bcafece3
Revises: None
Create Date: 2016-03-18 18:37:37.172707

"""

# revision identifiers, used by Alembic.
revision = '25d2bcafece3'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('worms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('worms')
    ### end Alembic commands ###
