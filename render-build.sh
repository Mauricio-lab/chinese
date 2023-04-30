#!/usr/bin/env bash
# exit on error
#apt-get -y install psmisc
#killall apt apt-get
#set -o errexit STORAGE_DIR=/opt/render/project/.render 
#if [[ ! -d $STORAGE_DIR/ ]]; then 
echo "...Downloading Chrome" 
#mkdir -p $STORAGE_DIR/chrome 
#sudo cd $STORAGE_DIR/chrome 
apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4
#curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
#echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
apt-get -y install google-chrome-stable
wget -N https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip -P
unzip ~/chromedriver_linux64.zip -d
mv -f ~/chromedriver /usr/local/bin/chromedriver
chown root:root /usr/local/bin/chromedriver
chmod 0755 /usr/local/bin/chromedriver

#wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
#unzip ./google-chrome-stable_current_amd64.deb 
#rm ./google-chrome-stable_current_amd64.deb 
#cd $HOME/project/src 
# Make sure we return to where we were
#else 
#    echo "...Using Chrome from cache"
#fi

