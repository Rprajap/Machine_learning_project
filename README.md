# Machine_learning_project
Software & Account Requirements:

1. [Github Account]
2. [Heroku Account]
3. [VS code]
4. [Git cli]
5. Git Document [https://git-scm.com/doc]



Creating a conda enviroment

'''
conda create -p venv python==3.7 -y
'''
activate vertual envirometn

'''
conda activate venv/
'''
or
'''conda activate venv'''

if using cmd then  run below command

conda init cmd.exe

pip install -r requirements.txt

making changes availabael to github

note :- To ignoe file or folder from git we can write name of file/folder in .gitignore

git add filename :- will maintain version of file name
or
git add file1 file2....filen

git add . :- will all file


git status


git log :- to check all version maintained by git

to create a version/commit all change by git

'''
git commit -m "message"
'''
whenever we commit a changes it create a vearsion of it

to send version / changes to github
''' git push origin main'''


to check remote url
'''git remote -v '''

to know what new aded 
'''git diff'''

To setup ci/cd pipline in heroku we need three information
1. Heroku Email
2. Heroku_Api_Key
3. Heroku_app_name  

Build Docker image.
'''
docker -build -t <image_name>:<tagname> .
'''

Note :- image name for docker musr be in lowercase

To list docker images
'''
docker images
'''
To run docker image
'''
docker run -p 5000:5000 -e PORT=5000 fc5ef00ca76b 
'''
To check running container in docker

'''
docker ps
'''
To stop docker  container.
'''docker stop container_id'''

'''
python setup.py install
'''

install ipynbkernel

'''
pip install ipykernel  
'''










