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
    

#Adding new items from NMARKET feed

outputRoot = ET.Element('Ads')





for ad in root2[3]:
    outputAd = outputRoot.append(ad)
    #outputAd.text = ad.text
    print(ad.text)




   


outputTree = ET.ElementTree(outputRoot)