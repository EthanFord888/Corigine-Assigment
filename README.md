# Corigine Fibonacci Assignment

Program used to find the index of the first ter in the Fibonacci sequence to contain N digits. 

Enter "N" to find the index in the Fibonacci sequence

## Requirements
- [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)

## Step 1: Download 

- Download the zip folder from this repository and [navigate to the folder](https://stackoverflow.com/questions/40146104/is-there-a-way-to-open-command-prompt-in-current-folder#:~:text=Just%20go%20to%20your%20folder,cmd%22%20on%20the%20address%20bar.&text=You%20can%20also%20use%20Alt,focus%20to%20the%20address%20bar.) in your command line or text editor.

## Step 2: Build image

` docker build -t fibonacci-term .`

## Step 3: Start container 

`docker run --rm -i -t fibonacci-term`

## Step 4: Enter "N" 

`Enter N: ## `


