import numpy as np 
from astropy.table import Table

def main():
	# np.linspace
	# np.arange
	some_array = np.linspace(0,2*np.pi,1000) 
	x = np.linspace(0.2*np.pi, 1000)  
	y = np.sin(x)

	data_table = Table()
	data_table["x"] = x
	data_table["y"] = y

	data_table["x"].format = "{:.3f}"
	data_table["y"].format = "{:.3f}"

	print(data_table)



if __name__ == "__main__":
	main()