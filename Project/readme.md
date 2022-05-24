
# This is our Best submissions 
# Table of CV accuracy 
| Student Names      | Model |  CV - Score    |  Model Accurcay |  Kaggle Accuracy | 
| -------------| ------------- |  -------------| ------------- |  ------------- |
| Qavi Kamal - 64145| KNN           | 0.6610055555555556      | 0.6886833333333333 |   0.68713 | 
| Mustafa noorani - 64177  |Lidstion  |  0.5476253968253968      | 54.7937037037037| 0.54220 |
| Ashar khan - 64271 | SVM |   59.22430555555556    | 59.24791666666667 | 0.58956 |
| Riyan Shahid - 64254  | Perceptron  | 0.5429641975308642     | 57.39  |0.57250|
| Asad Aslam- 64286  | Laplace | 0.6018847222222223 |0.6240411111111111 | 0.62404 |


### ---------------Qavi kamal---------------
### ----Problem----: Accuracy is 50% after increasing the neighbours , to learn the libraries and parameters of model 
### ----Sol----:
### So i have taken the best varriance columns(features) fron f-19 to f-28 with 80 20 split ratio then i made a submission good accuracy of 68% with 25 neighbours. To learn the machine leaining stuff. i used the google search and youtube to learn which model could be best for the given dataset So the best.accuracy we have got in KNN by implementing above parameters and techniques And take the mean of 5 consective values. I didnt take the Extra tree classifier values because the features i got with the libaray doesnt effect the result that much and giving accuracy of 51% so i take the feature with varriance. Even after doing parameter tuning it with grid gives the same result but it take 18 hours to give result and result only increased 0.0111% so it is not suitable. so i submit my best score in best time and that was simple KNN with best feature  according to varriances values of cross validation.But KNN does'nt give good result on large datasets . Most of the code optimize from https://scikit-learn.org/stable/modules/cross_validation.html
![image](https://user-images.githubusercontent.com/99618952/169701199-eaec436e-29db-4ca0-a29b-aa4cd0bb1574.png)
![image](https://user-images.githubusercontent.com/99618952/169701222-0214001c-1252-4d24-a17f-39743df8e34f.png)

## Muhammad Mustafa 
### Problem: Accuracy is 51% with 29 features but then some unimportent features remove which is 3 which increase my accuracy
### Sol: So i made a submission with improve accuracy of 54% what i going through is 27 features with 70 30 split ratio.
![image](https://github.com/qavikamal2323/Ai266-spring22/blob/0d6343b298fb69de93773990d4faf514372bc38c/Project/Mustafa-lidstone.JPG)
## Asad Aslam
### Problem: Accuracy is 58% with 29 features but then some unimportent features remove which increase my accuracy
### Sol: So i made a submission with improve accuracy of 62% what i am going through is 5 features with 80 20 split ratio.
![image](https://user-images.githubusercontent.com/92552475/169676212-be5563aa-2a22-465b-88e2-f59f1da7f3d5.png)

## Riyan Shahid
### Problem: Accuracy is 52% with 29 features but then some unimportent features remove which increase my accuracy
### Sol: So i made a submission with improve accuracy of 57% what i am going through is 5 features with 80 20 split ratio.
![image](https://user-images.githubusercontent.com/65994423/169720771-0f9e787c-ec7c-4254-b9c5-c7da93878fe8.png)

## Ashar Khan
### Problem: Accuracy is 56% with 29 features but then some unimportent features remove which increase my accuracy, In this svm model , I'm doing  one more experiment to increase the accuracy , using standard scalar function to change the data type and SVM function parameter (gamma = "scale") . But problem is that , my computer not train this model its take so many time , I'm try 15 hours but its not train because its huge number of rows , if i reduce the number of rows , then its trained and if I increase the number of rows then increase the model accuracy . experiment in "AsharKhan_64271_SVM_Model_project.ipynb" file 
### Solution: So i made a submission with improve accuracy of 58% what i am going through, select  f_00 to f_02 and f_19 to f_26 features with 80 20 split ratio.
![image](https://github.com/qavikamal2323/Ai266-spring22/blob/main/Project/SVM_KAGGLE_SCORE_Project.PNG?raw=true)
