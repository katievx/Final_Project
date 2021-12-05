
from os import read
import pandas as pd

def cookie():
    cookie_df = pd.read_csv("cookies.csv", sep = ",", encoding = "UTF-8")
    #print(cookie_df.head(10))
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
    
    print(cookies_and_cakes_df.head(20))
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
     user_i = input("Which option would you like: a list or graph?").lower()
     return user_i
    
def list_options(user_i, calorie_rank, baketime_rank, servingsize_rank):
    if user_i == "list":
        user_2 = input("What would you like the dataframe listed by: calories, bake time, or serving size?").lower()
        if user_2 == "calories":
            print(calorie_rank)
        if user_2 == "bake time":
            print(baketime_rank)
        if user_2 == "serving size":
            print(servingsize_rank)
        else:
            #does it still allow for input
            print(user_2)

def graphs():
    
    
    if user_i == "graph":
        user_2 == input("Do you want to see a histogram or bar graph?").lower()
        if user_2 == "bar graph":
            print("We have a graph for vegan friendly recipes and a graph for peanut-allergy friendly recipes")
            user_3 = input("Which would graph you like to see: vegan or peanut?").lower()
            if user_3 == "vegan":
                #insert graph
            if user_3 == "peanut":
                #call graph
            else:
                user_3

        
  #  else:
  #      print("We don't have that option!")
  #      return user_i
        
 
if __name__ == "__main__":
    read_cook = cookie()
    read_cake = cake()
    cal_per_serving_size(read_cook, read_cake)
    
    cal_df = cal_per_serving_size(read_cook, read_cake)
    sort(cal_df)