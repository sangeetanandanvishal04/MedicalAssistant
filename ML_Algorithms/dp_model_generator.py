import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')

# Load dataset
df = pd.read_csv('./ML_Algorithms/training.csv')

# Encode the target variable
label_encoder = LabelEncoder()
df['prognosis_encoded'] = label_encoder.fit_transform(df['prognosis'])

# Split the data into features (X) and target (y)
X = df.drop(['prognosis', 'prognosis_encoded'], axis=1)
y = df['prognosis_encoded']

# Split data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Standardize the features
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Convert data to PyTorch tensors
x_train_tensor = torch.tensor(x_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.long)
x_test_tensor = torch.tensor(x_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test.values, dtype=torch.long)

# Define Neural Network Model
class DiseasePredictorNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(DiseasePredictorNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# Model parameters
input_size = x_train.shape[1]
hidden_size = 64
output_size = len(df['prognosis_encoded'].unique())  # Number of unique prognosis values

# Initialize the model
model = DiseasePredictorNN(input_size, hidden_size, output_size)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training the model
num_epochs = 50
for epoch in range(num_epochs):
    model.train()
    
    # Forward pass
    outputs = model(x_train_tensor)
    loss = criterion(outputs, y_train_tensor)
    
    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Testing the model
model.eval()
with torch.no_grad():
    y_test_pred = model(x_test_tensor)
    _, y_test_pred_labels = torch.max(y_test_pred, 1)

# Convert predictions to numpy array for evaluation
y_test_pred_np = y_test_pred_labels.numpy()

# Evaluation
print("Testing Accuracy:", accuracy_score(y_test, y_test_pred_np))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_test_pred_np))
print("\nClassification Report:")
print(classification_report(y_test, y_test_pred_np))

# Save the trained model using pickle
with open('./ML_Models/disease_predictor.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Disease predictor model saved successfully.")