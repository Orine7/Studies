import numpy as np 
inputs = [[1.2,5.1,2.1],
        [1.2,5.1,2.1],
        [1.2,5.1,2.1]]

weights = [[3.2,2.1,8.7],
            [3.2,2.1,8.7],
            [3.2,2.1,8.7]]
bias = [1,5,3]

weights2 = [[3.2,2.1,8.7],
            [3.2,2.1,8.7],
            [3.2,2.1,8.7]]
bias2 = [1,5,3]

weights3 = [[3.2,2.1,8.7],
            [3.2,2.1,8.7],
            [3.2,2.1,8.7]]


bias3 = [1,5,3]

layer1_outputs = np.dot(inputs, np.array(weights).T) + bias

layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + bias2

layer3_outputs = np.dot(layer2_outputs, np.array(weights3).T) + bias3

print(layer3_outputs)