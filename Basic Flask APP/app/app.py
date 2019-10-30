from flask import Flask, send_file, make_response, render_template
from plot import plot_heatmap, plot_wordcloud
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
from load import load_data


app = Flask(__name__, template_folder='')

BASE_URL = "http://localhost:8080/"

terror_df = load_data()

@app.route('/',methods=['GET'])
def index():
    # return render_template('index.html', base_url=BASE_URL)
    return render_template('/templates/index.html' , base_url=BASE_URL)

images = []

# @app.route('/plots/global_terrorism/pairplot', methods=['GET'])
# def pairplot():
#     try:
#         # parse columns
        
#         f, ax = plt.subplots(figsize=(11, 9))
#         sns.pairplot(terror_df,
#                     hue='diagnosis',
#                     palette=('Red', '#875FDB'),
#                     markers=["o", "D"])

#         bytes_image = io.BytesIO()
#         plt.savefig(bytes_image, format='png')
#         bytes_image.seek(0)

#         # bytes_obj = pt.plot_pairplot()


#         return send_file(bytes_image,
#                          attachment_filename='plot.png',
#                          mimetype='image/png')
#     except ValueError:
#         # something went wrong to return bad request
#         return make_response('Unsupported request, probably feature names are wrong', 400)


@app.route('/plots/global_terrorism/correlation_matrix', methods=['GET'])
def correlation_matrix():
    bytes_obj = plot_heatmap()

    

    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')


# @app.route('/plots/global_terrorism/word_cloud', methods=['GET'])
def word_cloud():
    bytes_object = plot_wordcloud()

    

    return send_file(bytes_object,
                     attachment_filename='plot.png',
                     mimetype='image/png')



# @app.route('/plots/global_terrorism/plots', methods=['GET'])
# def plots_graphs():
#     bytes_obj = plot_heatmap()

#     images.append(bytes_obj)

#     bytes_object = plot_wordcloud()

#     images.append(bytes_object)
    
#     return send_file(images,
#                      attachment_filename='plot.png',
#                      mimetype='image/png')


if __name__ == '__main__':
    # app.jinja_env.auto_reload = True
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True,port=8080)




  