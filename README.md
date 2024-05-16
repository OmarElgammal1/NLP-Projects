## Project Overview
This is a Multi Classical ML Models for Different NLP tasks. The models are implemented
using TensorFlow and Scikit-learn. The models are trained on different datasets
datasets used are:
- [twitter-sentiment-analysis](https://www.kaggle.com/datasets/mohamedamgad2002/tweet-sentiment-analysis)
- [Sentiment Analysis on Movie Reviews](https://www.kaggle.com/competitions/sentiment-analysis-on-movie-reviews/data)
## Installation
1- Open your terminal or command prompt.

2- Navigate to the directory where you want to create the virtual environment. You can use the cd command to change directories.

3- Enter the following command to create a virtual environment named projectenv.
You can name it anything you like, but projectenv is used as an example here.
```sh
python -m venv projectenv && cd projectenv
```

This will create a new directory named **projectenv** in your current directory, which will contain the virtual environment.

4- Activate the virtual environment through: ```Scripts\activate```  
> Note: If it didn't work enter this instead: ```source Scripts\activate```

You should now see (**projectenv**) at the beginning of your command prompt, indicating that the virtual environment is active.

> To deactivate the virtual environment, simply enter the command `deactivate` in the terminal.

5- After activating the virtual environment, you can install the required packages using the following command:
```sh
pip install -r requirements.txt

```
6- After installing the required packages, you can run the project using the following command:
```sh
python -u main.py
```
## Usage
You Can use it in Sentiment Analysis, Other NLP tasks coming soon :)

## License

This project is licensed under the terms of the Apache License 2.0. For more details, see the [LICENSE](./LICENSE) file in the root directory of this project.