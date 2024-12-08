def createDB(cursor):
    try:
        cursor.execute("DROP SCHEMA MACRO_TRACKER;")
    except:
        print("Doesn't exist")
    
    cursor.execute("CREATE SCHEMA MACRO_TRACKER;")
    cursor.execute("USE MACRO_TRACKER;")
    cursor.execute("""
    CREATE TABLE USER_T (
        User_id INT NOT NULL,
        Weight INT NOT NULL,
        Birth_date DATE NOT NULL,
        PRIMARY KEY (User_id)
    );
    """)
    cursor.execute("""
    CREATE TABLE BRAND (
        B_id INT NOT NULL,
        B_name VARCHAR(100) NOT NULL,
        PRIMARY KEY (B_id)
    );
    """)
    cursor.execute("""
    CREATE TABLE FOOD (
        F_id INT NOT NULL,
        F_name VARCHAR(100) NOT NULL,
        Default_grams INT NOT NULL,
        Carbs INT NOT NULL,
        Fat INT NOT NULL,
        Protein INT NOT NULL,
        Calories INT NOT NULL,
        B_id INT NOT NULL,
        PRIMARY KEY (F_id),
        FOREIGN KEY (B_id)
            REFERENCES BRAND (B_id)
    );
    """)
    cursor.execute("""
    CREATE TABLE SERVING (
        S_name VARCHAR(100) NOT NULL,
        S_grams INT NOT NULL,
        F_id INT NOT NULL,
        PRIMARY KEY (S_name),
        FOREIGN KEY (F_id)
            REFERENCES FOOD (F_id)
    );
    """)
    cursor.execute("""
    CREATE TABLE LOG (
        U_id INT NOT NULL,
        Log_num INT NOT NULL,
        Log_date DATE NOT NULL,
        S_name VARCHAR(100) NOT NULL,
        FOREIGN KEY (U_id)
            REFERENCES USER_T (User_id),
        FOREIGN KEY (S_name)
            REFERENCES SERVING (S_name),
        CONSTRAINT PK_LOG PRIMARY KEY (U_id , Log_num)
    );
    """)
    cursor.execute("""
    CREATE TABLE FITNESS_GOAL (
        Fitness_goal VARCHAR(100) NOT NULL,
        User_id INT NOT NULL,
        FOREIGN KEY (User_id)
            REFERENCES USER_T (User_id),
        CONSTRAINT PK_FITNESS_GOAL PRIMARY KEY (Fitness_goal , User_id)
    );
    """)

def insertData(cursor):
    cursor.execute("""
    INSERT INTO USER_T (User_id, Weight, Birth_date) 
    VALUES 
        (1, 70, '1990-05-14'),
        (2, 85, '1985-03-22'),
        (3, 62, '2000-11-05');
    """)
    cursor.execute("""
    INSERT INTO BRAND (B_id, B_name) 
    VALUES 
        (1, 'Brand A'),
        (2, 'Brand B'),
        (3, 'Brand C');
    """)
    cursor.execute("""
    INSERT INTO FOOD (F_id, F_name, Default_grams, Carbs, Fat, Protein, Calories, B_id) 
    VALUES 
        (1, 'Oatmeal', 100, 50, 3, 6, 200, 1),
        (2, 'Chicken Breast', 100, 0, 2, 31, 165, 2),
        (3, 'Avocado', 100, 9, 15, 2, 160, 3);
    """)
    cursor.execute("""
    INSERT INTO SERVING (S_name, S_grams, F_id) 
    VALUES 
        ('Small Bowl of Oatmeal', 50, 1),
        ('Medium Bowl of Oatmeal', 100, 1),
        ('Large Bowl of Oatmeal', 150, 1),
        ('Single Piece of Chicken Breast', 100, 2),
        ('Half Avocado', 50, 3);
    """)
    cursor.execute("""
    INSERT INTO LOG (U_id, Log_num, Log_date, S_name) 
    VALUES 
        (1, 1, '2024-12-01', 'Small Bowl of Oatmeal'),
        (1, 2, '2024-12-02', 'Single Piece of Chicken Breast'),
        (2, 1, '2024-12-03', 'Half Avocado'),
        (3, 1, '2024-12-04', 'Medium Bowl of Oatmeal');
    """)
    cursor.execute("""
    INSERT INTO FITNESS_GOAL (Fitness_goal, User_id) 
    VALUES 
        ('Weight Loss', 1),
        ('Muscle Gain', 2),
        ('Maintain Weight', 3);
    """)