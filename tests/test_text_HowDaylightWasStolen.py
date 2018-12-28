import re
import sys
sys.path.append("..")
from text import *
import importlib
import os
import pdb
#----------------------------------------------------------------------------------------------------
pd.set_option('display.width', 1000)
#----------------------------------------------------------------------------------------------------

def createText():

    text = Text("../testData/harryMosesDaylight/daylight_1_4.eaf",
                "../testData/harryMosesDaylight/audioPhrases",
                grammaticalTermsFile=None,
                tierGuideFile="../testData/harryMosesDaylight/tierGuide.yaml")
    return(text)
    

def runTests(display=False):
    test_constructor()
    test_toHTML(display)

def test_constructor():

    print("--- test_constructor")

    text = createText()
    assert(text.validInputs())
    tbl = text.getTierSummary()
    assert(tbl.shape == (4,3))
    assert(list(tbl['key']) == ['speech', 'translation', 'morpheme', 'morphemeGloss'])
    assert(list(tbl['value']) == ['lushootseedSpeech', 'englishGloss', 'phonemicLushootseed', 'phonemicTranslation'])
    assert(list(tbl['count']) == [4, 4, 4, 4])

def test_toHTML(display=False):

    print("--- test_toHTML")
    
    text = createText()

    text.getLineAsTable(1)

    htmlText = text.toHTML()
    filename = "daylight.html"
    f = open(filename, "w")
    f.write(indent(htmlText))
    f.close()
    if(display):
       os.system("open %s" % filename)

if __name__ == '__main__':
    runTests()
