setwd('/Users/Zhongyu/Dropbox/DataScientist/data_manipulate/datasci_course_materials/assignment5');
library(caret)
library(tree)
library(rpart)
library(randomForest)
library(e1071)

# list.files()
seaflow <-  read.csv('seaflow_21min.csv',header=TRUE)
View(seaflow)
# ****** Answers to questions 2, 3
summary(seaflow)

# *** Split data into training and testing set
set.seed(257209)
inTrain <-  createDataPartition(y=seaflow$pop,p=.7,list=FALSE)
training <-  seaflow[inTrain,]
testing <-  seaflow[-inTrain,]
# ****** Answers to question 4 (change seed could change the result)
meanOfTime_train = mean(training$time)

# *** Form formula and train a model, build a decision tree
formula1 <-  formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model1 <- rpart(formula1, method='class', data=training)
# ****** Answers to question 5, 6, 7, 8
print(model1)
# *** Evaluate test set
predTestMatrix1 <-  predict(model1, testing)
getPop <- function(predTestMatrix){
   predPop = vector("character",length=dim(predTestMatrix)[1])
   testLen = 1:dim(predTestMatrix)[1]
   labels = c('crypto', 'nano', 'pico', 'synecho', 'ultra')
  for (row in testLen) {
    predPop[row] = labels[predTestMatrix[row,]==max(predTestMatrix[row,])]
  }
  predPop
}
# ****** Answer to question 9
predTestPop1 <-  getPop(predTestMatrix1)
accuracy1 <-  sum(predTestPop1 == testing$pop)/dim(testing)[1]

# *** Build and evaluate a random forest
model2 <- randomForest(formula1, data = training)
predTestPop2 <- predict(model2, testing)
# ****** Anaswer to question 10
accuracy2 <- sum(predTestPop2 == testing$pop)/length(predTestPop2)

# *** Build and train a SVM model, evaluate model performance *** answers to question 12
model3 <- svm(formula1, data=training)
predTestPop3 <- predict(model3, testing)
accuracy3 <- sum(predTestPop3 == testing$pop)/length(predTestPop3)

# *** Construct confusion matrix *** answers to question 13
table(pred = as.factor(predTestPop1), true = testing$pop)
table(pred = predTestPop2, true = testing$pop)
table(pred = predTestPop3, true = testing$pop)
# Note: except decision tree model1, directly print model2 and model 3,
# will automatically print out confusion matrix

# *** Sanity check the data
plot(seaflow$time, seaflow$fsc_small)
plot(seaflow$time, seaflow$fsc_perp)
plot(seaflow$time, seaflow$fsc_big) # *** the non-continuous variable
plot(seaflow$time, seaflow$pe)
plot(seaflow$time, seaflow$chl_big)
plot(seaflow$time, seaflow$chl_small)

# *** Investigate time vs. chl_big, remove possibly miscalibrated data files, re-train/rebuild the models
fileid208 = seaflow$file_id == 208
sel_seaflow = seaflow[!fileid208,]
plot(sel_seaflow$time, sel_seaflow$chl_big)
plot(sel_seaflow$time, sel_seaflow$fsc_big)
set.seed(257209)
inTrain2 = createDataPartition(y=sel_seaflow$pop, p = .7, list = FALSE)
sel_training = sel_seaflow[inTrain2,]
sel_testing = sel_seaflow[-inTrain2,]
# decision tree
sel_model1 <- rpart(formula1, method='class', data=sel_training)
print(sel_model1)
sel_predTestMatrix1 <- predict(sel_model1, sel_testing)
sel_predTestPop1 <- getPop(sel_predTestMatrix1)
sel_accuracy1 <-  sum(sel_predTestPop1 == sel_testing$pop)/dim(sel_testing)[1]
# random forest
sel_model2 <- randomForest(formula1, data=sel_training)
sel_predTestPop2 <- predict(sel_model2, sel_testing)
sel_accuracy2 <- sum(sel_predTestPop2 == sel_testing$pop)/length(sel_predTestPop2)
# SVM
sel_model3 <- svm(formula1, data=sel_training)
sel_predTestPop3 <- predict(sel_model3, sel_testing)
sel_accuracy3 <- sum(sel_predTestPop3 == sel_testing$pop)/length(sel_predTestPop3)
