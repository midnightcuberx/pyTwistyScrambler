from os import path

curr_dir = path.dirname(path.realpath(__file__))

def trim(func):
	def trimmed_func():
		return func().strip()
	return trimmed_func

#------------------------------------------------------------------------------

with open(path.join(curr_dir, 'js_resources/mathlib.js')) as f:
	MATHLIB_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/cross.js')) as f:
	CROSS_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/scramble_333_edit.js')) as f:
	SCRAMBLE_333_SRC = f.read()