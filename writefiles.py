from sys import argv
from os.path import exists

script, from_file, to_file = argv 

input = open(from_file)
indata = input.read()
if not exists(to_file):
    output = open(to_file, 'w')
    output.write(indata)
    output.close()
input.close()

#Write =  w
#Append =  a  
#Read   = r 
# every open method must be close 
# Main Method = main Class 
