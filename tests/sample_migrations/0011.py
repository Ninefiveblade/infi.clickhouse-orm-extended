from infi.clickhouse_orm_extended import migrations
from ..test_migrations import *

operations = [
    migrations.AlterTableWithBuffer(Model4Buffer_changed)
]
