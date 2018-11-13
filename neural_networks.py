import random


def activation_function(line, weights, threshold):
    sum = 0
    for i in range(0, len(line)):
        sum += line[i] * weights[i]
    if sum > threshold:
        return 1
    else:
        return 0


def calculate_error(train_data, weights, threshold):
    o = train_data[1]
    axon = activation_function(train_data[0], weights, threshold)
    error = o - axon

    return error


def calculate_weights(train_data, weights, error):
    for i, val in enumerate(weights):
        weights[i] += error * train_data[0][i]

    return weights


if __name__ == "__main__":
    training_set = []
    test_data = []
    weights = []

    iterations = 100
    threshold = random.randrange(1, 10)

    dimensionality = int(input())
    training_set_length = int(input())
    test_set_length = int(input())

    for i in range(training_set_length):
        values = []
        inp = input()
        inp = inp.replace('\n', '').replace('\r', '').replace(' ', '')
        inp = inp.split(',')
        aux = []
        for l in inp[0:-1]:
            aux.append(float(l))
        t_data = [aux, float(inp[-1])]
        training_set.append(t_data)

    for i in range(test_set_length):
        values = []
        inp = input()
        inp = inp.replace('\n', '').replace('\r', '').replace(' ', '')
        inp = inp.split(',')
        for l in inp:
            values.append(float(l))
        test_data.append(values)

    for i in range(dimensionality):
        rand = random.randrange(0, 1)
        weights.append(rand)

    for i in range(iterations):
        # calculate error
        error = 0

        for t in training_set:
            error_aux = calculate_error(t, weights, threshold)
            weights = calculate_weights(t, weights, error_aux)
            error += pow(error_aux, 2)

        if error == 0:
            break

    if (error >= 1):
        print("no solution found")
    else:
        for t in test_data:
            print(activation_function(t, weights, threshold))
