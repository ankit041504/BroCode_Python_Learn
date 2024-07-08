# BroCode_Python_Learn
Code sample from youtube video - Bro-Code Python full 

/* create python VENV in VS code */

.venv\Scripts\Activate.ps1

/* In terminal */

pip install dbt-bigquery
pip3 install apache-beam[gcp]
python.exe -m pip install --upgrade pip
gcloud auth application-default login   
dbt init
dbt debug

/* For git */


git status
git add .
git checkout -b dbt_first /*dbt_first is my project name to create same name branch*/
git add .
git commit -a -m 'saved branch first'
git push --set-upstream origin dbt_first  /*dbt_first is my branch name*/



/*if any access issue occure in VS code which is npt allowing to run any command in terminal*/

Get-ExecutionPolicy
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser