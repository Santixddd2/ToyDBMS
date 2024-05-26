import requests
import json
from tkinter import *
import click
import os

toysql_art = """
__        __   _                            _           
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___     
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |   
 __\_/\_/ \___|_|\___\___/|_|_|_| |_|\___|  \__\___/    
|_   _|__  _   _/ ___| / _ \| |                         
  | |/ _ \| | | \___ \| | | | |                         
  | | (_) | |_| |___) | |_| | |___                      
  |_|\___/ \__, |____/ \__\_\_____| _               __  
           |___/      | ____|_ __  (_) ___  _   _   \ \ 
                      |  _| | '_ \ | |/ _ \| | | | (_) |
                      | |___| | | || | (_) | |_| |  _| |
                      |_____|_| |_|/ |\___/ \__, | ( ) |
                                 |__/       |___/  |/_/ 
    """
headers = {
    'Content-Type': 'application/json'
}

def print_data(data):
        col=""
        lim=""
        Sdat=""
        columns=[]
        dat=[]
        for key in data:
            columns.append(key)
            dat.append(data[key])
            try:
                col=col+"| "+ key+" |"
                lim=lim+"---------"
            except:
                col=col+"| "+ key+" |"
                lim=lim+"---------"
        x=len(dat[0])*len(dat)
        print("\n"+col)
        keys=list(data.keys())
        for i in range(0,len(dat[0])):
            print(lim)
            for j in range(0,len(columns),1):
                Mdat=data[keys[j]]
                try: 
                   Sdat=Sdat+"| "+Mdat[i]
                except:
                    break
            print(Sdat)
            Sdat=""

def query():
    while True:
       q=input("ToySQL> ")
       data={"query":q}
       data_json = json.dumps(data)
       response = requests.post('http://127.0.0.1:5000/query', headers=headers, data=data_json)
       try:         
          response=json.loads(response.text)
          print_data(response)
       except:
          print(response)

def open_conection(data):
    data_json = json.dumps(data)
    print("Opening conection...")
    response = requests.post('http://127.0.0.1:5000/open', headers=headers, data=data_json)
    print("r: ",response.text)
    #print(toysql_art)
    #query()

@click.command()
@click.argument('name',type=str)
@click.argument('model',type=str)
@click.argument('dimension',type=click.Tuple([int, int,int]))
def main(name,model,dimension):
    data = {
    "name": name,
    "model": model,
    "dimension": dimension,
    "credentials":[]
     }
    open_conection(data)
    
if __name__ == '__main__':
    main()


