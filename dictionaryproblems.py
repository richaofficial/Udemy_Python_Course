d1={'simple_key':'hello'}
d1['simple_key']
d2={'k1':{'k2':'hello'}}
d2['k1']['k2']
d3={'k1':[{'nest_key':['this is deep',['hello']]}]}
d3['k1'][0]['nest_key'][1][0]

print(d3['k1'][0]['nest_key'][1][0])

