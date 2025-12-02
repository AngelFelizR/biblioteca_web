import sqlalchemy as sa

conn_str = (
    "mssql+pymssql://sa:Pass123%21@mssql2025:1433/master?charset=utf8&tds_version=7.4"
)

try:
    engine = sa.create_engine(conn_str)
    with engine.connect() as conn:
        result = conn.execute(sa.text("SELECT @@version")).fetchone()
        print("Conexión exitosa:", result)
except Exception as e:
    print("Error:", e)


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
with Session() as session:
    result = session.execute(sa.text("SELECT * FROM sys.databases")).fetchall()
    print(result)
