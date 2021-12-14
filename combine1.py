
import pandas as pd
import matplotlib.pyplot as plt 

def cookie():
    cookie_df = pd.read_csv("cookies.csv", sep = ",", encoding = "UTF-8")
    return cookie_df
def cake():
    cake_df = pd.read_csv("cakes.csv", sep = ",", encoding = "UTF-8")
    return cake_df

def cal_per_serving_size(cookie_df, cake_df): 
    """ 
    A function that creates a dataframe that includes all the recipes,
    and then adds a column for the calories per each cookie and cake slice 
    
    Side effects:
        Creates a new dataframe
        Modifies the new dataframe by adding new column 
    """
    cookies_and_cakes_df = pd.concat([cookie_df, cake_df])
    for line in cookies_and_cakes_df:
        if cookies_and_cakes_df["Serving Size"] == 0 or cookies_and_cakes_df["Serving Size"] == None:
            print(f"Please replace {line} with a non-zero or non-empty value!")
            break
        else:
            cookies_and_cakes_df["Calories per cookie or slice"] =  cookies_and_cakes_df["Calories"] / cookies_and_cakes_df["Serving Size"]
    
    print(cookies_and_cakes_df)
    return cookies_and_cakes_df


def sort(cookies_and_cakes_df):
   """Orders the dataframe by different categories, including:
       calories, bake time, and serving size
   """
   sort.calorie_rank = cookies_and_cakes_df.sort_values(["Calories"])
   sort.baketime_rank = cookies_and_cakes_df.sort_values(["Bake Time (minutes)"])
   sort.servingsize_rank = cookies_and_cakes_df.sort_values(["Serving Size"])
   return (sort.calorie_rank, sort.baketime_rank, sort.servingsize_rank)
   
def bars(cookies_and_cakes_df):
    calories_bar = cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Calories')
    servingsize_bar = cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Serving Size')
    baketime_bar = cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Bake Time (minutes)')
    return (calories_bar, servingsize_bar, baketime_bar)

def hists(cookies_and_cakes_df):
    calories_g = cookies_and_cakes_df.hist("Calories")
    servingsize_g = cookies_and_cakes_df.hist("Serving size")
    baketime_g = cookies_and_cakes_df.hist("Bake Time (minutes)")
    return (calories_g, servingsize_g, baketime_g)


def user_input():
     print("You can also sort the database by certian columns (from lowest to highest) by choosing to see a list.")
     print("Or, view a graphical display of some columns by choosing see to a graph.")
     user_1 = input("Which option would you like: a list or graph?").lower()
     return user_1

         
def list_options(user_1, calorie_rank, baketime_rank, servingsize_rank):
    if user_1 == "list":
        while True:
            user_2 = input("What would you like the dataframe listed by: calories, bake time, or serving size?").lower()
            if user_2 == "calories":
                print(calorie_rank)
                break
            if user_2 == "bake time":
                print(baketime_rank)
                break
            if user_2 == "serving size":
                print(servingsize_rank)
                break
            else:
                print("We don't have that option! Please input either 'calories', 'serving size', or 'bake time' ")  


def bar_options(user_1, calories_bar, servingsize_bar, baketime_bar):
    if user_1 == "graph":
        user_2 = input("Do you want to see a histogram or bar graph?").lower()
        while True:
            if user_2 == "bar graph":
                user_3 = input("What would you like the bar graph listed by: calories, bake time, or serving size?").lower()
                if user_3 == "calories":
                    print(calories_bar)
                    break
                if user_3 == "bake time":
                    print(baketime_bar)
                    break
                if user_3 == "serving size":
                    print(servingsize_bar)
                    break
                else:
                    print("We don't have that option! Please input either 'calories', 'serving size', or 'bake time' ")
        return user_2
                
                           
def hist_options(user_2, calories_g, servingsize_g, baketime_g):
        if user_2 == "histogram":
            user_3 = "What would you like a histogram for: calories, serving size, or bake time?".lower()
            if user_3 == "calories":
                print(calories_g)
            if user_3 == "serving size":
                print(servingsize_g)
            if user_3 == "bake time":
                print(baketime_g)
            else:
                print("We don't have that option! Please input either 'calories', 'serving size', or 'bake time' ")

    
    
                
def main(file1, file2):    
    read_cook = cookie()
    read_cake = cake()
    cal_per_serving_size(read_cook, read_cake)
    
    cal_df = cal_per_serving_size(read_cook, read_cake)
    sort(cal_df)
    
    user_info = user_input()
    
    sort1 = sort.calorie_rank
    sort2 = sort.baketime_rank
    sort3 = sort.servingsize_rank
    list_options(user_info,sort1, sort2, sort3)
    
 
if __name__ == "__main__":
    main()

