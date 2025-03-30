# Restaurant_Jiho_App
App for restaurant business

Our friend Jiho is trying to get into the restaurant business. He asked us to build a simple table assignment program to help manage which customer is assigned to each table in the restaurant. 
Jiho wants to store not only the name of the customer for the table but also if they hold a VIP status (earned by visiting the restaurant frequently).
Jiho wants to expand application to also take orders from customers.

Jiho is having a lot of success with our restaurant application. Unfortunately, our original design did not account for storing orders for each specific table. 
Jiho asked us to adjust our application to be able to store the orders that come in for each specific table and also be able to print out the order for the kitchen staff.

Jiho is pleased with how we can store orders for our tables. However, the staff now wants to distinguish between food items and drinks.
Since food items get prepared in the kitchen and drinks are prepared at the bar, it’s important to distinguish between the two in our application.
The tables dictionary has been changed to support the staff’s requests.

Jiho thinks our restaurant application is missing one really important feature. Jiho would like for the application to be able to calculate the total bill of a table (including tip) and split it based on the number of people at the table. 

Here is some additional functionality that Jiho might like:

    -The ability to remove a table’s guests when they leave the restaurant.
    -An adjustment to the calculate_price_per_person() function to access a tables 'total' and return the result.
    -The ability to add and remove order items for both food and drinks if there is ever a mistake.
    -The ability to queue reservations for later times for specific tables.
