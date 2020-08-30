# Homework 5, Introduction to Computer Science


This repository contains a python script that was written for an Intro to CS class. The assignment was to write a dissasembler for a Little Man Computer (LMC) program. 

The main function reads all the operation codes as supplied as input from the user. The main function will continue to take in operation codes until the HLT instruction is read. All operation codes are passed onto the disassembler function. 

The disassembler function takes in an operation code as an integer and converts it to a LMC mnemonic instruction and returns the instruction as a string. The leftmost value of the operation code indicates the LMC command. The remaining two digits denote the location of the data. The disassembler prints the final command and data location to shell.

The pool of operation codes are defined below:

1 : ADD

2 : SUB

3 : STA 

4 : LDA

5 : BRA

6 : BRZ

7 : BRP

