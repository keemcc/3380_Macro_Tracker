from datetime import datetime
from helperFunctions import userIDExists, dateExistsinUserLog

def foodsOnDate(cursor):
    userID = input("Enter a user ID: ")
    while (True):
        if userIDExists(cursor, userID):
            break
        elif userID == "-1":
            return
        else:
            userID=input('UserID does not exist. Please try again or type "-1" to exit: ')

    userInput = input("Enter a date (YYYY-MM-DD): ")
    while True:
        if (userInput == "-1"):
            return
        try:
            date = datetime.strptime(userInput, "%Y-%m-%d")
        except:
            userInput=input('Date is invalid. Please try again or type "-1" to exit: ')
        if dateExistsinUserLog(cursor, userID, date):
            break
        else:
            userInput=input('Date doesn\'t exist in user log. Please try another or type "-1" to exit: ')
    
    logQuery = """
    SELECT S_name
    FROM LOG
    WHERE U_id = %s AND Log_date = %s;
    """
    cursor.execute(logQuery, (userID, date))
    logRows = cursor.fetchall()

    foodNamesSet = set()
    for row in logRows:
        servingName = row[0]

        servingQuery = """
        SELECT F_id
        FROM SERVING
        WHERE S_name = %s;
        """

        cursor.execute(servingQuery, (servingName,))
        servingRow = cursor.fetchone()

        if servingRow is None:
            print(f"Error, {servingName} was not found.")
            return
        
        foodID = servingRow[0]

        foodQuery = """
        SELECT F_name
        FROM FOOD
        WHERE F_id = %s
        """

        cursor.execute(foodQuery, (foodID,))
        foodRow = cursor.fetchone()

        if foodRow is None:
            print(f"Error, food with ID = {foodID} was not found.")
            return
        
        foodNamesSet.add(foodRow[0])
    
    foodNames = list(foodNamesSet)
    print("")
    if (len(foodNames) == 0):
        print(f"User {userID} did not track any foods on {date.date()}", end="")
    elif (len(foodNames) == 1):
        print(f"User {userID} tracked {foodNames[0]} on {date.date()}", end="")
    else:
        print(f"User {userID}'s foods tracked on {date.date()} were")
        for foodName in foodNames[:-1]:
            print(f"{foodName}, ", end="")
        print(f"and {foodNames[-1]}", end="")
    print(".")