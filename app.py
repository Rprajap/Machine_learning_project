import sys
import logging
from flask import Flask
from housing.exception import HousingException


app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custum Exception")
    except Exception as e:
        housing = HousingException(e,sys)
        
        logging.info("We are testing a logging module")
        return "Starting machine learning project ci/cd pipeline is pending from your side"

if __name__ == "__main__":
    app.run(debug=True)
        