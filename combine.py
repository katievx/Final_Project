
from os import read
import pandas as pd
import matplotlib.pyplot as plt 

def cookie():
    cookie_df = pd.read_csv("cookies.csv", sep = ",", encoding = "UTF-8")
    return cookie_df
def cake():
    cake_df = pd.read_csv("cakes.csv", sep = ",", encoding = "UTF-8")
    return cake_df
    #print(cake_df.head(10))

def cal_per_serving_size(cookie_df, cake_df): 
    """ 
    A function that creates a dataframe that includes all the recipes,
    and then adds a column for the calories per each cookie and cake slice
    
    Side effects:
        Creates a new dataframe
        Modifies the new dataframe by adding new column 
    """
    cookies_and_cakes_df = pd.concat([cookie_df, cake_df])
    cookies_and_cakes_df["Calories per cookie or slice"] =  cookies_and_cakes_df["Calories"] / cookies_and_cakes_df["Serving Size"]
    
    print(cookies_and_cakes_df)
    return cookies_and_cakes_df

def sort(cookies_and_cakes_df):
   """Sort the dataframe by different categories, including:
       calories, bake time, and serving size
   """
   calorie_rank = cookies_and_cakes_df["Calories"].sort_values()
   baketime_rank = cookies_and_cakes_df["Bake Time (minutes)"].sort_values()
   servingsize_rank = cookies_and_cakes_df["Serving Size"].sort_values()
   
   print(calorie_rank, baketime_rank, servingsize_rank)
   return (calorie_rank, baketime_rank, servingsize_rank)
   
def user_input():
     print("If you would like, you can sort the database by certian columns.")
     print("We also have the option of displaying the recipes by vegan vs peanut-allergy friendly!")
     user_1 = input("Which option would you like: a list or graph?").lower()
     return user_1
    
def list_options(user_1, calorie_rank, baketime_rank, servingsize_rank):
    if user_1 == "list":
        user_2 = input("What would you like the dataframe listed by: calories, bake time, or serving size?").lower()
        if user_2 == "calories":
            print(calorie_rank)
        if user_2 == "bake time":
            print(baketime_rank)
        if user_2 == "serving size":
            print(servingsize_rank)
        else:
            user_2
            #does it still allow for input
            #print(user_2)
    return user_2

def bars(cookies_and_cakes_df):
    calories_bar = cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Calories')
    servingsize_bar = cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Serving Size')
    baketime_bar = cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Bake Time (minutes)')
    
    return(calories_bar, servingsize_bar, baketime_bar)
    
def hists(cookies_and_cakes_df):
    calories_g = cookies_and_cakes_df.hist("Calories")
    servingsize_g = cookies_and_cakes_df.hist("Serving size")
                                           
    baketime_g = cookies_and_cakes_df.hist("Bake Time (minutes)")
   
    return (calories_g, servingsize_g, baketime_g)


def bar_options(user_1, user_2, calories_bar, servingsize_bar, baketime_bar):
    #might have to move line(s) below outside func
    if user_1 == "graph":
        user_2 = input("Do you want to see a histogram or bar graph?").lower()
        if user_2 == "bar graph":
            user_3 = input("What would you like the bar graph listed by: calories, bake time, or serving size?").lower()
            if user_3 == "calories":
                print(calories_bar)
            if user_3 == "bake time":
                print(baketime_bar)
            if user_3 == "serving size":
                print(servingsize_bar)
            else:
                print("We don't have that option! Please input either 'calories', 'serving size', or 'bake time' ")
                user_3
        else:
                print("We don't have that option! Please input either 'bar graph' or 'histogram")
                user_2
                
                           
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
                user_3
                
 
if __name__ == "__main__":
    read_cook = cookie()
    read_cake = cake()
    cal_per_serving_size(read_cook, read_cake)
    
    cal_df = cal_per_serving_size(read_cook, read_cake)
    sort(cal_df)
    
    