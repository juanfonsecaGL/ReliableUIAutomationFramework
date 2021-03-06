#!/bin/bash

binFolder=~/Library/Python/3.7/bin/
chromeZip=chrome.zip
venvFolder=.test_automation
chromeVersion=80.0.3987.106

export PATH=$binFolder:$PATH
virtualenv $venvFolder
source $venvFolder/bin/activate
pip install -r requirements.txt
curl -o $chromeZip https://chromedriver.storage.googleapis.com/$chromeVersion/chromedriver_mac64.zip
unzip $chromeZip
mv chromedriver $binFolder
rm $chromeZip

echo
echo "FINISHED!!!"
