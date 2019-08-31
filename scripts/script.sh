#!/bin/bash

MY_LIST=(1 2 3 4)

function print_my_i() {
    echo "This $1 is good"
}

for i in ${MY_LIST[@]}; do
    value=$(print_my_i $i)
    echo $value
done
