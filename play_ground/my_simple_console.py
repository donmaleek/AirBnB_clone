#!/usr/bin python3

import cmd
import re
#from shlex import split
#from models import storage

class mycmd(cmd.Cmd):
	intro = """welcome to ENG. Mathias Mramba Console, 
		Are you Ready to do hard things?
		Type 'help' for more commands. \n"""
	prompt = "$"
	__classes = {
		"BaseModel",
		"User",
		"State",
		"City",
		"Place",
		"Amenity",
		"Review"
	}
	def do_greet(self, arg):
		"""Greets the user"""
		print("Howdy Engineer, how may I help you DO Hard things.")
	
	def do_quit(self, arg):
		"""Quit command to exit program."""
		return True
	
	def do_EOF(self, arg):
		"""EOF signal to exit program."""
		print("Byee sir")

if __name__ == "__main__":
	mycmd().cmdloop()
