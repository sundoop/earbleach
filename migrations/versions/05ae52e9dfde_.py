"""empty message

Revision ID: 05ae52e9dfde
Revises: 25d2bcafece3
Create Date: 2016-03-18 23:08:51.178836

"""

# revision identifiers, used by Alembic.
revision = '05ae52e9dfde'
down_revision = '25d2bcafece3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'worms', ['title'])
    op.create_unique_constraint(None, 'worms', ['url'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'worms', type_='unique')
    op.drop_constraint(None, 'worms', type_='unique')
    ### end Alembic commands ###
