from load import load_data
from wordcloud import WordCloud, ImageColorGenerator
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io

terror_df = load_data()

def plot_wordcloud():
    f, ax = plt.subplots(figsize=(11, 9))
    # plt.figure(figsize=(10,20))
    wordcloud = WordCloud(background_color= 'black', 
                        max_font_size=500, 
                        collocations= False, 
                        relative_scaling= 0.4, 
                        colormap= "Reds").generate(''.join([x for x in terror_df['region_txt'].str.replace(' ','')]))
    # plt.title('Frequent Attack Regions', fontdict = {'size':20, 'weight':'bold'})
    plt.imshow(wordcloud, interpolation= 'bilinear')
    plt.tight_layout(pad=0)
    plt.axis('off')
    # plt.show()

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)

    return bytes_image

def plot_heatmap():

    corr = terror_df.corr(method='pearson')

    f, ax = plt.subplots(figsize=(20, 20))

    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)


    return bytes_image
