#!/bin/sh


tmux new-session -d -s main ;
tmux split-window -h ;
tmux select-pane -L
tmux send-keys -t main 'ls' C-m
tmux select-pane -R
tmux send-keys -t main 'htop' C-m
tmux attach-session -d -t main 
