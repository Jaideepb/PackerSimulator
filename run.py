#!flask/bin/python
from app import app
from app.start import start_main

start_main()
app.run(debug=True, host='10.48.150.154')
# app.run(debug=True)