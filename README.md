### Introduction

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
### Instructions for running locally

Clone repository to local machine
```
git clone git@github.com:dunglucbac/InteriorRecommendation.git
```

Change directory to local repository
```
cd InteriorRecommendation
```

Create python virtual environment
```
python3 -m venv venv             # create virtualenv
source venv/bin/activate         # activate virtualenv
pip install -r requirements.txt  # install requirements
```

Run scripts
```
cd app/
python -m main.py
```

Check results

![image](https://2.pik.vn/2020ef7de977-9025-47c4-bfb9-f26eecb2c48d.jpg)



### Link references
https://www.miai.vn/2019/08/09/yolo-series-2-cach-train-yolo-de-detect-cac-object-dac-thu/
https://www.miai.vn/2019/08/15/yolo-series-cach-train-yolo-tren-google-colab/
https://github.com/codingbunnie/WISH-by-NANA-FashionRecommendationEngine
https://www.kaggle.com/ekaterinagasparian/train6
https://mc.ai/end-to-end-object-detection-for-furniture-using-deep-learning/
