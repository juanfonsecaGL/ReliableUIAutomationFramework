#!/bin/bash

# TODO: migrate to a makefile when I have time

binFolder=~/Library/Python/3.7/bin/
chromeZip=chrome.zip
venvFolder=./test_automation

export PATH=$binFolder:$PATH
virtualenv $venvFolder
source $venvFolder/bin/activate
pip install -r requirements.txt
curl -o $chromeZip https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_mac64.zip
unzip $chromeZip
mv chromedriver $binFolder
behave

# clean
rm $chromeZip
rm -r $venvFolder
