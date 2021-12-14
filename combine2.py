from argparse import ArgumentParser
import sys
import pandas as pd
import matplotlib.pyplot as plt 


class Recipe:
    
    def __init__(self, cookie_df, cake_df):
        self.cookie_df = cookie_df
        self.cake_df = cake_df

    def read_csvs(cookie_df, cake_df):
        cookie_df = pd.read_csv(cookie_df, sep = ",", encoding = "UTF-8")
        cake_df = pd.read_csv(cake_df, sep = ",", encoding = "UTF-8")
        return (cake_df, cookie_df)

    def cal_per_serving_size(self, cookie_df, cake_df): 
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

#might remove self. portion ???
    def sort(self, cookies_and_cakes_df):
        """Orders the dataframe by different categories, including:
        calories, bake time, and serving size
        """
        self.calorie_rank = cookies_and_cakes_df.sort_values(["Calories"])
        self.baketime_rank = cookies_and_cakes_df.sort_values(["Bake Time (minutes)"])
        self.servingsize_rank = cookies_and_cakes_df.sort_values(["Serving Size"])
        return (self.calorie_rank, self.baketime_rank, self.servingsize_rank)
        
    def bars(self, cookies_and_cakes_df):
        calories_bar = cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Calories')
        servingsize_bar = cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Serving Size')
        baketime_bar = cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Bake Time (minutes)')
        return (calories_bar, servingsize_bar, baketime_bar)

    def hists(self, cookies_and_cakes_df):
        calories_g = cookies_and_cakes_df.hist("Calories")
        servingsize_g = cookies_and_cakes_df.hist("Serving size")
        baketime_g = cookies_and_cakes_df.hist("Bake Time (minutes)")
        return (calories_g, servingsize_g, baketime_g)

#might make user input sep class(?)
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
    recipes = Recipe(file1, file2)    
    recipes.cal_per_serving_size(file1, file2)
    
    cal_df = recipes.cal_per_serving_size(file1, file2)
    recipes.sort(cal_df)
    
    user_info = user_input()

    sort1 = recipes.calorie_rank
    sort2 = recipes.baketime_rank
    sort3 = recipes.servingsize_rank
    list_options(user_info,sort1, sort2, sort3)
    
    b1 = recipes.calories_bar
    b2 = recipes.servingsize_bar
    b3 = recipes.baketime_bar
    bar_options(user_info, b1, b2, b3)
    
    bar_choice = bar_options()
    h1 = recipes.calories_g
    h2 = recipes.servingsize_g
    h3 = recipes.baketime_g
    hist_options(bar_choice, h1, h2, h3)
    


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

