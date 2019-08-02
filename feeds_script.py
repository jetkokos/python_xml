import xml.etree.ElementTree as ET

tree1 = ET.parse('feed/nmarket.xml')
root1 = tree1.getroot()

tree2 = ET.parse('feed/topnlab.xml')
root2 = tree2.getroot()



# =============================================================================
# #Adding new strings to xml with Host, phone etc
# for elem in root2:
#     manager = ET.SubElement(elem, 'Manager')
#     manager.text = 'Vlad'
#     host = ET.SubElement(elem, 'Host')
#     host.text = 'Favour'
#for elem in root2[1]:
#    print(elem, elem.text)
# =============================================================================
    

#Creating output.xml 


#Creating attributes "target" and "formatVersion"
outputRoot = ET.Element("Ads", {"target": "Avito.ru", "formatVersion": "3"})

#Filling new list with Ad from root2
i = 0 
for ad in root2:
    outputRootAd = ET.SubElement(outputRoot, "Ad")
    for adProperty in root2[i]:
        outputRootAd.append(adProperty) 
    i += 1  
        


    
  
    
#for i in outputRootAd:
 #   print(str(i) + ' ' + str(i.text))




   


outputTree = ET.ElementTree(outputRoot)
file = outputTree.write('output.xml', 'UTF-8')
