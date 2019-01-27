# InfoRe-internship-challenge

Note: We would prefer you to use [Keras](keras.io) for this project due to its simplicity. However, any other framework is welcome.

## Challenge 1: Images Classification

### About

In this challenge, you're aksed to create a model or using whatever AI algorithm you want to classify over 10 different breeds of dog. Follow this [link](https://www.dropbox.com/s/p5xgxa9ofmq48vf/dataset.zip?dl=0) to download the dataset. 
Train/valid split information is provided in  `Computer Vision/public.json`. Test data will be published after the deadline and your final score will be evaluated based on it. 

**Make sure you index the classes in the following way, otherwise your final score will be incorrect**

| Class Name  | Index |
|-------------|-------|
| bullmastiff | 0     |
| chowchow    | 1     |
| pug         | 2     |
| maltese     | 3     |
| huskysibir  | 4     |
| dachshund   | 5     |
| dalmatian   | 6     |
| corgi       | 7     |
| chihuahua   | 8     |
| yorkshire   | 9     |

### Referencing Materials

- [CNN network](http://cs231n.github.io/)
- [Building model with keras](https://elitedatascience.com/keras-tutorial-deep-learning-in-python)
- Transfer learning with keras tutorial (google yourself :D)

## Challenge 2: Intent Classification

### About

The goal of this challenge is to develop a model that can detect the user's intention based on their query or input sentence. This is a basic sentence classification problem with 7 classes (7 intents), with around 2000 sentences each class in the training dataset. All the training data is contained in `intent-train-data`, there are 7 files respected to 7 classes. Each file contains all training examples of each class and one example (sentence) on each line. This dataset is extracted from [nlu-benchmark](https://github.com/snipsco/nlu-benchmark/)

The 7 intents are: (**Make sure you index the classes in the following order, otherwise your final score will be incorrect**) 

0. SearchCreativeWork (e.g. Find me the I, Robot television show),
1. GetWeather (e.g. Is it windy in Boston, MA right now?),
2. BookRestaurant (e.g. I want to book a highly rated restaurant for me and my boyfriend tomorrow night),
3. PlayMusic (e.g. Play the last track from Beyoncé off Spotify),
4. AddToPlaylist (e.g. Add Diamonds to my roadtrip playlist)
5. RateBook (e.g. Give 6 stars to Of Mice and Men)
6. SearchScreeningEvent (e.g. Check the showtimes for Wonder Woman in Paris)

### Referencing Materials

- [Text Classification with keras](https://realpython.com/python-keras-text-classification/)
- [How to solve 90% of NLP problems](https://blog.insightdatascience.com/how-to-solve-90-of-nlp-problems-a-step-by-step-guide-fda605278e4e)