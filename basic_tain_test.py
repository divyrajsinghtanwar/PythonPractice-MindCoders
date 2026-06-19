from sklearn.model_selection import train_test_split,cross_val_score
import numpy as np


#Simulated dataset : 500 student records
np.random.seed(42)
X = np.random.randn(500,5) #5 feature (study hrs ,attendence,etc for 500 student)
y = np.random.randint(0,2,500) #label pass(1)/fail(0) for 500 student

#80/20 Train-test split
X_train,X_Test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42,stratify=y
)
print(f'Training samples : {len(X_train)}|Test samples :{len(X_Test)}')

#5-fold cross validattion -more reliable than single split
from sklearn.ensemble import RandomForestClassifier
model =RandomForestClassifier(n_estimators=50,random_state=42)
cv_scores = cross_val_score(model,X,y,cv =5,scoring = 'accuracy')
print(f'Cv scores each fold: {cv_scores.round(3)}')
print(f'mean: {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}')