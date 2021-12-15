from argparse import ArgumentParser
import sys
from numpy import NaN
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.parsers import read_csv 


class Recipe:
    
    def __init__(self, cookie_df, cake_df):
        self.cookie_df = pd.read_csv(cookie_df, sep = ",", encoding = "UTF-8")
        self.cake_df = pd.read_csv(cake_df, sep = ",", encoding = "UTF-8")
        self.cookies_and_cakes_df = pd.concat([self.cookie_df, self.cake_df])

    def cal_per_serving_size(self): 
        """ 
        A function that creates a dataframe that includes all the recipes,
        and then adds a column for the calories per each cookie and cake slice 
        
        Side effects:
            Creates a new dataframe
            Modifies the new dataframe by adding new column 
        """
    #    for line in self.cookies_and_cakes_df:
    #        if self.cookies_and_cakes_df["Serving Size"] == NaN:
     #           print(f"Please replace {line} with a non-zero or non-empty value!")
      #          break
       #     else:
        self.cookies_and_cakes_df["Calories per cookie or slice"] =  self.cookies_and_cakes_df["Calories"] / self.cookies_and_cakes_df["Serving Size"]
        
    def sort(self, cookies_and_cakes_df):
        """Orders the dataframe by different categories, including:
        calories, bake time, and serving size
        """
        calorie_rank = cookies_and_cakes_df.sort_values(["Calories"])
        baketime_rank = cookies_and_cakes_df.sort_values(["Bake Time (minutes)"])
        servingsize_rank = cookies_and_cakes_df.sort_values(["Serving Size"])
        return (calorie_rank, baketime_rank, servingsize_rank)
        
    def bars(self):
        self.calories_bar = self.cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Calories')
        servingsize_bar = self.cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Serving Size')
        baketime_bar = self.cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Bake Time (minutes)')
        return (self.calories_bar, self.servingsize_bar, self.baketime_bar)

    def hists(self, cookies_and_cakes_df):
        calories_g = cookies_and_cakes_df.hist("Calories")
        servingsize_g = cookies_and_cakes_df.hist("Serving size")
        baketime_g = cookies_and_cakes_df.hist("Bake Time (minutes)")
        return (calories_g, servingsize_g, baketime_g)

    def user_input(self):
        print("You can also sort the database by certain columns (from lowest to highest) by choosing to see a list.")
        print("Or, view a graphical display of some columns by choosing see to a graph.")
        user_1 = input("Which option would you like: a list or graph?").lower()
        return user_1

def list_options(recipes):
    calorie_rank, baketime_rank, servingsize_rank = recipes.sort()
  #  if user_1 == "list":
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

def bar_options(cookies_and_cakes_df):
 #   if user_1 == "graph":
 #       user_2 = input("Do you want to see a histogram or bar graph?").lower()
    while True:
 #       if user_2 == "bar graph":
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
 #   return user_2
                                    
def hist_options(cookies_and_cakes_df):
    #    if user_2 == "histogram":
        user_3 = "What would you like a histogram for: calories, serving size, or bake time?".lower()
        if user_3 == "calories":
            print(calories_g)
        if user_3 == "serving size":
            print(servingsize_g)
        if user_3 == "bake time":
            print(baketime_g)
        else:
            print("We don't have that option! Please input either 'calories', 'serving size', or 'bake time' ")

def user_choice(user_1):
        if user_1 == "list":
            list_options(cookies_and_cakes_df)
        if user_1 == "graph":
            user_2 = input("Do you want to see a histogpython2ram or bar graph?").lower()
            if user_2 == "bar graph":
                bar_options(cookies_and_cakes_df)
            if user_2 == "histogram":
                hist_options(cookies_and_cakes_df)
        return user_2
                
                
def main(file1, file2):   
    recipes = Recipe(file1, file2)    
    recipes.cal_per_serving_size()

    user_c = recipes.user_input()
    user_choice(user_c)
    
    #for displaying based on input
    cal_df = recipes.cal_per_serving_size()
    hist_options(cal_df)
    bar_options(cal_df)
    list_options(cal_df)    
    

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("file1",
                        help="path to CSV file containing cookie info")
    parser.add_argument("file2",
                        help="path to CSV file containing cake info")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file1, args.file2)