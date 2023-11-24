#!/bin/bash

binFolder=~/Library/Python/3.7/bin/
chromeZip=chrome.zip
venvFolder=.test_automation
#chromeVersion=119.0.6045.160

pip install virtualenv

export PATH=$binFolder:$PATH
python -m virtualenv $venvFolder
#virtualenv $venvFolder
source $venvFolder/Scripts/activate
pip install -r requirements.txt
#curl -o $chromeZip https://chromedriver.storage.googleapis.com/$chromeVersion/chromedriver_mac64.zip
#unzip $chromeZip
#mv chromedriver $binFolder
#rm $chromeZip

echo
#echo "FINISHED!!!"
