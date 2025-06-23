import json
import xml.etree.ElementTree as ET


filename = 'HR365TSClients.json'
xml_array = [
        '<Field Name="GID" ID="{01a8c173-4806-4bcb-8ed0-9ddf3f1b288b}" DisplayName="GID"  Type="Text"></Field>',
        '<Field Name="CompanyDetails" ID="{a386f60f-189e-4867-900e-d20050d9ebcf}" DisplayName="CompanyDetails" Type="Note"></Field>',
        '<Field Name="BillingData" ID="{bb98c392-6998-4869-9ba4-e3b6bd1dc901}" DisplayName="BillingData" Type="Note"></Field>',
        '<Field Name="ContactData" ID="{e03a7dc7-6bb8-44f3-b849-5d886aaf17ce}" DisplayName="ContactData" Type="Note"></Field>',
        '<Field Name="Status" ID="{e103dcb6-5e05-46d7-a2e6-6470a407d975}" DisplayName="Status" Type="Text"></Field>',
        '<Field Name="Archived" ID="{fd5732da-d592-4f60-8bb2-ac27fdb31cd9}" DisplayName="Archived" Type="Text"></Field>',
        '<Field Name="CustomFields" ID="{1b244b88-269b-4ff2-8e6c-a75d5153f307}" DisplayName="CustomFields" Type="Note"></Field>',
        '<Field Name="Deleted" ID="{edb63870-c8f7-4194-b4f5-1b3e10ad3022}" DisplayName="Deleted" Type="Text"></Field>',
        '<Field Name="DocumentDetails" ID="{ebd0c961-9b70-4805-a070-b6147df0672f}" DisplayName="DocumentDetails" Type="Note"></Field>',
        '<Field Name="Source" ID="{ce16f873-4f93-4c67-b17b-bda3e95a79b3}" DisplayName="Source" Type="Text"></Field>',
      ]
required_fields = ['Name', 'ID', 'DisplayName', 'Type']
converted_data = []
id_set = set()
duplicate_ids = []
print("Xml length is: ", len(xml_array))

for xml in xml_array:
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        print(xml)
        continue

    field_dict = {}
    missing_fields = []

    for req_field in required_fields:
        value = root.get(req_field)
        if value is not None:
            field_dict[req_field] = value
        else:
            missing_fields.append(req_field)

    mult_value = root.get('Mult')
    if mult_value is not None:
        field_dict['Mult'] = mult_value

    id_value = field_dict.get('ID')
    if id_value and field_dict.get('Name'):
        if id_value in id_set:
            duplicate_ids.append(id_value)
        else:
            id_set.add(id_value)
            converted_data.append(field_dict)

    if missing_fields:
        id_value = root.get('ID', 'N/A')
        print(f"Missing fields for ID '{id_value}' {xml}")

with open(filename, 'w') as json_file:
    json.dump(converted_data, json_file, indent=4)

print(f"Data has been converted and saved to '{filename}'")
print("Json length is: ", len(converted_data))

if duplicate_ids:
    print("Duplicate IDs found:", ", ".join(duplicate_ids))
else:
    print("No duplicate IDs found.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # required_fields = ['Name', 'ID', 'DisplayName', 'Type']

# converted_data = []
# print("Xml length is: ",len(xml_array))

# for xml in xml_array:
#     try:
#         root = ET.fromstring(xml)
#     except ET.ParseError as e:
#         print(f"Error parsing XML: {e}")
#         print(xml)
#         continue

#     field_dict = {}
#     missing_fields = []

#     for req_field in required_fields:
#         value = root.get(req_field)
#         if value is not None:
#             field_dict[req_field] = value
#         else:
#             missing_fields.append(req_field)

#     mult_value = root.get('Mult')
#     if mult_value is not None:
#         field_dict['Mult'] = mult_value

#     if field_dict.get('ID') and field_dict.get('Name'):
#         converted_data.append(field_dict)

#     if missing_fields:
#         id_value = root.get('ID', 'N/A')
#         display_name = root.get('DisplayName', 'N/A')
#         print(f"Missing fields for ID '{id_value}' (DisplayName: '{display_name}'): {', '.join(missing_fields)}")

# with open(filename, 'w') as json_file:
#     json.dump(converted_data, json_file, indent=4)

# print(f"Data has been converted and saved to '{filename}'")
# print("Json length is: ",len(converted_data))


# // setSettingsValue
# // setLoginUserValues
# // setEmployeeOnboardList
# // setStandardtaskvalue
# // setEmailTemplatesValues

# // setDocumentValues
# // setCustomIds
# // TaskTemplatevalues
# // TaskTemplateMastervalues