import pickle

data ={'key1':'value1','key2':[1,2,3]}

with open('data.pickle','wb') as f:
    pickle.dump(data, f)

with open('data.pickle','rb') as f:
    loaded_data = pickle.load(f)

print(loaded_data)