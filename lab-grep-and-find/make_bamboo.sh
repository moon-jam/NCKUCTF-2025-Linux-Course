#!/bin/bash

CHALLENGE_DIR="where_is_bamboo"
FLAG="NCKUCTF{}"

rm -rf "$CHALLENGE_DIR"
mkdir "$CHALLENGE_DIR"
cd "$CHALLENGE_DIR"

current_dir="."
for i in $(seq 1 100); do
    new_dir=$(openssl rand -hex 4)
    mkdir "$current_dir/$new_dir"
    echo "no bamboo qq" > "$current_dir/$new_dir/bamboo$i.txt"
    current_dir="$current_dir/$new_dir"
done

echo "$FLAG" > "$current_dir/flag.txt"
