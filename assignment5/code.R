setwd('/Users/Zhongyu/Dropbox/DataScientist/data_manipulate/datasci_course_materials/assignment5');
library(caret)
library(tree)
library(rpart)
library(randomForest)
library(e1071)

# list.files()
seaflow = read.csv('seaflow_21min.csv',header=TRUE)
View(seaflow)
summary(seaflow)
