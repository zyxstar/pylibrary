
import os
outfile=open("combin.txt",'w')
for (thisDir, subsHere, filesHere) in os.walk(os.path.abspath(os.path.dirname(__file__))):
    for f in filesHere:
        thefile=os.path.join(thisDir, f)
        if os.path.isfile(thefile):
            if os.path.splitext(thefile)[1] in ['.sql']:
                infile=open(thefile,'r')
                outfile.write(infile.read())
                outfile.write("\r\n")
                infile.close()
                
outfile.close()