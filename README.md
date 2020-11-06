Introduction

Have you ever been in a situation where you came to your friend’s house then impressed by his / her apartment decoration. The idea is based on my experience of that and I want a smart machine learning system that can give me similar products on the internet. Moreover, it will give you a better idea by recommending home designs from others to give you a clearer view of what you want in ‘your house’.

### Project structure explanation
```
interior-recommendation
│   README.md             # Project description
│
└───app                   # The folder contains source code
   |               
   └───blueprints
   |   |
   |   └───home
   |        |  
   |        └───blueprints.py  # Receive images from the website then generate recommendation
   |
   └───middlewares
   |    │  ...              
   |               
   └───models           
   |   │  
   |   |─── cropped       # Data class for cropped image
   |   |    ...
   |   └───products       # Deserialize a row in the DataFrame
   |       ...
   └───static             # Bootstrap template
   |    │  ...
   └───templates          # HTML template folder
   |
   main.py                # main function running flask
```


Furniture detection
In order to detect in real-time, I’m gonna use Yolo version 3. I gather and label data by using Open Google Image v5 https://storage.googleapis.com/openimages/web/visualizer/index.html?set=train&type=detection&c=%2Fm%2F03m3pdh.
At this step I have my own proper data formated to be using for training in VM or google colab.
This step involves properly configuring custom .cfg file, .obj data, .obj name and train.txt file.
The last configuration file needed before we can begin to train our custom detector is the file train.txt which hold the relative paths of our training images.
Once everything I need to train my custom model using Yolo v3 is ready, I can open file and train it.
Recommed similar products
Firstly, crawling data from famous furniture websites included https://www.wayfair.com/, https://www.luluandgeorgia.com/, https://www.onekingslane.com/…
Put data crawled from these resources to database.
Recommend new home decorations
Suggest where to buy these new products
Methodology
The users upload image(JPG, JPEG format) YOLO detection will detect features and preprocessing of that image then feed into model as an input. The model produces the probability and bouding boxes drawn around furniture object.There are 6 classes including bed, chair, swivelchair, table, lamp, sofa.

Links
https://www.miai.vn/2019/08/09/yolo-series-2-cach-train-yolo-de-detect-cac-object-dac-thu/
https://www.miai.vn/2019/08/15/yolo-series-cach-train-yolo-tren-google-colab/
https://github.com/codingbunnie/WISH-by-NANA-FashionRecommendationEngine
https://www.kaggle.com/ekaterinagasparian/train6
https://mc.ai/end-to-end-object-detection-for-furniture-using-deep-learning/
