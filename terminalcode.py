import os
# process1 = os.system("py -m pytest --edge --html=report_edge.html --maximize -n=4 --screenshot ")
process2 = os.system("py -m pytest --safari --html=report_safari.html --screenshot ")
# process3 = os.system("py -m pytest --firefox --html=report_firefox.html --maximize -n=4 --screenshot ")