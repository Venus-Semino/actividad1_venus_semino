from database.database import get_connection

# ==================================================
# ALUMNOS
# ==================================================


# CREATE
def crear_alumno(nombre):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        INSERT INTO alumnos (nombre)
        VALUES (%s)
        RETURNING id, nombre;
    """

    cursor.execute(sql, (nombre,))

    alumno = cursor.fetchone()

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "id": alumno[0],
        "nombre": alumno[1]
    }



# RETRIEVE - TODOS
def obtener_alumnos():
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        SELECT id, nombre
        FROM alumnos
        ORDER BY id;
    """

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    connection.close()

    alumnos = []

    for alumno in resultados:
        alumnos.append({
            "id": alumno[0],
            "nombre": alumno[1]
        })

    return alumnos

# RETRIEVE - UNO
def obtener_alumno(alumno_id):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        SELECT id, nombre
        FROM alumnos
        WHERE id = %s;
    """

    cursor.execute(sql, (alumno_id,))

    alumno = cursor.fetchone()

    cursor.close()
    connection.close()

    if alumno is None:
        return None

    return {
        "id": alumno[0],
        "nombre": alumno[1]
    }

# UPDATE
def actualizar_alumno(alumno_id, nombre):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        UPDATE alumnos
        SET nombre = %s
        WHERE id = %s
        RETURNING id, nombre;
    """

    cursor.execute(sql, (nombre, alumno_id))

    alumno = cursor.fetchone()

    connection.commit()

    cursor.close()
    connection.close()

    if alumno is None:
        return None

    return {
        "id": alumno[0],
        "nombre": alumno[1]
    }


# DELETE
def eliminar_alumno(alumno_id):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        DELETE FROM alumnos
        WHERE id = %s
        RETURNING id, nombre;
    """

    cursor.execute(sql, (alumno_id,))

    alumno = cursor.fetchone()

    connection.commit()

    cursor.close()
    connection.close()

    if alumno is None:
        return None

    return {
        "id": alumno[0],
        "nombre": alumno[1]
    }
