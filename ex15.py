from sys import argv

print "I'll also ask you to type it again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
print txt_again.close
