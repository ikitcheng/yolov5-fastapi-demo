# Plate Waste Detection Analysis
# Author: I Kit Cheng
# Date: 2022-03-30

import pandas as pd
import config

def calc_area(bbox_pix_coord, pix2cm2_factor):
    """Calculate the area of each bounding box.

    Args:
        bbox_pix_coord (list): A list of pixel coordinates [x1,y1,x2,y2].
        pix2cm2_factor (float): The pixel to cm conversion factor. 
            This depends on the distance between camera the food.
    Returns: 
        area (float): Area (in cm2) of bounding box (assuming all images taken from fixed height).
    """
    x1, y1, x2, y2 = bbox_pix_coord
    area = ((x2-x1) * (y2-y1)) * pix2cm2_factor
    return area
    
def calc_weight(df, area, class_name):
    """Calculate the weight of food in bounding box. 

    Args:
        df (pd.DataFrame): Dataframe of food densities (in g/ml or g/cm3).
        weight (float): Weight of food (in grams).
        class_name (str): Name of food in bounding box. 
    """
    class_name = class_name.lower()

    if class_name in df.index:
        density = df.loc[class_name, 'Density (g/ml)']
        thickness = df.loc[class_name, 'Thickness (cm)']
        FOOD_AREA_FACTOR = 0.8
        volume = FOOD_AREA_FACTOR * area * thickness
        weight = volume * density # 1 ml = 1 cm^3
    else:
        if class_name == 'apple':
            weight = 133. #grams (medium)
        elif class_name == 'orange':
            weight = 190. #grams (medium)
        elif class_name == 'pear':
            weight = 180. #grams (medium)
        elif class_name == 'banana':
            weight = 120. #grams (medium)
        else: 
            weight = 0 # not determined (yet)
    return weight

def classify_edible_inedible(class_name):
    """ Classify detected plate waste as Edible or Inedible. 

    Args:
        class_name (str): Plate waste name. 
    Returns:
        str : 'Edible' or 'Inedible'
    """

    plate_waste_classes = {'Apple':'Edible',
                           'Apple-core':'Inedible',
                           'Apple-peel':'Inedible',
                           'Banana':'Edible',
                           'Bone':'Inedible',
                           'Bone-fish':'Inedible',
                            'Bread':'Edible',
                            'Bun':'Edible',
                            'Egg-hard':'Edible',
                            'Egg-scramble':'Edible',
                            'Egg-shell':'Inedible',
                            'Egg-steam':'Edible',
                            'Egg-yolk':'Edible',
                            'Fish':'Edible',
                            'Meat':'Edible',
                            'Mussel':'Edible',
                            'Mussel-shell':'Inedible',
                            'Noodle':'Edible',
                            'Orange':'Edible',
                            'Orange-peel':'Inedible',
                            'Other-waste':'Inedible',
                            'Pancake':'Edible',
                            'Pasta':'Edible',
                            'Pear':'Edible',
                            'Pear-core':'Inedible',
                            'Pear-peel':'Inedible',
                            'Potato':'Edible',
                            'Rice':'Edible',
                            'Shrimp':'Edible',
                            'Shrimp-shell':'Inedible',
                            'Tomato':'Edible',
                            'Tofu':'Edible',
                            'Vegetable':'Edible'}
    
    return plate_waste_classes[class_name]