"""users table

Revision ID: 487c19a9c093
Revises: 
Create Date: 2020-04-30 16:30:48.728180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '487c19a9c093'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('address1', sa.String(length=128), nullable=True),
    sa.Column('address2', sa.String(length=128), nullable=True),
    sa.Column('street', sa.String(length=128), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('postal_code', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_address1'), 'company', ['address1'], unique=False)
    op.create_index(op.f('ix_company_address2'), 'company', ['address2'], unique=False)
    op.create_index(op.f('ix_company_city'), 'company', ['city'], unique=False)
    op.create_index(op.f('ix_company_country'), 'company', ['country'], unique=False)
    op.create_index(op.f('ix_company_name'), 'company', ['name'], unique=True)
    op.create_index(op.f('ix_company_postal_code'), 'company', ['postal_code'], unique=False)
    op.create_index(op.f('ix_company_street'), 'company', ['street'], unique=False)
    op.create_table('user',
    sa.Column('user_number', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('designation', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('user_number')
    )
    op.create_index(op.f('ix_user_designation'), 'user', ['designation'], unique=False)
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=False)
    op.create_index(op.f('ix_user_user_id'), 'user', ['user_id'], unique=True)
    op.create_table('company_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('financial_year', sa.Integer(), nullable=True),
    sa.Column('annual_sales', sa.Integer(), nullable=True),
    sa.Column('book_value_equity', sa.Integer(), nullable=True),
    sa.Column('total_current_assets', sa.Integer(), nullable=True),
    sa.Column('total_current_liabilities', sa.Integer(), nullable=True),
    sa.Column('earnings_before_interest_tax', sa.Integer(), nullable=True),
    sa.Column('retained_earnings', sa.Integer(), nullable=True),
    sa.Column('BRS', sa.Integer(), nullable=True),
    sa.Column('BRZ', sa.String(length=64), nullable=True),
    sa.Column('company_name', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['company_name'], ['company.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_data_BRS'), 'company_data', ['BRS'], unique=False)
    op.create_index(op.f('ix_company_data_BRZ'), 'company_data', ['BRZ'], unique=False)
    op.create_index(op.f('ix_company_data_annual_sales'), 'company_data', ['annual_sales'], unique=False)
    op.create_index(op.f('ix_company_data_book_value_equity'), 'company_data', ['book_value_equity'], unique=False)
    op.create_index(op.f('ix_company_data_earnings_before_interest_tax'), 'company_data', ['earnings_before_interest_tax'], unique=False)
    op.create_index(op.f('ix_company_data_financial_year'), 'company_data', ['financial_year'], unique=True)
    op.create_index(op.f('ix_company_data_retained_earnings'), 'company_data', ['retained_earnings'], unique=False)
    op.create_index(op.f('ix_company_data_total_current_assets'), 'company_data', ['total_current_assets'], unique=False)
    op.create_index(op.f('ix_company_data_total_current_liabilities'), 'company_data', ['total_current_liabilities'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_company_data_total_current_liabilities'), table_name='company_data')
    op.drop_index(op.f('ix_company_data_total_current_assets'), table_name='company_data')
    op.drop_index(op.f('ix_company_data_retained_earnings'), table_name='company_data')
    op.drop_index(op.f('ix_company_data_financial_year'), table_name='company_data')
    op.drop_index(op.f('ix_company_data_earnings_before_interest_tax'), table_name='company_data')
    op.drop_index(op.f('ix_company_data_book_value_equity'), table_name='company_data')
    op.drop_index(op.f('ix_company_data_annual_sales'), table_name='company_data')
    op.drop_index(op.f('ix_company_data_BRZ'), table_name='company_data')
    op.drop_index(op.f('ix_company_data_BRS'), table_name='company_data')
    op.drop_table('company_data')
    op.drop_index(op.f('ix_user_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_designation'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_company_street'), table_name='company')
    op.drop_index(op.f('ix_company_postal_code'), table_name='company')
    op.drop_index(op.f('ix_company_name'), table_name='company')
    op.drop_index(op.f('ix_company_country'), table_name='company')
    op.drop_index(op.f('ix_company_city'), table_name='company')
    op.drop_index(op.f('ix_company_address2'), table_name='company')
    op.drop_index(op.f('ix_company_address1'), table_name='company')
    op.drop_table('company')
    # ### end Alembic commands ###
