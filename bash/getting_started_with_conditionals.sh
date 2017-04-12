#!/bin/bash

read inp

if [ $inp == "y" ] || [ $inp == "Y" ]; then
  echo "YES"
elif [ $inp == "n" ] || [ $inp == "N" ]; then
  echo "NO"
fi
