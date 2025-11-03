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

# 1327
def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    february_2020_orders = orders[orders['order_date'].dt.year == 2020]
    february_2020_orders = february_2020_orders[orders['order_date'].dt.month == 2]
    merged = pd.merge(february_2020_orders, products, on='product_id')

    result = merged.groupby('product_name')['unit'].sum().reset_index()
    result = result[result['unit'] >= 100]
    
    return result[['product_name', 'unit']]

# 1378
def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(employees, employee_uni, how='left', on='id')[['unique_id', 'name']]

# 550
def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity["first_day"] = activity.groupby(["player_id"])[["event_date"]].transform("min")
    activity["is_day"] = (activity.event_date - activity.first_day).dt.total_seconds() == 86400
    df = activity[activity['is_day']]

    return pd.DataFrame({"fraction":[round(df.player_id.nunique() / activity.player_id.nunique(),2)]})
    
# 1075
def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:

    merged = project.merge(employee, on = 'employee_id', how = 'inner')
    grouped = merged.groupby('project_id').agg(average_years = ('experience_years', 'mean')).reset_index()
    grouped['average_years'] = grouped['average_years'].round(2)
    
    return grouped

# 185
def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    duplicate =employee.drop_duplicates(["salary","departmentId"])
    df_sorted = duplicate.sort_values(by=["salary"], ascending= False)
    df_groupby = df_sorted.groupby("departmentId").head(3)
    df = employee.merge(department, how ="left", left_on = "departmentId",right_on = "id")
    merging = df.merge(df_groupby[["salary","departmentId"]], how ="inner", on = ["departmentId","salary"])
    merging =  merging.rename(columns ={"name_y":"Department", "name_x": "Employee", "salary":"Salary"})
    
    return merging[["Department","Employee", "Salary"]]
