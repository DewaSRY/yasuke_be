from pathlib import Path
import os
import logging

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from app.libs import sql_alchemy_lib

"""
##################################################################################
#########Import all Your model Here so Alembic will know the model is exists######
##################################################################################
"""
from app.user.user_model import UserModel
from app.health_check.health_check_model import HealthCheckModel

"""
##################################################################################
#########Import all Your model Here so Alembic will know the model is exists######
##################################################################################
"""

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = sql_alchemy_lib.Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


# MYSQL_CONNECTOR = os.environ.get("SQLALCHEMY_DATABASE_URL")
# DB_path = str((Path().parent / "sql_app.db").resolve())
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# config.set_main_option("sqlalchemy.url", f"sqlite:///{DB_path}")
config.set_main_option("sqlalchemy.url", sql_alchemy_lib.MYSQL_CONNECTOR)
logger = logging.getLogger('alembic')
logger.info(f"Using database URL: {sql_alchemy_lib.MYSQL_CONNECTOR}")


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
