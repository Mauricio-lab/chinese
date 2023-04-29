#!/usr/bin/env bash
# exit on error
set -o errexit STORAGE_DIR=/opt/render/project/.render 
if [[ ! -d $STORAGE_DIR/chrome ]]; then 
    echo "...Downloading Chrome" 
    sudo mkdir -p $STORAGE_DIR/chrome 
    sudo cd $STORAGE_DIR/chrome 
    wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
    sudo dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome 
    sudo rm ./google-chrome-stable_current_amd64.deb 
    cd $HOME/project/src 
    # Make sure we return to where we were
    else 
        echo "...Using Chrome from cache"
    fi

