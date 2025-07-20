import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Projects/Freecodecamp_projects/medical_examination/medical_examination.csv')

df['overweight'] = (df['weight'] / (df['height']/100) ** 2 > 25).astype(int)


# normalizing the data by making sure that cholesterol and gluc are either 0 or 1
df['cholesterol'] = df['cholesterol'].apply(lambda x : 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x : 0 if x == 1 else 1)

# Plotting the categorical  graph
def draw_cat_plot():
    # creating a dataframe for the catplot
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol' , 'gluc', 'smoke', 'alco' , 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name = 'total')
    # drawing the catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')
    fig = fig.fig
    fig.savefig('catplot.png')
    return fig

# plotting the heat map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 9))
    
    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidths=0.5, cbar_kws={'shrink': 0.5}, center=0, ax=ax)
    fig.savefig('heatmap.png')
    return fig
