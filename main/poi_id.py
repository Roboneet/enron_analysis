#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")
import matplotlib.pyplot as plt
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data


from helper import *

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary', 'from_this_person_to_poi'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

data_exploration(data_dict)
### Task 2: Remove outliers
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = clean_nans(data_dict, features_list[1:3])
my_dataset.pop('TOTAL',0)


### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

color = 'b'
for point in data:
	if point[0] == 1:
		color = 'r'
	else:
		color = 'b'
	plt.scatter(point[1],point[2],color=color)

max_feature_1 = max(my_dataset, key=lambda x: my_dataset[x][features_list[1]])
max_feature_2 = max(my_dataset, key=lambda x: my_dataset[x][features_list[2]])
print 'max ',features_list[1],':', max_feature_1
print 'max ',features_list[2],':', max_feature_2
plt.xlabel(features_list[1])
plt.ylabel(features_list[2])

plt.savefig('./images/'+features_list[1]+'-'+features_list[2]+'.png')
plt.show()
### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion="entropy",random_state=100)

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
print 'splitting'
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=25)

print 'training...'
clf.fit(features_train, labels_train)
print 'predicting'
pred = clf.predict(features_test)

from sklearn.metrics import precision_score, recall_score
print 'precision: ', precision_score(labels_test, pred, average="macro")
print 'recall: ', recall_score(labels_test, pred, average="macro")


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)



