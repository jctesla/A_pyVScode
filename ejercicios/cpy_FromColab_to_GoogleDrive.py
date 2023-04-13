# This code are de original for NoteBook's Colab.

# Mount your Google Drive to Colab, so you can access files in your Google Drive. 
from google.colab import drive
drive.mount('/content/drive')                   

# Replace 'file.txt' with the name of your file
from google.colab import files
firstFile = './sample_data/california_housing_test.csv'       # File de Origin q esta en el Colab.
secondFile = 'fileAnyOne.csv'                                 # Name file going to save in GoogleDrive.
pathh = '/content/drive/MyDrive/AnyOne/'                      # path destino del GoogleDrive.

with open(firstFile,'r') as firstfile, open(pathh + secondFile,'a') as secondfile:
	
	# read content from first file
	for line in firstfile:
			secondfile.write(line)                                  # append each line to destiny.
