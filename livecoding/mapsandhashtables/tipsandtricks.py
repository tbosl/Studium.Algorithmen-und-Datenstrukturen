import collections

# nested dictionaries
d = dict()
d = {}
# does not work since we can not create a sub dictionary but only values
# d['key1'][['key2']] = 'value'

# This is how it works but not nice because we have to create the sub dictionary first (bothering)
d['key1'] = {}
d['key1']['key2'] = 'value'
print(d)

# -> use default dictionary

d = collections.defaultdict(dict)  # by default it works on dict (parameter)
d['key1']['key2'] = 'value'
print(d)

# collections has many more helpful classes but they are not relevant for the course but maybe for further career
