#!/usr/bin/python
import os
import subprocess

# ############################### FUNCTIONS ########################################
def fileList():
    """
    Assign to fileList the list of the files contained by the local directory
    """
    l1 = os.listdir(os.getcwd())
    for fiLe in enumerate(l1):
        if "py" in fiLe[1] or ".xls" in fiLe[1]:
            pass
        else:
            print fiLe


def header(arg1):
    output = arg1[0].split()
    counter = 0
    limit = 3
    head = []
    while counter <= limit:
        increase = counter + 1
        if counter < 2:
            head.append(output[counter] + "_" + output[increase])
        else:
            head.append(output[counter] + "_" + output[increase] + " " + output[4])
        counter = counter + 2
    return str(head).replace("['", "").replace("', '", " ").replace("']", "").replace(" ", "\t")


def data(arg1):
    cont = ""
    for x in arg1:
        if x[0] == " ":
            cont = str(cont) + "\n" + x[1:].replace("  ", " ").replace(" ", "\t")
        else:
            cont = str(cont) + "\n" + x.replace("  ", " ").replace(" ", "\t")
    return cont


# ############################ FUNCTIONS # END #####################################
subprocess.call(["clear"])
scalcPath = raw_input(('###########################################################\n'
                       'Please, specify the path in which I can find scalc software\n'
                       'example: /usr/bin/scalc\n'
                       '###########################################################\n'
))
print "######################"
fileList()

inputFileName = raw_input(('##############################################\n'
                           'Write below the file name you want to process:\n'
                           '##############################################\n'
))  # inputFileName to pass input file
print "######################"
# ##############################
inputFile = open(inputFileName, mode='r')  # inputFile containing allows to access to file content
fileContent = inputFile.read()  # fileContent containing the file content
cont2List = [element.replace("\t", " ") for element in fileContent.split("\n")]
"""
cont2List converts file content into a list in which every element
is constituted by a single line from the orginal input file

"""
header = header(cont2List)
dAta = [str(element).replace("\t", " ") for element in cont2List[1:] if element != ""]
"""
dAta variable stored the elements from cont2List but header
"""
# ###################################
inputFile.close()  # close the file
# ###################################
# ###################################
if os.path.isfile("output.xls"):  # check output file existence
    os.remove("output.xls")
# ##############################
output1 = "output.xls"  # output1 to store first output file
# ##############################
contentList = []  # intialize list
# ##############################
outFile = open(output1, mode='w')
outFile.write(header + data(dAta))
outFile = open(output1, mode='r')
outCont = outFile.read()
outFile.close()  # close the file
# ###################################
subprocess.call([scalcPath, output1])
