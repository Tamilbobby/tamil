from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from github import Github
from git import Repo
import os

app = Flask(__name__)

app.secret_key = "your secret key" 

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'T@mil2203'
app.config['MYSQL_DB'] = 'varun1'

mysql = MySQL(app)
access_token = "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" 
g = Github(access_token)
user = g.get_user()

# @app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		email = request.form['email']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE email = % s AND password = % s', (email, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			#session['id'] = account['id']
			session['email'] = account['email']
			msg = 'Logged in successfully !'
			return render_template('index.html', msg = msg)
		else:
			msg = 'Incorrect email / password !'
	return render_template('login.html', msg = msg)


@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE email = % s', (email, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO accounts VALUES (% s, % s, % s)', (username, password, email, ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)



#############otherresources########################


@app.route('/index')
def index():
   return render_template('index.html')

@app.route('/providers')
def providers():
   return render_template('Providers.html')

@app.route('/resources')
def resources():
   return render_template('Resource.html')


@app.route('/form')
def form():
   return render_template('Form.html')

#################### ECR START #####################

@app.route('/ecr')
def ecr():
   return render_template('ECR_form.html')

@app.route('/repo', methods=['POST', 'GET']) 
def repo():
   # access_token = "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" 
   repo_name = request.form['repo-name']
   access_key = request.form['access']
   secret_key = request.form['secret']
   region = request.form['region']
   name = request.form['repo-name']
   mutability = request.form['mutability']
   scan = request.form['scan']
   try:
      # g = Github(access_token)
      # user = g.get_user()
      repo = user.create_repo(repo_name, private=True)  
   
      repo_url = f'https://{access_token}@github.com/Tamilbobby/{repo_name}.git'
   #git_clone = repo.clone_url
      directory = f"/user-one/{repo_name}"
   
      #os.system(f'sed -i "s/git .*/git \&apos\;https:\/\/{access_token}\@github.com\/Tamilbobby\/{repo_name}.git\&apos\;/g" /user-one/config.xml')
   
      #os.system(f'java -jar /home/arun/Downloads/jenkins-cli.jar -s http://localhost:8080 create-job {repo_name} < /user-one/config.xml')
   
      Repo.clone_from(repo_url, directory)
      file = directory 
      with open(file, 'w') as f:
          dq = '"'
          values = [f"access_key = {dq}{access_key}{dq}", '\n', f"secret_key = {dq}{secret_key}{dq}", '\n', 
                    f"region = {dq}{region}{dq}", '\n', f"name = {dq}{name}{dq}", '\n', f"mutability = {dq}{mutability}{dq}", '\n', f"scan = {scan}"]
          f.writelines(values)
      repo = Repo(directory)
      os.system(f'cp -r /user-one/terraform/* {directory}')
      repo.git.add('.')
      repo.index.commit("added demo")
      origin = repo.remote(name='origin')
      origin.push()
      msg = "repository created successfully"
   except:   
      msg = "repository already existed"
   finally:
      return render_template('status.html', msg = msg)
   
#################### ECR END #####################

#################### VPC START #####################

@app.route('/vpc')
def vpc():
   return render_template('vpc.html')

@app.route('/virtualprivate', methods=['POST', 'GET'])
def virtualprivate():
   # access_token = "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" 
   
   aim = request.form['aim id']
   instance = request.form['instance type']
   instancekey = request.form['instance key name']
   vpc = request.form['vpc cidr binstancelock']
   subnet = request.form['subnet cidr block']
   route = request.form['route cidr block']
   pro = request.form['Protocol']
   repo_name = request.form['region']
   try:
      # g = Github(access_token)
      #user = g.get_user()
      repo = user.create_repo(repo_name, private=True)
   
      repo_url = f'https://{access_token}@github.com/Tamilbobby/{repo_name}.git'
   
      directory = f"/user-one/ec2-repos/{repo_name}"
   
      Repo.clone_from(repo_url, directory)
      file = directory 

      with open(file, 'w') as f:
         dq = '"'
         values = [f"aim = {dq}{aim}{dq}", '\n', f"instance = {dq}{instance}{dq}", '\n', f"instancekey = {dq}{instancekey}{dq}", '\n', 
                 f"vpc = {dq}{vpc}{dq}", '\n', f"subnet = {dq}{subnet}{dq}", '\n', f"route = {dq}{route}{dq}", '\n', 
                 f"pro = {dq}{pro}{dq}", '\n']
         f.writelines(values)
   
         repo = Repo(directory)
    #os.system(f'cp -r /user-one/ec2-terraform/*.tf {directory}')
         repo.git.add('.')
         repo.index.commit("added demo")
         origin = repo.remote(name='origin')
         origin.push()
         msg = "repository created successfully"
   except:   
      msg = "repository already existed"
   finally:
      return render_template('status.html', msg = msg)
   
