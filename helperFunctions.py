#finds if the userID exists by seeing if it returns anything when selecting
def userIDExists(cursor, userID):
    try:
        userID = int(userID)
    except:
        return False

    query = """
    SELECT *
    FROM USER_T
    WHERE User_id = %s;
    """

    cursor.execute(query, (userID,))
    result = cursor.fetchone()

    if result is None:
        return False
    else:
        return True

#finds if serving name exists in a similar way to the userID
def servingNameExists(cursor, servingName):
    query = """
    SELECT *
    FROM SERVING
    WHERE S_name = %s;
    """
    
    cursor.execute(query, (servingName,))
    result = cursor.fetchone()

    if result is None:
        return False
    else:
        return True

#finds if date exists in a similar way to servingNameExists and userIDExists
def dateExistsinUserLog(cursor, userID, date):
    query = """
    SELECT *
    FROM LOG
    WHERE U_id = %s AND Log_date = %s;
    """

    cursor.execute(query, (userID, date))
    result = cursor.fetchall()

    if result is None:
        return False
    else:
        return True

#finds the next log number for a user
def findLogNumber(cursor, userID):
    query = """
    SELECT MAX(Log_num) AS maxLogNum
    FROM LOG
    WHERE U_id = %s;
    """

    cursor.execute(query, (userID,))
    result = cursor.fetchone()

    if result and result[0] is not None:
        log = int(result[0]) + 1
    else:
        log = 1
    return log