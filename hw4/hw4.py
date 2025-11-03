import pandas as pd

# 1050
def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].size().reset_index()
    return actor_director[actor_director.timestamp >= 3].iloc[:,[0,1]]

# 1667
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')

# 175
def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = person.merge(address, on='personId', how='left')
    result = result[['firstName', 'lastName', 'city', 'state']]
    return result

# 176
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salary = employee['salary'].drop_duplicates().nlargest(2)
    if len(salary) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    return pd.DataFrame({'SecondHighestSalary': [salary.iloc[1]]})
