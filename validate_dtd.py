from lxml import etree

# Load the DTD
with open("student.dtd", "rb") as dtd_file:
    dtd = etree.DTD(dtd_file)

# Parse the XML document
xml_doc = etree.parse("student.xml")

# Validate XML against DTD
if dtd.validate(xml_doc):
    print("XML is VALID according to the DTD.")
else:
    print("XML is INVALID according to the DTD.")
    print(dtd.error_log)