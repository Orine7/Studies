inputs = [1.2,5.1,2.1]

weights = [3.2,2.1,8.7]


bias = 2

layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, bias):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)