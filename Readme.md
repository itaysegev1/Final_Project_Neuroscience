# Hebbian Network for Letter Classification

This project implements a Hebbian Learning Network that classifies letters of the English alphabet into three groups: A-I, J-R, and S-Z. The network uses supervised learning to recognize patterns in letter representations and can handle various forms of input distortion and variations.

## Features

- Hebbian learning implementation with weight matrix optimization
- Sigmoid activation function for output normalization
- Support for different letter representations (normal, bold, circled)
- Noise tolerance testing with various error percentages (5%, 10%, 15%, 20%)
- Accuracy, variance, and standard deviation calculations
- Comprehensive testing across different letter styles and noise levels

## Project Structure

- `HebbianNetwork.py`: Core implementation of the Hebbian Learning Network
- `Main.py`: Main execution file with testing procedures and result visualization
- `VectorsFactory.py`: Factory class for generating letter vectors and test data

## Technical Details

### HebbianNetwork Class

The network implementation includes:
- Configurable input and output layer sizes
- Adjustable learning rate
- Weight matrix initialization
- Sigmoid activation function
- Training method with regularization
- Prediction capabilities
- Accuracy calculation

### Training Parameters
- Learning Rate: 1.0 (default)
- Input Size: 64 neurons (8x8 letter representation)
- Output Size: 3 neurons (representing the three letter groups)
- Epochs: 5000 (default)
- Regularization: 0.00001

## Usage

1. Initialize the network:
```python
from HebbianNetwork import HebbianNetwork
net = HebbianNetwork(input_size=64, output_size=3, learning_rate=1)
```

2. Create training data:
```python
inputs = VectorsFactory.create_letters_vector()
outputs = VectorsFactory.create_groups_mat()
```

3. Train the network:
```python
errors = net.train(inputs, outputs, epochs=5000)
```

4. Make predictions:
```python
prediction = net.predict(input_vector)
```

## Testing and Evaluation

The project includes comprehensive testing capabilities:
- Training accuracy evaluation
- Testing with different levels of input noise (5%-20%)
- Testing with different letter styles (bold, circled)
- Statistical analysis including:
  - Accuracy calculations
  - Variance measurements
  - Standard deviation computations

## Output Format

The program provides colored console output for better readability:
- Green: Success messages and progress updates
- Purple: Statistical results and accuracy measurements
- Blue: Correct predictions
- Red: Incorrect predictions

## Requirements

- Python 3.x
- NumPy library

## Performance

The network achieves:
- High accuracy on training data
- Robust performance with up to 10% noise
- Reasonable recognition of bold and circled letter variants
- Degrading but predictable performance with increasing noise levels

## Error Handling

The implementation includes:
- Input validation
- Training convergence checking
- Early stopping when target accuracy is achieved