#####################################################
#			Imports									#
#####################################################

from app import app

#####################################################
#			Script									#
#####################################################

if __name__ == "__main__":

    app.run(debug=True, port=5000, use_reloader=True)
