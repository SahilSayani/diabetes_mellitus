import pickle

class Solution:
    def __init__(self,model1,model2,model3,model4):
        self.model1 = model1
        self.model2 = model2
        self.model3 = model3
        self.model4 = model4
        
    def diabetes_dataset(self):
        with open('diabetes_dataset/diabetes_dataset.pkl', 'rb') as file:
            rf_model = pickle.load(file)
        test=[]
        test.append(self.model1)
        #X_test=[[54,	11.3,	130,	7.7,	6.3,	5.4,	33.0,	0]]
        # Use the loaded model for inference
        y_pred_loaded = rf_model.predict(test)
        return y_pred_loaded
    
    def diabetes_prediction(self):
        pass
    def diabetes_type1(self):
        pass
    def diabetes_type1_type2(self):
        with open('diabetes_type1_type2\diabetes_type1_type2.pkl', 'rb') as file:
            rf_model = pickle.load(file)
        test = []
        test.append(self.model1)
        #X_test=[[54,	11.3,	130,	7.7,	6.3,	5.4,	33.0,	0]]
        # Use the loaded model for inference
        y_pred_loaded = rf_model.predict(test)
        return y_pred_loaded
    def output(self):
        pred1 = self.diabetes_dataset()
        pred2 = self.diabetes_prediction()
        pred3 = self.diabetes_type1()
        pred4 = self.diabetes_type1_type2()
        

        #Main point how to determine which model gets what weight?




def main():
    model1,model2,model3,model4=[],[],[],[]
    prediction = Solution(model1,model2,model3,model4)
    
   



if __name__ == '__main__':
    main()