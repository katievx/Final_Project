from argparse import ArgumentParser
import sys
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.parsers import read_csv 


class Recipe:
    """Create a class to read in files into a concatenated dataframe. Also sort categories
        and create histograms and bar graphs to be used for user input
    Attributes:
        cookie_df(str): path to a text file
        cake_df(str): path to a text file
        cookies_and_cake_df(dataframe): a pandas dataframe combining cookies and cakes
    """
    def __init__(self, cookie_df, cake_df):
        """Read in two files and concatenate into a single dataframe
        Args:
            cookie_df(str): see class documentation
            cake_df(str): see class documentation
        Side effects:
            Creates a new datafame
        """
        self.cookie_df = pd.read_csv(cookie_df, sep = ",", encoding = "UTF-8")
        self.cake_df = pd.read_csv(cake_df, sep = ",", encoding = "UTF-8")
        self.cookies_and_cakes_df = pd.concat([self.cookie_df, self.cake_df])

    def cal_per_serving_size(self): 
        """A function that creates a dataframe that includes all the recipes,
            and then adds a column for the calories per each cookie and cake slice 
        Side effects:
            Modifies the dataframe by adding new column 
        """
        self.cookies_and_cakes_df["Calories per cookie or slice"] =  self.cookies_and_cakes_df["Calories"] / self.cookies_and_cakes_df["Serving Size"]
        print("Here is the current dataframe of the two csv files:")
        print(self.cookies_and_cakes_df)
        
    def sort(self):
        """Orders the dataframe by different categories, including:
            calories, bake time, and serving size
        Returns:
            Three ranks of the dataframe categories
        """
        calorie_rank = self.cookies_and_cakes_df.sort_values(["Calories"])
        baketime_rank = self.cookies_and_cakes_df.sort_values(["Bake Time (minutes)"])
        servingsize_rank = self.cookies_and_cakes_df.sort_values(["Serving Size"])
        return (calorie_rank, baketime_rank, servingsize_rank)
        
    def bars(self):
        """Create bar graphs from the dataframe
        Returns:
            Three bar graphs of categories from the recipe dataframe
        """
        calories_bar = self.cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Calories')
        servingsize_bar = self.cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Serving Size')
        baketime_bar = self.cookies_and_cakes_df.plot.bar(x = 'Recipe Name', y = 'Bake Time (minutes)')
        return (calories_bar, servingsize_bar, baketime_bar)

    def hists(self):
        """Create histograms from the dataframe
        Returns:
            Three histograms of categories from the recipe dataframe
        """
        calories_g = self.cookies_and_cakes_df.hist("Calories")
        servingsize_g = self.cookies_and_cakes_df.hist("Serving size")
        baketime_g = self.cookies_and_cakes_df.hist("Bake Time (minutes)")
        return (calories_g, servingsize_g, baketime_g)

    def user_input(self):
        """Prompt user to input an answer about how they want to visualize the dataframe
        Returns:
            user_1(str): user input to the first question
        Side effects:
            Printing options to the user to prompt input
        """
        print("You can also sort the database by certain columns (from lowest to highest) by choosing to see a list.")
        print("Or, view a graphical display of some columns by choosing see to a graph.")
        user_1 = input("Which option would you like: a list or graph?").lower()
        return user_1


def list_options(recipes):
    """If user chose the list visualization, ask what they would want to sort by and print
        their visualization
    Args:
        Recipes: instance of the recipe class
    Side effects:
        Print rank that is inputted by user
    """
    calorie_rank, baketime_rank, servingsize_rank = recipes
    user_2 = input("What would you like the dataframe listed by: calories, bake time, or serving size?").lower()
    while True:
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

def bar_options(recipes):
    """If user chose the bar graph visualization, ask what they would want to sort by and print
        their visualization as a bar graph
    Side effects:
        Print bar graph that is inputted by user
    """
    calories_bar, servingsize_bar, baketime_bar = recipes
    
    user_3 = input("What would you like the bar graph listed by: calories, bake time, or serving size?").lower()
    while True:
        if user_3 == "calories":
            plt.show(calories_bar)
            break
        if user_3 == "bake time":
            plt.show(baketime_bar)
            break
        if user_3 == "serving size":
            plt.show(servingsize_bar)
            break
        else:
            print("We don't have that option! Please input either 'calories', 'serving size', or 'bake time' ")

                                    
def hist_options(recipes):
    """If user chose the histogram visualization, ask what they would want to sort by and print
        their visualization as a histogram
    Side effects:
        Print histogram that is inputted by user
    """
    calories_g, servingsize_g, baketime_g = recipes
    
    user_3 = "What would you like a histogram for: calories, serving size, or bake time?".lower()
    while True:
        if user_3 == "calories":
            plt.show(calories_g)
            break
        if user_3 == "serving size":
            plt.show(servingsize_g)
            break
        if user_3 == "bake time":
            plt.show(baketime_g)
            break
        else:
            print("We don't have that option! Please input either 'calories', 'serving size', or 'bake time' ")

def user_choice(user_1):
    """Return the choice that was inputted by the user
    Returns:
        The visualization chosen by the user
    """
    while True:
        if user_1 == "list":
            list_options
            break
        if user_1 == "graph":
            user_n = input("Do you want to see a histogram or bar graph?").lower()
            if user_n == "bar graph":
                bar_options
                break
            if user_n == "histogram":
                hist_options
                break
        else:
            print("We don't have that option! Please input either 'list', 'graph' ")
            
            return user_n
                
                
def main(file1, file2):   
    """Create a recipes object from Recipe class and return visualization from user unput
    Args:
        file1(str): First file with data
        file2(str): Another file with data
    """
    recipes = Recipe(file1, file2)    
    recipes.cal_per_serving_size()

    user_c = recipes.user_input()
    user_choice(user_c)
    
    if user_c == "list":
        list_op = recipes.sort()
        list_options(list_op)
        
    user_g = user_choice
    
    if user_g == "bar graph":
        bar_op = recipes.bars()
        bar_options(bar_op)
    if user_g == "histogram":
        hist_op = recipes.hists()
        hist_options(hist_op)

   
    
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