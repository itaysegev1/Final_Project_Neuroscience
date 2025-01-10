import numpy as np

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
RESET = "\033[0m"

from HebbianNetwork import HebbianNetwork
from VectorsFactory import VectorsFactory

if __name__ == '__main__':
    # crating the network
    net = HebbianNetwork(64, 3, learning_rate=1)

    # creating the inputs
    inputs = VectorsFactory.create_letters_vector()
    outputs = VectorsFactory.create_weight_mat()

    # training the network
    print(f"{GREEN}start training...{RESET}")
    errors = net.train(
        inputs,
        outputs,
        epochs=5000
    )

    # evaluate the network
    accuracy = net.calculate_accuracy(inputs, outputs)
    print(f"{BLUE}Accurate on train {accuracy:.2%}{RESET}")

    # Checking the results for all the letters and print
    print(f"{GREEN}Results for all the letters on the train: {RESET}")
    for i, input_vector in enumerate(inputs):
        prediction = net.predict(input_vector)
        if np.array_equal(prediction, [1, 0, 0]):
            ans = "A-I"
        elif np.array_equal(prediction, [0, 1, 0]):
            ans = "J-R"
        else:
            ans = "S-Z"

        expected = "A-I" if i <= 8 else "J-R" if i <= 17 else "S-Z"
        color = BLUE if ans == expected else RED

        print(f"\t{color}The letter {chr(65 + i)} Suppose to be in: {expected},and the answer is: {ans}{RESET}")

    for i in range(5, 21, 5):
        vecs = VectorsFactory.create_vectors_with_mistakes(inputs, percent=i / 100)
        accuracy = net.calculate_accuracy(vecs, outputs)
        print(f"\n{PURPLE}the accuracy with {i}% of mistake is: {accuracy:.2%}{RESET}")
        print(f"{GREEN}Results for this group: {RESET}")
        for j, input_vector in enumerate(vecs):
            prediction = net.predict(input_vector)
            if np.array_equal(prediction, [1, 0, 0]):
                ans = "A-I"
            elif np.array_equal(prediction, [0, 1, 0]):
                ans = "J-R"
            else:
                ans = "S-Z"

            expected = "A-I" if j <= 8 else "J-R" if j <= 17 else "S-Z"
            color = BLUE if ans == expected else RED
            print(f"\t{color}The letter {chr(65 + j)} Suppose to be in: {expected},and the answer is: {ans}{RESET}")

    test2vecs = VectorsFactory.create_bold_letters_vector()
    accuracy = net.calculate_accuracy(test2vecs, outputs)
    print(f"\n{PURPLE}the accuracy with group number 1: {accuracy:.2%}{RESET}")
    print(f"{GREEN}Results for this group: {RESET}")
    for j, input_vector in enumerate(test2vecs):
        prediction = net.predict(input_vector)
        if np.array_equal(prediction, [1, 0, 0]):
            ans = "A-I"
        elif np.array_equal(prediction, [0, 1, 0]):
            ans = "J-R"
        else:
            ans = "S-Z"

        expected = "A-I" if j <= 8 else "J-R" if j <= 17 else "S-Z"
        color = BLUE if ans == expected else RED
        print(f"\t{color}The letter {chr(65 + j)} Suppose to be in: {expected},and the answer is: {ans}{RESET}")

    test3vecs = VectorsFactory.create_letters_v3_vector()
    accuracy = net.calculate_accuracy(test3vecs, outputs)
    print(f"\n{PURPLE}the accuracy with group number 2: {accuracy:.2%}{RESET}")
    print(f"{GREEN}Results for this group: {RESET}")
    for j, input_vector in enumerate(test3vecs):
        prediction = net.predict(input_vector)
        if np.array_equal(prediction, [1, 0, 0]):
            ans = "A-I"
        elif np.array_equal(prediction, [0, 1, 0]):
            ans = "J-R"
        else:
            ans = "S-Z"

        expected = "A-I" if j <= 8 else "J-R" if j <= 17 else "S-Z"
        color = BLUE if ans == expected else RED
        print(f"\t{color}The letter {chr(65 + j)} Suppose to be in: {expected},and the answer is: {ans}{RESET}")

    test4vecs = VectorsFactory.create_letters_v4_vector()
    accuracy = net.calculate_accuracy(test4vecs, outputs)
    print(f"\n{PURPLE}the accuracy with group number 3: {accuracy:.2%}{RESET}")
    print(f"{GREEN}Results for this group: {RESET}")
    for j, input_vector in enumerate(test4vecs):
        prediction = net.predict(input_vector)
        if np.array_equal(prediction, [1, 0, 0]):
            ans = "A-I"
        elif np.array_equal(prediction, [0, 1, 0]):
            ans = "J-R"
        else:
            ans = "S-Z"

        expected = "A-I" if j <= 8 else "J-R" if j <= 17 else "S-Z"
        color = BLUE if ans == expected else RED
        print(f"\t{color}The letter {chr(65 + j)} Suppose to be in: {expected},and the answer is: {ans}{RESET}")
