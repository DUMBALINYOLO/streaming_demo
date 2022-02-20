

1. python -m venv venvname

2. venvname\scripts\activate if windows

3. python -m pip install --upgrade pip

4. pip install -r requirements.txt


5. python manage.py migrate

6. MAKE SURE YOUR REDIS IS RUNNING ON THE BACKGROUND ON THE DEFAULT REDIS PORT

7. open another cmd and navigate to where your project is and activate your virtual environment

8. celery -A demo worker -l info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo 
NB run that script

9. open another cmd and navigate to where your project is and activate your virtual environment

10. celery -A demo beat -l INFO

NB: run that script

11. open another cmd and navigate to where your project is and activate your virtual environment

12. python manage.py runserver

13. go to http://127.0.0.1:8000

14. Click ok to the alert and your data will start streaming and you can always run an inspect and go to your browser console and the data shall be outputed there. Same shall apply to the chart from chart.js



CHECK THE task.py in streams thats where your your put data in the redis chanel_layer
and check on consumers too on stream folder thats where the broadcast_finance method is 
the one grabing data from event stream and publishes to your users. If you check very well
I convert the integer to string, because an integer can not be encoded to bytes and the 
websockets would cause an encode error



