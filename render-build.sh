#!/usr/bin/env bash
# exit on error
set -o errexit

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  wget https://chromedriver.storage.googleapis.com/112.0.5615.49/chromedriver_linux64.zip
  #wget https://chromedriver.storage.googleapis.com/index.html?path=113.0.5672.24/
  unzip chromedriver_linux64.zip
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  echo "________________________________________________"
  echo "________________________________________________"
  echo "________________________________________________"
  echo "________________________________________________"
  chromedriver --version
  echo "________________________________________________"
  echo "________________________________________________"
  echo "________________________________________________"
  echo "________________________________________________"
  cd $HOME/project/src # Make sure we return to where we were
else
    echo "FUCK"
fi

# be sure to add Chromes location to the PATH as part of your Start Command
#export PATH="${PATH}:/opt/render/project/.render/chrome/opt/google/chrome"

echo "-------------------------------------------------------------------------------------"
echo "-------------------------------------------------------------------------------------"
echo "-------------------------------------------------------------------------------------"
echo "-------------------------------------------------------------------------------------"
echo "-------------------------------------------------------------------------------------"
echo "-------------------------------------------------------------------------------------"

# add your own build commands...