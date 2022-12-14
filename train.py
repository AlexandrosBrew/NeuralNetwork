import numpy as np
from main import *

try:
    data = pd.read_csv('C:/Users/vali/Documents/Datasets/mnist_train.csv')
except:
    data = pd.read_csv('/Users/alexandrosbrew/Documents/GitHub Repos/Datasets/mnist_train.csv')
data = np.array(data)
m, n = data.shape
np.random.shuffle(data)

data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]

data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]

userinp = input('''1. Start training
2. View weights and biases
3.Exit and Save\n''' + '-'*25+'\n')

while userinp != '3':
    if userinp == '1':
        iteration = int(input('Iterations No: '))
        learningRate = float(input('Learning Rate: '))
        w1, b1, w2, b2, acc = gradient_descent(X_train, Y_train, learningRate, iteration)
        print(w1)
    elif userinp == '2':
        print('-'*25)
        print(f'Weight 1: {str(w1)}   |   Weight 2: {str(w2)}')
        print(f'Bias 1: {str(b1)}   |   Bias 2: {str(b2)}')
        print(f'Accuracy: {str(acc)}')
    
    print('-'*25)
    userinp = input('''1. Start training
2. View weights and biases
3.Exit and Save\n''' + '-'*25+'\n')