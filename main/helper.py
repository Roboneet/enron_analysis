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

