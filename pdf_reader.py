from PyPDF2 import PdfFileReader

# add pdf filepath
pdf_fr = PdfFileReader(stream="/Users/KeeganLaptop/OneDrive/Whittier College/Rock History Rockin Out/Week02/Who Were the Harlem Hellfighters.pdf")
# select pdf page to extract text from
page_one = pdf_fr.getPage(0)
# create string object to be used in the call to Polly
page_text = page_one.extractText()
