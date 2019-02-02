# InfoRe-internship-challenge

## Note

- We would prefer you to use [Keras](keras.io) in this project due to its simplicity. However, any other framework is welcome.
- In these following challenges, we will provide you with training data which you can use to build your model. On the deadlines, we will publish our private test data for you to get the final score.
- You have to write a report per week in which you should describe/explain how you processed data, how you improved your model (using cross-validation, k-fold, grid-search or something like that) stage by stage. 

For example:

`REPORT WEEK 1 CHALLENGE 1`

| Date       | Description                                                                                                             | Top-3 acc (Training/Validation) | Top-1 acc (Training/Validation) |
|------------|-------------------------------------------------------------------------------------------------------------------------|---------------------------------|---------------------------------|
| 12/02/2018 | First try with a basic SVM                                                                                              | 80/70                           | 77.6/72.5                       |
| 13/02/2018 | Using Lenet5 architecture                                                                                               | 85/84                           | 80.5/82.4                       |
| 14/02/2018 | It's Valentine's Day so I changed the number of units of all hidden layers to the number of days we have been together. | 99.99/50                        | 90.1/19.2                       |
| ...        |                                                                                                                         |                                 |                                 |

- Note that we will use [top-1 and top-3 accuracy](https://stats.stackexchange.com/questions/156471/imagenet-what-is-top-1-and-top-5-error-rate) to evaluate your model. Please implement these metrics by yourself to make sure that the performance in your report is aligned with your final score.

## Challenge 1: Images Classification

### About

In this challenge, you're aksed to create a model or using whatever AI algorithm you want to classify over 10 different breeds of dog. Follow this [link](https://www.dropbox.com/s/p5xgxa9ofmq48vf/dataset.zip?dl=0) to download the dataset. 

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

### Deadlines

- 1st report: 23:59 17/02/2019
- 2nd report: 23:59 23/02/2019
- Private data published: 12:00 24/02/2019

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

### Deadlines

- 1st report: 23:59 03/03/2019
- 2nd report: 23:59 09/03/2019
- Private data published: 12:00 10/03/2019