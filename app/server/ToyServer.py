from Classes.ToySQL import *
from Classes.Interpretation_functions import *
from keras.models import load_model
from flask import Flask,request,jsonify

obj=DatabaseController()
app = Flask(__name__)

@app.route('/open', methods=['POST'])

#This is the code to connect the server with ToySQL
def open():
    try: 
       data=request.get_json()
       name=data.get('name')
       path=data.get('model')
       model=load_model(path)
       dimension=tuple(data.get('dimension'))
       credentials=list(data.get('credentials'))
       obj.open_conection(name,credentials,model=model,dimension=dimension,function=class_comparation)
       return jsonify({"succes": "Connection open. All schemas are now in RAM"}), 200
    except:
        return jsonify({"error": "Error with connection"}), 400
    
#This is the code to provide security on database
#def login():
    #return 0

#This is the code that send a query to ToySQL
@app.route('/query', methods=['POST'])
def query():
    try: 
       data=request.get_json()
       query=data.get('query')
       val=obj.query(query)
       if val==None:
          return  jsonify({"succes": "Something wrong with kernel"}), 200
       return val
    except:
       return  jsonify({"error": "Something wrong with kernel"}), 500
   

@app.route('/close', methods=['POST'])   
#This is the code that close connection with ToySQL
def close():
    try:
        obj.close_conection()
    except:
        return jsonify({"error": "Something wrong with kernel"}), 500
  
if __name__ == '__main__':
    app.run(port=5000,debug=True)