#################### VPC END ##################### 

#################### EC2 START #####################
@app.route('/ec2')
def ec2():
   return render_template('Ec2.html')

@app.route('/cloudcompute', methods=['POST', 'GET'])
def cloudcompute():
   # access_token = "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" 
   repo_name = request.form['rt tags']
   azs = request.form['azs']
   routec = request.form['route:cidr']
   region = request.form['region']
   regi   = request.form['region']
   gwtag  = request.form['gw tags']
   access = request.form['access key']
   private = request.form['private subnet:tags']
   secret  = request.form['secret key']
   sec = request.form['secret key']
   
   try:
   #  g = Github(access_token)
    #user = g.get_user()
    repo = user.create_repo(repo_name, private=True)
   
    repo_url = f'https://{access_token}@github.com/Tamilbobby/{repo_name}.git'
   
    directory = f"/user-one/ec2-repos/{repo_name}"
   
    Repo.clone_from(repo_url, directory)
    file = directory 

    with open(file, 'w') as f:
       dq = '"'
       values = [f"region = {dq}{region}{dq}", '\n', f"access = {dq}{access}{dq}", '\n', f"secret = {dq}{secret}{dq}", '\n',  
                 f"sec = {dq}{sec}{dq}", '\n', f"azs = {dq}{azs}{dq}", '\n', f"routec = {dq}{routec}{dq}", '\n', 
                 f"regi = {dq}{regi}{dq}", '\n', f"gwtag = {dq}{gwtag}{dq}", '\n', f"private = {dq}{private}{dq}"]
       f.writelines(values)
   
    repo = Repo(directory)
    #os.system(f'cp -r /user-one/ec2-terraform/*.tf {directory}')
    repo.git.add('.')
    repo.index.commit("added demo")
    origin = repo.remote(name='origin')
    origin.push()
    msg = "repository created successfully"
   except:   
      msg = "repository already existed"
   finally:
      return render_template('status.html', msg = msg)
#################### VPC END #####################

#################### EKS START #####################

@app.route('/eks')
def eks():
   return render_template('EKS.html')

@app.route('/eksrepo', methods=['POST', 'GET'])
def eksrepo():
   # access_token = "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" 
   repo_name = request.form['rt tags']
   azs = request.form['azs']
   routecidr = request.form['route:cidr']
   region = request.form['region']
   gw_tag = request.form['gw tags']
   eks_access = request.form['access key']
   eks_private = request.form['private subnet:tags']
   secret = request.form['secret key']
   
   
   # g = Github(access_token)
   #user = g.get_user()
   repo = user.create_repo(repo_name, private=True)
   
   repo_url = f'https://{access_token}@github.com/Tamilbobby/{repo_name}.git'
   
   directory = f"/user-one/eks-repos/{repo_name}"
   
   Repo.clone_from(repo_url, directory)
   file = directory
   
   with open(file, 'w') as f:
      dq = '"'
      values = [f"region = {dq}{region}{dq}", "\n", f"eks_access= {dq}{eks_access}{dq}", "\n" 
                f"secret = {dq}{secret}{dq}", "\n", f"azs = {dq}{azs}{dq}", "\n", 
                f"eks_private = {dq}{eks_private}{dq}", "\n", f"routecidr = {dq}{routecidr}{dq}", "\n",f"gw_tag = {dq}{gw_tag}{dq}" ]
      f.writelines(values)
   
   repo = Repo(directory)
   #os.system(f'cp -r /user-one/eks-terraform/*.tf {directory}')
   repo.git.add('.')
   repo.index.commit("added demo")
   origin = repo.remote(name='origin')
   origin.push()
   
   return 'success'

#################### EKS END #####################

#################### S3 START #####################

@app.route('/bucket')
def bucket():
   return render_template('S3.html')

