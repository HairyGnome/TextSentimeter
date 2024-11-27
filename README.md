# TextSentimenter

## Description
This project is an AI model created to find out the sentiment of texts on its inputs. The output has five different values, going as: negative, slightly negative, neutral, slightly positive, positive.
## Dependencies
The model is created and trained using Tensorflow 2.14.
## Dataset
The dataset used for training is Sentiment140, a dataset consisting of tweets with sentiment labels. It was uploaded by Μαριος Μιχαηλιδης KazAnova, and is available [here](https://www.kaggle.com/datasets/kazanova/sentiment140/data).
## Modules
### Tokenizer
Used to tokenize input text. Tokenization is required to make the input comprehensible for the network, and also to shorten the input. A algorythm used in this module is a BPE encoding algorythm with utf-8 encoding. It was created with the help of [this](https://medium.com/thedeephub/all-you-need-to-know-about-tokenization-in-llms-7a801302cf54) article.
Can be used for training other models from scratch without modification.
### DatabaseParser
Used to parse the training dataset to model-comprehensible. Reads through the provided file and saves the text inputs after tokenizing them, as well as the target label. This module was created with this specific dataset in mind and cannot be used on other datasets without modifications.
### Sentimeter
The model itself. This module defines the model, layer to layer. It also contains the algorythms to train the model, and some evaluation.
