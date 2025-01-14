# 📝 Hebbian Neural Network for Letter Classification

<div align="center">

# 🧠 Letter Classification Neural Network

<h2>
A Sophisticated Implementation of Hebbian Learning
</h2>

<p align="center">
    <b>🎯 Advanced Pattern Recognition | 🔍 Robust Classification | 📊 Comprehensive Analysis</b>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x">
</p>

---

</div>

## 🌟 Overview

This project showcases an advanced implementation of a Hebbian Learning Network designed to classify English alphabet letters. The network demonstrates impressive pattern recognition capabilities, able to handle both clean and noisy inputs while maintaining robust performance.

## 🎯 Key Features

### Classification Modes
- ✨ **Group Classification**: Sorts letters into three categories (A-I, J-R, S-Z)
- 🎯 **Individual Letter Recognition**: Identifies specific letters (A through Z)

### Input Flexibility
- 📋 Standard letter format
- 📝 Bold letters
- ⭕ Bold with circular styling
- 🔵 Extra bold with circular styling

### Advanced Testing
- 🔍 Noise tolerance testing (5%, 10%, 15%, 20%)
- 📊 Comprehensive accuracy analysis
- 🎨 Color-coded visual feedback

## 🏗️ Project Structure

### 📁 Core Components

```
└── 📂 Project Root
    ├── 📜 HebbianNetwork.py  # Core neural network implementation
    ├── 📜 VectorsFactory.py  # Data generation and preprocessing
    ├── 📜 Main.py           # Execution and interface
    └── 📜 README.md         # Documentation
```

### 🔧 Technical Architecture

#### HebbianNetwork.py
- 🧠 Neural network core implementation
- ⚙️ Weight matrix management
- 🎯 Training and prediction logic
- 📊 Sigmoid activation function

#### VectorsFactory.py
- 🎨 Letter vector generation
- 📚 Dataset creation
- 🔄 Noise simulation
- 📋 Output matrix management

#### Main.py
- 🎮 User interface
- 📊 Results visualization
- 📈 Statistical analysis
- 🔍 Testing procedures

## 💻 Technical Specifications

### Network Architecture
- **Input Layer**: 64 neurons (8x8 grid)
- **Output Layer**: 
  - 3 neurons (group classification)
  - 26 neurons (individual letters)
- **Parameters**:
  - Learning Rate: 1.0
  - Training Epochs: 5000
  - Regularization: 0.00001

### 🎨 Letter Representation
Letters are encoded as 8x8 binary matrices where:
```
1 = Letter segment
0 = Background
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- NumPy library

### Installation Steps

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Install dependencies:
```bash
pip install numpy
```

### 🎮 Usage

1. Run the main script:
```bash
python Main.py
```

2. Choose your classification mode:
```
Enter a number for active the Hebbian Network:
1. For categories for 3 groups (A-I),(J-R),(S-Z)
2. For categories each letter for itself
3. Exit
```

## 📊 Performance Analysis

The system provides rich analytics including:
- ✅ Accuracy percentages
- 📈 Performance variance
- 📊 Standard deviation
- 🎨 Color-coded results:
  - 🔵 Blue: Correct predictions
  - 🔴 Red: Incorrect predictions
  - 💚 Green: Status messages
  - 💜 Purple: Statistical results

## 🔍 Implementation Details

### Training Process
1. 📝 Weight matrix initialization
2. 🔄 Iterative training through epochs
3. 🧮 Hebbian learning rule application
4. ⚖️ Weight updates with regularization
5. 📈 Convergence monitoring

### Prediction Workflow
1. 📥 Input vector processing
2. ⚙️ Weight application
3. 📊 Sigmoid activation
4. 📤 Classification output

## 🛠️ Error Handling

The system includes robust error handling for:
- ✅ Input validation
- 🔍 Parameter verification
- 💪 Noise resilience
- 📉 Graceful performance degradation

## 🌟 Examples

### Sample Output
```
The accuracy with Group of the train letters: 100.00%
Results for this group:
    The letter A Suppose to be in: A-I, and the answer is: A-I
    The letter B Suppose to be in: A-I, and the answer is: A-I
    ...
```

## 👥 Contributors

This project was developed by:
- **Itay Segev**
- **Salome Timsit**

---

<div align="center">

📧 *For questions or support, please open an issue in the repository*

</div>