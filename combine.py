import pandas as pd


##Eesha's problem
def read_cookie(cookie_filepath):
   """ A function that makes a DataFrame from the cookies.csv file.
  
   Args:
       cookie_filepath (str): the path to the CSV file for cookies.csv.   
  
   Returns:
       DataFrame: cookies.csv in DataFrame format.
   """
   cookie_df = pd.read_csv(cookie_filepath, sep = ",", encoding = "UTF-8")
   return cookie_df
  
def read_cake(cake_filepath):
   """ A function that makes a DataFrame from the cakes.csv file.
  
   Args:
       cake_filepath (str): the file path to the cakes.csv file.
  
   Returns:
       DataFrame: cakes.csv in DataFrame format.
   """
   cake_df = pd.read_csv(cake_filepath, sep = ",", encoding = "UTF-8")
   return cake_df
  
  
##Opeyemi's problem
def cal_per_serving_size(): 
    """ 
    A function that creates a dataframe that includes all the recipes,
    and then adds a column for the calories per each cookie and cake slice
    
    Side effects:
        Creates a new dataframe
        Modifies the new dataframe by adding new column 
    """

    cookies_and_cakes_df = pd.concat([read_cookie.cookie_df, read_cookie.cake_df])
    
    cookies_and_cakes_df["Calories per cookie or slice"] =  cookies_and_cakes_df["Calories"] / cookies_and_cakes_df["Serving Size"]


##Katelyn's problem
def sort():
   """Sort the dataframe by different categories, including:
       calories, bake time, and serving size
   """
   calorie_rank = cookies_and_cakes_df["Calories"].sort_values()
   baketime_rank = cookies_and_cakes_df["Bake Time (minutes)"].sort_values()
   servingsize_rank = cookies_and_cakes_df["Serving Size"].sort_values()