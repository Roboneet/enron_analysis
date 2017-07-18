import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

def data_exploration(data):
	_keys = data.keys()
	_pois = [i for i in data if data[i]['poi'] == 1]
	_features = data[_keys[0]].keys()
	print '======================================'
	print 'Number of data_points :', len(_keys)
	print 'Number of pois :', len(_pois)
	print 'Number of features available :', len(_features)
	print '======================================'
	_nan_features = {}
	for person in data:
		for feature in _features:
			if data[person][feature] == 'NaN':
				if feature in _nan_features:
					_nan_features[feature] += 1
				else:
					_nan_features[feature] = 1

	print 'Number of NaN data points for each feature: '
	for i in _features:
		if i in _nan_features :
			print i , ':', _nan_features[i]
		else :
			print i, ':0' 

	print '========================================'
	_too_many_nans = [ i for i in _nan_features if _nan_features[i] > 100 ]
	print 'There is too less info available about : ' , ', '.join(_too_many_nans)
	print '======================================'


def clean_nans(data, feature_names):
	new_data = {}
	for person in data:
		f = 1
		for feature in feature_names:
			if data[person][feature] == 'NaN':
				f = 0
		if f:
			new_data[person] = data[person]

	return new_data



# def prettify(data, clf, features, labels, features_list, name):
# 	x_min = data[min(data, key=lambda x: data[x][features_list[1]])][features_list[1]];x_max = data[max(data, key=lambda x: data[x][features_list[1]])][features_list[1]];y_min = data[min(data, key=lambda x: data[x][features_list[2]])][features_list[2]];y_max = data[max(data, key=lambda x: data[x][features_list[2]])][features_list[2]]


# 	# Plot the decision boundary. For that, we will assign a color to each
# 	# point in the mesh [x_min, m_max]x[y_min, y_max]. 
# 	h = .01  # step size in the mesh
#     xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
#     Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
#     print 'making mesh'
#     # Put the result into a color plot
#     Z = Z.reshape(xx.shape)
#     plt.xlim(xx.min(), xx.max())
#     plt.ylim(yy.min(), yy.max())

#     plt.pcolormesh(xx, yy, Z, cmap=pl.cm.seismic)

#     # Plot also the test points
#     print 'making points'
#     feature1_non_pois = [features[ii][0] for ii in range(0, len(features)) if labels[ii]==0 ];feature1_pois = [features[ii][0] for ii in range(0, len(features)) if labels[ii]==1 ];feature2_non_pois = [features[ii][1] for ii in range(0, len(features)) if labels[ii]==0 ];feature2_pois = [features[ii][1] for ii in range(0, len(features)) if labels[ii]==1 ];
#     print 'drawing'
#     plt.scatter(feature1_pois, feature2_pois, color = "b", label="poi")
#     plt.scatter(feature1_non_pois,feature2_non_pois, color = "r", label="non_poi")
#     plt.legend()
#     plt.xlabel(features_list[1])
#     plt.ylabel(features_list[2])
#     print 'saving'
#     plt.savefig("images/"+name+".png")
#     plt.show()

def prettified(data, clf, features, labels, features_list, name):
	x_min = data[min(data, key=lambda x: data[x][features_list[1]])][features_list[1]];
	x_max = data[max(data, key=lambda x: data[x][features_list[1]])][features_list[1]];
	y_min = data[min(data, key=lambda x: data[x][features_list[1]])][features_list[2]];
	y_max = data[max(data, key=lambda x: data[x][features_list[1]])][features_list[2]];


	hx = (x_max - x_min)/100.0
	hy = (y_max - y_min)/100.0
	
	xx, yy = np.meshgrid(np.arange(x_min, x_max,hx), np.arange(y_min, y_max, hy))
	Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

	Z.reshape(xx.shape)
	plt.xlim(xx.min(),xx.max())
	plt.ylim(yy.min(),yy.max())

	plt.pcolormesh(xx, yy, Z, cmap=pl.cm.seismic)

	feature1_non_pois = [features[ii][0] for ii in range(0,len(features)) if labels[ii] == 0]
	feature1_pois = [features[ii][0] for ii in range(0,len(features)) if labels[ii] == 1]
	feature2_non_pois = [features[ii][1] for ii in range(0,len(features)) if labels[ii] == 0]
	feature2_pois = [features[ii][1] for ii in range(0,len(features)) if labels[ii] == 1]

	plt.scatter(feature1_pois, feature2_pois, color="b", label="poi")
	plt.scatter(feature1_non_pois, feature2_non_pois, color="r", label="non_poi")
	plt.legend()
	plt.xlabel(features_list[1])
	plt.xlabel(features_list[2])
	plt.savefig('images/'+name+'.png')
	plt.show()
