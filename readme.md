1. Ubuntu
2. python3
3. pip3
4. sudo pip3 install virtualenv
5. 进入项目目录 virtualenv venv
6. pip3 install Flask
7. sudo pip3 install pymongo
8. nginx
9. sudo apt-get install build-essential python-dev
10. sudo pip install uwsgi
11. sudo mkdir -p /var/log/uwsgi
12. sudo chown -R ubuntu:ubuntu /var/log/uwsgi
13. uwsgi --ini ./demoapp_uwsgi.ini