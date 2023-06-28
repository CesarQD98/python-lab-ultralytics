#!/bin/bash

while getopts ":m:c:" opt; do
  case $opt in
  m) yolov8_model_file=$OPTARG
    ;;
  c) data_training_config=$OPTARG
    ;;
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

# if [[ $required_flag_count -lt 2 ]]; then
#   echo "Please provide at least two required flags and their arguments." >&2
#   exit 1
# fi

# if [ ! -e "$yolov8_model_file" ]; then
#   echo "Model file path (.pt) does not exist → $yolov8_model_file" >&2
#   exit 1
# fi

cmd="python model_train/main.py"

if [ ! -z "$yolov8_model_file" ]; then
  cmd="$cmd -m \"$yolov8_model_file\""
fi

if [ ! -z "$data_training_config" ]; then
  cmd="$cmd -c \"$data_training_config\""
fi

if [ "$(uname)" == "Darwin" ] || [ "$(uname)" == "Linux" ]; then
  source env/bin/activate
else
  source env/Scripts/activate
fi

eval "$cmd"
