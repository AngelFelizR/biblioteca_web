from sqlalchemy import create_engine, text

conn_str = r"mssql+pymssql://sa:Pass123!@mssql2025:1433/BibliotecaDB?charset=utf8&tds_version=7.4"

try:

    engine = create_engine(conn_str)

    if __name__ == "__main__":
        with engine.connect() as conn:
            result = conn.execute(text("SELECT @@version AS Version")).all()[0]
            sql_version = str(result).split("\\n")[0].strip().replace("(","", count = 1)
            print("Conexión exitosa:", sql_version)

except Exception as e:
    
    print("Error:", e)