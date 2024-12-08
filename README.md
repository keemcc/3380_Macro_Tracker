Function: Track_food 

//This function will track food and food weight for a user on a certain day. It will 	access the “LOG” table. 

Input: User_id, Date, S_name. Input the user ID, date, and serving name. 

Steps: 

1. Check LOG table with User_id as U_id to see how many logs have been made. 

2. Create new row in LOG with U_id as input User_id, Log_num as the number of existing logs + 1, Date as the input date, and S_name as the input S_name. 

 

Function: Calories_on_date 

//This function will return the number of calories logged for a certain user on a 	certain day. It will access the “LOG”, “SERVING”, and “FOOD” tables. 

Input: User_id, Date. Input the user ID and date to check. 

Steps: 

Check LOG table for every row with U_id equal to passed User_id and Date equal to passed date. 

For each instance of both conditions being met enter the SERVING table and search for S_name equal to S_name of LOG row. 

Using F_id and S_grams from SERVING row, find row in FOOD with same F_id. 

User S_grams divided by Default_grams to find serving size, in FOOD row, then calculate number of calories in the serving by multiplying by the serving size. 

Add number of calories to total. 

Repeat for all rows in LOG with U_id equal to User_id and Date equal to Date. 

Return the total Calories. 

  

 

Function: Foods_on_date 

//This function will return a list of all foods tracked by a certain user on a certain 	date. It will access the “LOG”, “SERVING”, and “FOOD” tables. 

Input: User_id, Date. Input the user ID and date to check. 

Steps: 

1. Check LOG table for every row with U_id equal to passed ID and Date equal to 	passed date. 

2. For each LOG row with these conditions met, use S_name in the row to find 	S_name row in the SERVING table. 

3. Where this condition is met, use F_id in the row and find F_id in the FOOD table. 

4. Return each F_name when all conditions are met.	 