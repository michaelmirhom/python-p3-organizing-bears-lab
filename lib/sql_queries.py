select_all_female_bears_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE sex='F';
"""


select_all_bears_names_and_orders_in_alphabetical_order = """
Select  name from  bears ORDER BY bears.name   ASC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT bears.name, bears.age   from bears WHERE alive =1 order by bears.age  asc;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT bears.name , bears.age FROM bears ORDER BY bears.age DESC LIMIT 1; 
"""
select_youngest_bear_and_returns_name_and_age = """
    SELECT bears.name, bears.age from bears ORDER BY bears.age ASC LIMIT 1;
"""