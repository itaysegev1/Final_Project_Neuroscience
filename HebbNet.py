# import numpy as np
#
#
# class HebbNet:
#     def __init__(self, input_size, output_size, learning_rate=0.001):
#         self.input_size = input_size
#         self.output_size = output_size
#         self.learning_rate = learning_rate
#         self.weights = np.zeros((output_size, input_size))
#
#     # def train(self, inputs, outputs, learning_rate=1):
#     #     for i in range(self.input_size):
#     #         ans = self.predict(inputs)
#     #         while ans != outputs:
#     #             learning_rate =0.15
#     #             for j in range(self.output_size):
#     #                 if outputs[j] == 0:
#     #                     self.weights[i, j] -= learning_rate
#     #                 self.weights[i, j] += inputs[i] * (outputs[j]-ans[j]) * learning_rate
#     #             ans = self.predict(inputs)
#     #         else:
#     #             learning_rate =0.1
#     #             for j in range(self.output_size):
#     #                 if outputs[j] == 0:
#     #                     self.weights[i, j] -= learning_rate
#     #                 self.weights[i, j] += inputs[i] * outputs[j] + learning_rate
#
#
# def train(self, inputs, outputs):
#     for i in range(self.output_size):
#         x = 0
#         for input in inputs:
#             print(len(input))
#             for j in range(len(input)):
#                 print(i, j)
#                 if j < len(input) - 1:
#                     self.weights[j][i] += outputs[x][i] * self.weights[j][i]
#                 else:
#                     self.weights[j][i] = outputs[x][i] + self.weights[j][i]
#             x += 1
#
#
# def predict(self, inputs):
#     result = [-200, -200, -200]
#     maxo = float('-inf')
#     ans_vec = []
#     for j in range(self.output_size):
#         for i in range(self.input_size):
#             result[j] += self.weights[i, j] * inputs[i]
#         if result[j] > maxo:
#             maxo = result[j]
#         print(result[j])
#     for i in range(self.output_size):
#         if result[i] == maxo:
#             ans_vec.append(1)
#         else:
#             ans_vec.append(0)
#     return ans_vec
#
#
# def __str__(self):
#     return str(self.weights)
