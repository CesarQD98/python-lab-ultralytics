#!/bin/bash

while getopts ":m:" opt; do
  case $opt in
  m) yolov8_model_file=$OPTARG ;;
  \?)
    echo "Invalid option -$OPTARG" >&2
    exit 1
    ;;
  :)
    echo "Option -$OPTARG requires an argument." >&2
    exit 1
    ;;
  esac
done

if [ ! -e "$yolov8_model_file" ]; then
  echo "Model file path (.pt) does not exist → $yolov8_model_file" >&2
  exit 1
fi

cmd="python model_train/main.py -m \"$yolov8_model_file\""

if [ "$(uname)" == "Darwin" ] || [ "$(uname)" == "Linux" ]; then
  source env/bin/activate
else
  source env/Scripts/activate
fi

eval "$cmd"
