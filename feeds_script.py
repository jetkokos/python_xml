import xml.etree.ElementTree as ET


tree1 = ET.parse('feed/corrected/feed_nmarket.xml')
root1 = tree1.getroot()

tree2 = ET.parse('feed/corrected/feed_topnlab.xml')
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
    
#Editing root1 to required options
#root1.remove(root1[0])
#print(root1[0])

#Creating output.xml 


#Creating attributes "target" and "formatVersion"
outputRoot = ET.Element("Ads", {"target": "Avito.ru", "formatVersion": "3"})
outputTree = ET.ElementTree(outputRoot)


xmlns = str(root1.tag.split('}')[0] + '}')
#Filling new list with Ads from root1
for i, ad in enumerate(root1, start = 1):
    
    #Generating nodes for tags besides "generation-date"  
    if ad.tag != xmlns + 'generation-date':
        outputRootAd = ET.SubElement(outputRoot, "Ad")
        ident = ET.SubElement(outputRootAd, "Id")
        ident.text = ad.get("internal-id")
        
        Category = ET.SubElement(outputRootAd, "Category")
        Category.text = ad.find(xmlns + 'category').text
        
        #DateEnd
        
        AdStatus = ET.SubElement(outputRootAd, "AdStatus")
        AdStatus.text = 'Free'
        
        OperationType = ET.SubElement(outputRootAd, "OperationType")
        OperationType.text = ad.find(xmlns + 'type').text
        
        PropertyRights = ET.SubElement(outputRootAd, "PropertyRights")
        PropertyRights.text = 'Посредник'
        
        Address = ET.SubElement(outputRootAd, "Address")
        country = ad.find(xmlns + 'location').find(xmlns + 'country').text
        localityName = ad.find(xmlns + 'location').find(xmlns + 'locality-name').text
        subLocalityName = ad.find(xmlns + 'location').find(xmlns + 'sub-locality-name').text
        addr = ad.find(xmlns+ 'location').find(xmlns + 'address').text
        Address.text = country + ', ' + localityName + ', ' + subLocalityName + ', ' + addr
        
        Latitude = ET.SubElement(outputRootAd, "Latitude")
        Latitude.text = ad.find(xmlns + 'location').find(xmlns + 'latitude').text
        
        Longitude = ET.SubElement(outputRootAd, "Longitude")
        Longitude.text = ad.find(xmlns + 'location').find(xmlns + 'longitude').text
        
        Rooms = ET.SubElement(outputRootAd, "Rooms")
        Rooms.text = ad.find(xmlns + 'rooms').text
        
        Floor = ET.SubElement(outputRootAd, "Floor")
        Floor.text = ad.find(xmlns + 'floor').text
        
        Floors = ET.SubElement(outputRootAd, "Floors")
        Floors.text = ad.find(xmlns + 'floors-total').text
        
        HouseType = ET.SubElement(outputRootAd, "HouseType")
        HouseType.text = ad.find(xmlns + 'building-type').text
        
        LivingSpace = ET.SubElement(outputRootAd, "LivingSpace")
        LivingSpace.text = ad.find(xmlns + 'living-space').find(xmlns + 'value').text
        
        Square = ET.SubElement(outputRootAd, "Square")
        Square.text = ad.find(xmlns + 'area').find(xmlns + 'value').text
        
        Description = ET.SubElement(outputRootAd, "Description")
        Description.text = ad.find(xmlns + 'description').text
        
        CompanyName = ET.SubElement(outputRootAd, "CompanyName")
        CompanyName.text = 'Компания "ФАВОР"'
        
        ManagerName = ET.SubElement(outputRootAd, "ManagerName")
        ManagerName.text = 'Дильдина Галина'
        
        EMail = ET.SubElement(outputRootAd, "EMail")
        EMail.text = 'galina@favorestate.ru'
        
        ContactPhone = ET.SubElement(outputRootAd, "ContactPhone")
        ContactPhone.text = '+7 (921) 940-80-92'
        
        Price = ET.SubElement(outputRootAd, "Price")
        Price.text = ad.find(xmlns + 'price').text
        
        Images = ET.SubElement(outputRootAd, "Images")
        Image = ET.SubElement(Images, "Image")
        Image_url = ad.find(xmlns + 'image').text
        Image.set('url', Image_url)
 
       
 
#Filling new list with Ad from root2

for i, ad in enumerate(root2, start = 0):
    outputRootAd = ET.SubElement(outputRoot, "Ad")
    for adProperty in root2[i]:
        outputRootAd.append(adProperty) 
    i+=1
        
# =============================================================================
# for i, elem in enumerate(outputRoot):
#     print(elem.tag)
#     for prop in outputRoot[i]:
#         print("---" + prop.tag + '| ' + prop.text)
# =============================================================================

   


file = outputTree.write('output.xml', 'UTF-8', True)
