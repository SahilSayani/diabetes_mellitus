import pickle

with open('diabetes_dataset/diabetes_dataset.pkl', 'rb') as file:
    loaded_svm_model = pickle.load(file)
X_test=[[54,	11.3,	130,	7.7,	6.3,	5.4,	33.0,	0]]
# Use the loaded model for inference
y_pred_loaded = loaded_svm_model.predict(X_test)
print(y_pred_loaded)