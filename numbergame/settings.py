from sqlalchemy import create_engine

MysqlConf = {
    'engine': 'mysql+mysqlconnector',
    'pool_size': 20,
    'pool_recycle': 30,
    'debug': False,
    'username': '',
    'password': '',
    'host': '',
    'port': 3306,
    'db_name': 'ng',
}

SQLALCHEMY = {
    'debug': False,
}

engine = create_engine(
    '{engine}://{username}:{password}@{host}:{port}/{db_name}'.format(
        **MysqlConf
    ),
    pool_size=MysqlConf['pool_size'],
    echo=SQLALCHEMY['debug'],
    pool_timeout=20,
    pool_recycle=259,
    pool_pre_ping=True,
    pool_reset_on_return=None,
    isolation_level="READ COMMITTED"
)
