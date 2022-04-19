
## Run 24/7 on simdoc :  

apt install screen   
cd ~/Developer/Davinci     
screen -S Davinci  
python3 app.py   

--------- or using PM2 ---------- 
https://pm2.keymetrics.io/docs/usage/quick-start/

npm install pm2@latest -g 
pm2 start python3 app.py 

pm2 restart app_name  
pm2 reload app_name  
pm2 stop app_name  
pm2 delete app_name  
