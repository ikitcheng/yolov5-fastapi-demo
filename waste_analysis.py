# Plate Waste Detection Analysis
# Author: I Kit Cheng
# Date: 2022-03-30

import pandas as pd
import config

def calc_area(bbox_pix_coord, pix2cm2_factor=0.05):
    """Calculate the area of each bounding box. 

    Args:
        bbox_pix_coord (list): A list of pixel coordinates [x1,y1,x2,y2].
    Returns: 
        area (float): Area (in cm2) of bounding box (assuming all images taken from fixed height).
    """
    x1, y1, x2, y2 = bbox_pix_coord
    area = ((x2-x1) * (y2-y1)) * pix2cm2_factor
    return area
    
def calc_weight(area, class_name):
    """Calculate the weight of food in bounding box. 

    Args:
        weight (float): Weight of food (in grams).
        class_name (str): Name of food in bounding box. 
    """
    df = pd.read_excel(f"{config.PATH_TO_DATA}food_density_data.xlsx", index_col=0)
    density = df.loc[class_name.lower(), 'Density (g/ml)']
    thickness = df.loc[class_name.lower(), 'Thickness (cm)']
    FOOD_AREA_FACTOR = 0.8
    volume = FOOD_AREA_FACTOR * area * thickness
    weight = volume * density # 1 ml = 1 cm^3
    return weight