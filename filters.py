import pandas as pd

def apply_filters(df, selected_gender, selected_class):
    # Filter by gender if specific option is selected
    if selected_gender != "All":
        df = df[df['sex'] == selected_gender]
        
    # Filter by ticket class if specific option is selected
    if selected_class != "All":
        df = df[df['pclass'] == int(selected_class)]
        
    return df