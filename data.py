import pandas as pd
from flask import Flask,jsonify,request

df = pd.read_csv('data.csv')

name = df["Star_name"].to_list() 
mass = df["Mass"].to_list() 
radius = df["Radius"].to_list() 
distance = df["Distance"].to_list() 
gravity = df["Acceleration due to Gravity on this star"].to_list()

final_star_list = []
temp_dict = {}

for i in range(len(name)):
    temp_dict['name'] = name[i]
    temp_dict['mass'] = mass[i]
    temp_dict['radius'] = radius[i]
    temp_dict['distance'] = distance[i]
    temp_dict['gravity'] = gravity[i]
    final_star_list.append(temp_dict)
    temp_dict = {}
    print(final_star_list)

from star_list import data

app = Flask(__name__)
@app.route('/')

def index():
    return jsonify({
        'Data' : data,
        'Massage' : 'Success'
    }),200

@app.route('/star_search')
def star_searh(): 
    name =  request.args.get('Name')
    star_data = next(item for item in data if item['Name'] == name)
    return jsonify({
        'Data' : star_data,
        'message': 'success'
    }),200
if __name__ == '__main__':
    app.run()