@app.route('/bucketrepo', methods=['POST', 'GET'])
def bucketrepo():
   # access_token = "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" 
   repo_name = request.form['rt tags']
   azs = request.form['azs']
   # g = Github(access_token)
   #user = g.get_user()
   repo = user.create_repo(repo_name, private=True)
   
   repo_url = f'https://{access_token}@github.com/Tamilbobby/{repo_name}.git'
   
   directory = f"/user-one/s3-repos/{repo_name}"
   
   Repo.clone_from(repo_url, directory)
   file = directory 
   
   with open(file, 'w') as f:
      dq = '"'
      values = [f"azs = {dq}{azs}{dq}"]
      f.writelines(values)
   
   repo = Repo(directory)
   #os.system(f'cp -r /user-one/s3-terraform/*.tf {directory}')
   repo.git.add('.')
   repo.index.commit("added demo")
   origin = repo.remote(name='origin')
   origin.push()
   
   return 'success'

#################### S3 END #####################

#################### RDS START #####################

@app.route('/rds')
def rds():
   return render_template('RDS.html')

@app.route('/rdsrepo', methods=['POST', 'GET'])
def rdsrepo():
   # access_token = "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" 
   repo_name = request.form['rt tags']
   azs = request.form['azs']
   routec = request.form['route:cidr']
   region = request.form['region']
   reg = request.form['region']
   gwtag = request.form['gw tags']
   access =  request.form['access key']
   private = request.form['private subnet:tags']
   secret = request.form['secret key']
   sec = request.form['secret key']

   
   # g = Github(access_token)
   # user = g.get_user()
   repo = user.create_repo(repo_name, private=True)
   
   repo_url = f'https://{access_token}@github.com/Tamilbobby/{repo_name}.git'
   
   directory = f"/user-one/rds-repos/{repo_name}"
   
   Repo.clone_from(repo_url, directory)
   file = directory 
   
   with open(file, 'w') as f:
      dq = '"'
      values = [f"region = {dq}{region}{dq}", "\n", f"access = {dq}{access}{dq}", "\n", f"secret = {dq}{secret}{dq}", "\n",
                f"azs = {dq}{azs}{dq}", "\n", f"sec = {dq}{sec}{dq}", "\n", f"reg = {dq}{reg}{dq}", "\n", 
                f"private = {dq}{private}{dq}", "\n", f"gwtag = {dq}{gwtag}{dq}", "\n", f"routec = {dq}{routec}{dq}"]
      f.writelines(values)
   
   repo = Repo(directory)
   #os.system(f'cp -r /user-one/rds-terraform/*.tf {directory}')
   repo.git.add('.')
   repo.index.commit("added demo")
   origin = repo.remote(name='origin')
   origin.push()   
   
   return 'success'

#################### RDS END #####################
#####################google cloud############

@app.route('/googlecloud')
def googlecloud():
   return render_template('googlecloud_index.html')




@app.route('/googlevpc')
def googlevpc():
   return render_template('googlevpc.html')


@app.route('/googlecloudvpc', methods=['POST', 'GET'])
def googlecloudvpc():
    repo_name = request.form['project id']
    vpcn = request.form['vpc name']
    Credential = request.form['Credentials']
    route = request.form['routing-mode']
    subnet = request.form['sub-net-name']
    subnetc = request.form['subnet-cidr']
    

   
   # g = Github(access_token)
   # user = g.get_user()
    repo = user.create_repo(repo_name, private=True)
   
    repo_url = f'https://{access_token}@github.com/Tamilbobby/{repo_name}.git'
   
    directory = f"/user-one/rds-repos/{repo_name}"
   
    Repo.clone_from(repo_url, directory)
    file = directory 
   
    with open(file, 'w') as f:
       dq = '"'
       values = [f"vpcn = {dq}{vpcn}{dq}", "\n", f"Credential = {dq}{Credential}{dq}", "\n", f"route = {dq}{route}{dq}", "\n",
                f"subnet = {dq}{subnet}{dq}", "\n", f"subnetc = {dq}{subnetc}{dq}"]
       f.writelines(values)
   
       repo = Repo(directory)
   #os.system(f'cp -r /user-one/rds-terraform/*.tf {directory}')
       repo.git.add('.')
       repo.index.commit("added demo")
       origin = repo.remote(name='origin')
       origin.push()   
   
       return 'success'


if __name__ == '__main__':
   app.run(debug=True)