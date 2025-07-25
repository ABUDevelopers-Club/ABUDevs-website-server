"""Fresh migration for student model

Revision ID: 714d52a28f9b
Revises: 
Create Date: 2025-06-02 12:34:46.025552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '714d52a28f9b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('track', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('subtitle', sa.String(length=150), nullable=True),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('author', sa.String(length=100), nullable=False),
    sa.Column('author_position', sa.String(length=100), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('hashtags', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('track', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('subtitle', sa.String(length=150), nullable=True),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('venue', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('student_id', sa.String(length=20), nullable=False),
    sa.Column('department', sa.String(length=100), nullable=False),
    sa.Column('current_level', sa.String(length=20), nullable=False),
    sa.Column('tech_experience_level', sa.String(length=50), nullable=False),
    sa.Column('area_of_interest', sa.String(length=200), nullable=False),
    sa.Column('reason_for_joining', sa.Text(), nullable=False),
    sa.Column('abudevs_id', sa.String(length=50), nullable=False),
    sa.Column('registered_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('abudevs_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('student')
    op.drop_table('event')
    op.drop_table('blog')
    # ### end Alembic commands ###
