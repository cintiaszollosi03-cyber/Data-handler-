from __future__ import annotations

from typing import Any

try:
    import oracledb  # type: ignore
    from oracledb import Connection, DatabaseError  # type: ignore
except ImportError:  # pragma: no cover
    oracledb = None  # type: ignore

    class Connection:  # type: ignore
        pass

    class DatabaseError(Exception):  # type: ignore
        pass


def get_oracle_connection(
    user: str,
    password: str,
    dsn: str,
    lib_dir: str | None = None,
) -> Connection:
    if oracledb is None:
        raise ImportError(
            "oracledb is not installed. Install it to use Oracle export."
        )

    if lib_dir:
        oracledb.init_oracle_client(lib_dir=lib_dir)

    return oracledb.connect(
        user=user,
        password=password,
        dsn=dsn,
    )


def write_workplaces_oracle(
    workplaces: list[Any],
    connection: Connection,
    table_name: str = "workplace",
    create: bool = True,
) -> None:
    cursor = connection.cursor()

    if create:
        try:
            cursor.execute(f"DROP TABLE {table_name} CASCADE CONSTRAINTS PURGE")
        except DatabaseError:
            pass

        cursor.execute(
            f"""
            CREATE TABLE {table_name} (
                ID VARCHAR2(20) PRIMARY KEY,
                NAME VARCHAR2(100),
                LOCATION VARCHAR2(200)
            )
            """
        )

    cursor.executemany(
        f"""
        INSERT INTO {table_name} (id, name, location)
        VALUES (:1, :2, :3)
        """,
        [(w.id, w.name, w.location) for w in workplaces],
    )
    connection.commit()


def write_addresses_oracle(
    addresses: list[Any],
    connection: Connection,
    table_name: str = "address",
    create: bool = True,
) -> None:
    cursor = connection.cursor()

    if create:
        try:
            cursor.execute(f"DROP TABLE {table_name} CASCADE CONSTRAINTS PURGE")
        except DatabaseError:
            pass

        cursor.execute(
            f"""
            CREATE TABLE {table_name} (
                ID VARCHAR2(20) PRIMARY KEY,
                STREET VARCHAR2(200),
                CITY VARCHAR2(100),
                COUNTRY VARCHAR2(100)
            )
            """
        )

    cursor.executemany(
        f"""
        INSERT INTO {table_name} (id, street, city, country)
        VALUES (:1, :2, :3, :4)
        """,
        [(a.id, a.street, a.city, a.country) for a in addresses],
    )
    connection.commit()


def write_people_oracle(
    people: list[Any],
    connection: Connection,
    table_name: str = "person",
    create: bool = True,
) -> None:
    cursor = connection.cursor()

    if create:
        try:
            cursor.execute(f"DROP TABLE {table_name} CASCADE CONSTRAINTS PURGE")
        except DatabaseError:
            pass

        cursor.execute(
            f"""
            CREATE TABLE {table_name} (
                ID VARCHAR2(20) PRIMARY KEY,
                NAME VARCHAR2(100),
                AGE NUMBER(3),
                MALE NUMBER(1),
                WORKPLACE_ID VARCHAR2(20),
                ADDRESS_ID VARCHAR2(20),
                FOREIGN KEY (WORKPLACE_ID) REFERENCES workplace(ID),
                FOREIGN KEY (ADDRESS_ID) REFERENCES address(ID)
            )
            """
        )

    cursor.executemany(
        f"""
        INSERT INTO {table_name}
        (id, name, age, male, workplace_id, address_id)
        VALUES (:1, :2, :3, :4, :5, :6)
        """,
        [
            (
                p.id,
                p.name,
                p.age,
                int(p.male),
                p.workplace.id if p.workplace else None,
                p.address.id if p.address else None,
            )
            for p in people
        ],
    )
    connection.commit()
