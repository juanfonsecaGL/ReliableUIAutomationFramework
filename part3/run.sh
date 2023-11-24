#!/bin/bash

#binFolder=~/Library/Python/3.7/bin/
venvFolder=../.test_automation

#export PATH=$binFolder:$PATH
source $venvFolder/Scripts/activate
behave
