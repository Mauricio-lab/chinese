#!/usr/bin/env bash
#!/usr/bin/env bash
# exit on error
./opt/render/project/src/.venv/bin/python -m pip install --upgrade pip
set -o errexit

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget https://chromedriver.storage.googleapis.com/95.0.4638.54/chromedriver_linux64.zip
  #wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  #dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  unzip chromedriver_linux64.zip
  #./chromedriver
  #cd opt
  #cd google
  #cd chrome  
  #ls -la
  #cd ..
  #cd ..
  #cd ..

  rm ./google-chrome-stable_current_amd64.deb
  cd $HOME/project/src # Make sure we return to where we were
#eee
else
  echo "...Using Chrome from cache"
fi
export PATH=$PATH:/opt/render/.local/share/pyppeteer/local-chromium/
export PATH=$PATH:/opt/render/project/.render/chrome
