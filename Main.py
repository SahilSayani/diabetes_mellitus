import pickle
import pandas as pd
#columns {AGE,	Urea,Cr,HbA1c,Chol,TG,	BMI,gender,HighBP,HighChol,,PhysActivity,GenHlth,DiffWalk,healthy_food}
#diabetes 012_health_indicator will get the priority
class Solution:
    model1_columns = ['AGE'	,'Urea'	,'Cr'	,'HbA1c'	,'Chol'	,'TG','BMI',	'gender']
    model2_columns = ['HighBP','HighChol',	'BMI',	'PhysActivity'	,'GenHlth',	'DiffWalk'	,'Sex'	,'Age'	,'healthy_food']
    model3_columns = ['Age',	'BS Fast',	'BS pp'	,'Plasma R'	,'Plasma F',	'HbA1c'	]
    def __init__(self,model1,model2):
        
        self.model1 = model1
        self.model2 = model2
        
        
        
    def diabetes_dataset(self):
        with open('diabetes_dataset/diabetes_dataset.pkl', 'rb') as file:
            rf_model = pickle.load(file)
        test = []
        test.append(self.model1)
        test1 = pd.DataFrame(test, columns=Solution.model1_columns)

        #X_test=[[54,	11.3,	130,	7.7,	6.3,	5.4,	33.0,	0]]
        # Use the loaded model for inference
        y_pred_loaded = rf_model.predict(test1)
        return y_pred_loaded
    
    def diabetes_prediction(self):
        with open('diabetes_prediction/diabetes_012_health_indicators.pkl', 'rb') as file:
            rf_model = pickle.load(file)
        test = []
        test.append(self.model2)
        test1 = pd.DataFrame(test, columns=Solution.model2_columns)
        
        
        y_pred_loaded = rf_model.predict(test1)
        return y_pred_loaded
    
    """def diabetes_type1(self):
        with open('', 'rb') as file:
            rf_model = pickle.load(file)
        test = []
        test.append(self.model1)
        
        y_pred_loaded = rf_model.predict(test)
        return y_pred_loaded"""
    def diabetes_type1_type2(self):
        with open('diabetes_type1_type2/diabetes_type1_type2.pkl', 'rb') as file:
            rf_model = pickle.load(file)
        test = []
        #Age	BS Fast	BS pp	Plasma R	Plasma F	HbA1c	
        #BS Fast	BS pp	Plasma R	Plasma F
        hba1c = self.model1[3] * 18.01559
        BS_fast = float(input('The fasting blood glucose level measured in mmol/L or mg/dL: '))
        BS_pp = float(input('The postprandial (after meal) blood glucose level measured in mmol/L or mg/dL : '))
        Plasma_R = float(input(' The random blood glucose level measured in mmol/L or mg/dL: '))
        Plasma_F = float(input('Another fasting blood glucose level, possibly a different measurement or source than BS Fast: '))
        temp = [self.model1[0],BS_fast,BS_pp,Plasma_R,Plasma_F,int(hba1c)]
        test.append(temp)
        
        test1 = pd.DataFrame(test, columns=Solution.model3_columns)

        
        y_pred_loaded = rf_model.predict(test1)
        return y_pred_loaded
    
    def output(self):
        #first layer
        pred1 = self.diabetes_dataset()
        pred2 = self.diabetes_prediction()
        # 0 -> no diabetes 1 -> pre-diabetes 2 -> diabetes
        if(pred1==0 and pred2 ==0 ):
            return 'The patient does not have diabetes and is healthy'
        elif((pred1==0 or pred1==1) and  pred2==1):
            return 'Patient has pre-diabetes and can get diabetes type 2 in the future'
        
        else:
            print("-------------------------xx--------------------------------")
            print('patient likely has diabetes , more information is needed for confirmation')
            #second layer
            pred3 = self.diabetes_type1_type2()
            if (pred3==1):
                return 'Patient has Type 1 Diabetes '
            elif(pred3==2):
                return 'Patient has Type 2 Diabetes '
            elif(pred3 ==0 and (pred1 ==0 or pred2 ==0)):
                return 'Patient is Normal'
            else:
                return 'Patient might have diabetes please consult doctor for more information'


        
        
        






def main():
    #AGE,	Urea,Cr,HbA1c,Chol,TG,	BMI,gender,HighBP,HighChol,,PhysActivity,GenHlth,DiffWalk,Age ,healthy_food
    """age = int(input('enter your age : '))
    urea = float(input('enter the urea amount : '))
    Cr =int(input('enter the urea amount Creatinine ratio: '))
    HbA1c = float(input('enter the  HbA1c amount : '))
    chol = float(input('enter the cholestrol level: '))
    Tg = float(input('enter the Triglycerides: '))
    BMI = float(input('enter BMI: '))
    gender = int(input('enter your gender (0 : female and 1 : male): '))
    HighBp =  int(input('if high Bp enter 1 else enter 0: '))
    Physical_Activity = int(input('if physical activity is done frequently enter 1 else enter 0: '))
    General_Health = int(input('if overall health is positive enter 1 else enter 0: '))
    Difficulty_walking = int(input('if you have difficulty walking enter 1 else enter 0: '))
    healthy_food = int(input('if you eat healthy food like vegetable and fruits on a daily basis enter 1 else enter 0: '))"""
    try:
        age = int(input('enter your age: '))
        urea = float(input('enter the urea amount: '))
        Cr = int(input('enter the urea amount Creatinine ratio: '))
        HbA1c = float(input('enter the HbA1c amount: '))
        chol = float(input('enter the cholesterol level: '))
        Tg = float(input('enter the Triglycerides: '))
        BMI = float(input('enter BMI: '))
        gender = int(input('enter your gender (0: female and 1: male): '))
        HighBp = int(input('(HighBp :1 else  enter:0): '))
        Physical_Activity = int(input('(if physical activity is done frequently enter: 1) else enter: 0: '))
        General_Health = int(input('( 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor) : '))
        Difficulty_walking = int(input('(if you have difficulty walking enter : 1) else enter : 0: '))
        healthy_food = int(input('(if you eat healthy food like vegetable and fruits on a daily basis enter : 1) else enter : 0: '))

    except ValueError as e:
        print("Error: Invalid input! Please enter valid numeric values.")
        return 0
    if(chol>6.2):
        chol_level=1
    else:
        chol_level=0
    model1 = [age ,urea,Cr,HbA1c,chol,Tg,BMI,gender]
    model2 = [float(HighBp),float(chol_level),BMI,float(Physical_Activity),float(General_Health),float(Difficulty_walking),float(gender),float(age),healthy_food]

    
    
    prediction = Solution(model1,model2)
    o = prediction.output()
    print(o)
    
   



if __name__ == '__main__':
    main()
