#!/bin/bash

gcc lib/LinkedList/LinkedList.c -c
gcc lib/Stack/Stack.c -c
gcc main.c -c
gcc main.o LinkedList.o Stack.o -o main

clear
./main

rm main.o Stack.o LinkedList.o main