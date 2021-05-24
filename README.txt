1. Setup the Python Virtual Environment (for Linux)
$ bash
$ virtual venv -p $(which python3) 	<-- this cmd will install virtual env. 
$ source ./venv/bin/activate	<-- this cmd will activate the virtual env. 
$ pip3 install --upgrade pip

# You know if the virtual env. is activate when you see (venv) appear before the name of the host server

2. Download the necessary libraries while Virtual Environment is activate:

#install each package manually one by one
$ pip install pytop
$ pip install pyqrcode
$ pip install pypng 

OR

#install all packages specified in requirements.txt
$ pip install -r requirements.txt


3. Generate the QR Code

# To generate a qr code that can be read by Google authenticator, run the following command:

	$ python otp.py generate-qr

4. Scan the QR Code

# The qr code is generated as 'myqr.png'. Scan that qr using Google's 'Authenticator' app
(installed on your phone) which will then generate a one-time password using the qr code

5. Generate otp using source code

# After you have scanned the qr code generated from step 3, create the
one-time password (using the program) with the following command:

# Please note: if you run this cmd every 30 seconds the resulting otp will be different

	$ python otp.py generate-otp 

6. Compare the otps generated using the authenticator app and the program. 
Are they the same? If not wait another 30 seconds and run the above cmd again.	

#To deactivate virtual env. type 'deactivate' in the cmd line
