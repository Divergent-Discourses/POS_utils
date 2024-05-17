AcTib Setup for Apple M1 Computers:

1.	So far, I only managed to get the pipeline working on Linux, and not on a Windows VM. Starting from nothing, on my Mac laptop, here’s what I did:

  a.	Download a Linux OS emulator and the latest version of Ubuntu as the chosen OS. 

  b.	From the command line, ensure the following:

    i.	The latest python version is at least 3.x.x, with the command python --version

    ii.	Store all python modules in a virtual environment. First, ensure that your python version has the capacity to create virtual environments with the following command: sudo apt install python3 python3-venv

    iii.	Create a virtual environment with python3 -m venv virtual-environment-name 

    iv.	Activate the venv with source virtual-environment-name/bin/activate

    v.	pip install the following core dependencies:

      1.	numpy
      2.	pandas
      3.	botok
      4.	pyewts
      5.	nltk
      6.	BeautifulSoup4

    vi.	In the Linux command line, run the following commands:
    
      1.	sudo apt install timbl
      2.	sudo apt install mbt

    vii.	Install Git with sudo apt install git
    
    viii.	Navigate to the directory where you want the AcTib code to be stored and clone with git clone http://github.com/lothelanor/actib/ 
    
    ix.	Now, you can follow the instructions in the AcTib documentation to run the preprocessing -> pos-directory pipeline. 
