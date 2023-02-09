import matplotlib.pyplot as plt
import cv2
from pytesseract import Output
import re
import json
from train_ocr import train_ocr_core
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def plot_gray(image):
    plt.figure(figsize=(16, 10))
    return plt.imshow(image, cmap='Greys_r')


def plot_rgb(image):
    plt.figure(figsize=(16, 10))
    return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


def find_amounts(text):
        amounts = re.findall(r'\d+\.\d{2}\b', text)
        #amounts = re.findall(r'[0-9]+(,[0-9]+)*,?', text)
        floats = [float(amount) for amount in amounts]
        unique = list(dict.fromkeys(floats))
        return unique


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def ocr_core(filename,tempfile):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image






    amounts = find_amounts(text)

    grandtotal = max(amounts)



    #invoiceno = re.findall(r'((?<=Invoice No: ).{17})', text)
    #invoiceran = re.findall(r'((?<=Invoice No:).{17})', text)
    #invoicenum = re.findall(r'((?<=Invoice No :).{17})', text)
    #invoicenumber = re.findall(r'((?<=Invoice Number ).{17})', text)
    #invoicetry = re.findall(r'((?<=Invoice Number# ).{17})', text)
    #invoicewell = re.findall(r'((?<=Invoice Number#).{17})', text)
    #invoicesome = re.findall(r'((?<=Invoice Number #).{17})', text)



   # with open(tempfile) as f:
        #data = json.load(f)
    #invoicesomething = re.findall(rf'((?<='+reg+').{4,17}\s)', text)

    #with open(f"invoice_templates/{tempfile}", encoding='utf-8', errors='ignore') as json_data:
        #data = json.load(json_data, strict=False)

    path = f'./{tempfile}.json'
    # Check whether the specified
    # path exists or not
    isExist = os.path.exists(path)
    print(isExist)

    # with open(f'{path}', 'rt') as myfile:  # Open lorem.txt for reading text
    # contents = myfile.read()  # Read the entire file to a string





    if(isExist):
        f = open(f'{path}')
        data = json.load(f)






    else:
        print("upload again")






    invoice_number = list(data[0].values())
    vendor_name = list(data[1].values())
    invoice_date = list(data[2].values())
    invoice_bill = list(data[3].values())
    #dynamic_invoice_value1 = list(data[4].values())[0][0]
    #dynamic_invoice_value2 = list(data[4].values())[0][1]
    #dynamic_invoice_value3 = list(data[4].values())[0][2]






    invoice_number1 = listToString(invoice_number)
    vendor_name1 = listToString(vendor_name)
    invoice_date1 = listToString(invoice_date)
    invoice_bill1 = listToString(invoice_bill)
    #dynamic_invoice_value_con1 = listToString(dynamic_invoice_value1)
    #dynamic_invoice_value_con2 = listToString(dynamic_invoice_value2)




    #dynamic_invoice_value_con3 = listToString(dynamic_invoice_value3)
    #dynamic_invoice_value_con4 = listToString(dynamic_invoice_value4)




    ino = re.findall(rf'((?<=' + invoice_number1 + ').{4,17}\s)', text)
    iname = vendor_name1
    idate = re.findall(rf'((?<=' + invoice_date1 + ').{4,17}\s)', text)
    ibill = re.findall(rf'((?<=' + invoice_bill1 + ').{4,17}\s)', text)
    #dynamic1 = re.findall(rf'((?<=' + dynamic_invoice_value_con1 + ').{4,17}\s)', text)
    #dynamic2 = re.findall(rf'((?<=' + dynamic_invoice_value_con2 + ').{4,17}\s)', text)
   #dynamic3 = re.findall(rf'((?<=' + dynamic_invoice_value_con3 + ').{4,17}\s)', text)
    #dynamic4 = re.findall(rf'((?<=' + dynamic_invoice_value_con4 + ').{4,17}\s)', text)



    try:
      dynamic_invoice_value1 = list(data[4].values())[0][0]
      dynamic_invoice_value2 = list(data[4].values())[0][1]
      dynamic_invoice_value3 = list(data[4].values())[0][2]
      dynamic_invoice_value4 = list(data[4].values())[0][3]
      dynamic_invoice_value5 = list(data[4].values())[0][4]
      dynamic_invoice_value_con1 = listToString(dynamic_invoice_value1)
      dynamic_invoice_value_con2 = listToString(dynamic_invoice_value2)
      dynamic_invoice_value_con3 = listToString(dynamic_invoice_value3)
      dynamic_invoice_value_con4 = listToString(dynamic_invoice_value4)
      dynamic_invoice_value_con5 = listToString(dynamic_invoice_value5)
      dynamic1 = re.findall(rf'((?<=' + dynamic_invoice_value_con1 + ').{4,17}\s)', text)
      dynamic2 = re.findall(rf'((?<=' + dynamic_invoice_value_con2 + ').{4,17}\s)', text)
      dynamic3 = re.findall(rf'((?<=' + dynamic_invoice_value_con3 + ').{4,17}\s)', text)
      dynamic4 = re.findall(rf'((?<=' + dynamic_invoice_value_con4 + ').{4,17}\s)', text)
      dynamic5 = re.findall(rf'((?<=' + dynamic_invoice_value_con5 + ').{4,17}\s)', text)


      return ("Invoice Number:",ino , "Invoice Vendor:", iname,"Invoice Date:", idate, "Invoice Total:",ibill,dynamic_invoice_value_con1, dynamic1,dynamic_invoice_value_con2, dynamic2, dynamic_invoice_value_con3,dynamic3,dynamic_invoice_value_con4,dynamic4, dynamic_invoice_value_con5,dynamic5);

    except IndexError:
        print("IndexError: list index out of range")



    try:
      dynamic_invoice_value1 = list(data[4].values())[0][0]
      dynamic_invoice_value2 = list(data[4].values())[0][1]
      dynamic_invoice_value3 = list(data[4].values())[0][2]
      dynamic_invoice_value4 = list(data[4].values())[0][3]

      dynamic_invoice_value_con1 = listToString(dynamic_invoice_value1)
      dynamic_invoice_value_con2 = listToString(dynamic_invoice_value2)
      dynamic_invoice_value_con3 = listToString(dynamic_invoice_value3)
      dynamic_invoice_value_con4 = listToString(dynamic_invoice_value4)

      dynamic1 = re.findall(rf'((?<=' + dynamic_invoice_value_con1 + ').{4,17}\s)', text)
      dynamic2 = re.findall(rf'((?<=' + dynamic_invoice_value_con2 + ').{4,17}\s)', text)
      dynamic3 = re.findall(rf'((?<=' + dynamic_invoice_value_con3 + ').{4,17}\s)', text)
      dynamic4 = re.findall(rf'((?<=' + dynamic_invoice_value_con4 + ').{4,17}\s)', text)



      return ("Invoice Number:",ino , "Invoice Vendor:", iname,"Invoice Date:", idate, "Invoice Total:",ibill,dynamic_invoice_value_con1, dynamic1,dynamic_invoice_value_con2, dynamic2, dynamic_invoice_value_con3,dynamic3,dynamic_invoice_value_con4,dynamic4);

    except IndexError:
        print("IndexError: list index out of range")









    try:
      dynamic_invoice_value1 = list(data[4].values())[0][0]
      dynamic_invoice_value2 = list(data[4].values())[0][1]
      dynamic_invoice_value3 = list(data[4].values())[0][2]

      dynamic_invoice_value_con1 = listToString(dynamic_invoice_value1)
      dynamic_invoice_value_con2 = listToString(dynamic_invoice_value2)
      dynamic_invoice_value_con3 = listToString(dynamic_invoice_value3)

      dynamic1 = re.findall(rf'((?<=' + dynamic_invoice_value_con1 + ').{4,17}\s)', text)
      dynamic2 = re.findall(rf'((?<=' + dynamic_invoice_value_con2 + ').{4,17}\s)', text)
      dynamic3 = re.findall(rf'((?<=' + dynamic_invoice_value_con3 + ').{4,17}\s)', text)



      return ("Invoice Number:",ino , "Invoice Vendor:", iname,"Invoice Date:", idate, "Invoice Total:",ibill,dynamic_invoice_value_con1, dynamic1,dynamic_invoice_value_con2, dynamic2, dynamic_invoice_value_con3,dynamic3);

    except IndexError:
        print("IndexError: list index out of range")

    try:
        dynamic_invoice_value1 = list(data[4].values())[0][0]
        dynamic_invoice_value2 = list(data[4].values())[0][1]


        dynamic_invoice_value_con1 = listToString(dynamic_invoice_value1)
        dynamic_invoice_value_con2 = listToString(dynamic_invoice_value2)


        dynamic1 = re.findall(rf'((?<=' + dynamic_invoice_value_con1 + ').{4,17}\s)', text)
        dynamic2 = re.findall(rf'((?<=' + dynamic_invoice_value_con2 + ').{4,17}\s)', text)


        return ("Invoice Number:",ino , "Invoice Vendor:", iname,"Invoice Date:", idate, "Invoice Total:",ibill,dynamic_invoice_value_con1, dynamic1,dynamic_invoice_value_con2, dynamic2);

    except IndexError:
        print("IndexError: list index out of range")

    try:
        dynamic_invoice_value1 = list(data[4].values())[0][0]


        dynamic_invoice_value_con1 = listToString(dynamic_invoice_value1)


        dynamic1 = re.findall(rf'((?<=' + dynamic_invoice_value_con1 + ').{4,17}\s)', text)


        return ("Invoice Number:",ino , "Invoice Vendor:", iname,"Invoice Date:", idate, "Invoice Total:",ibill,dynamic_invoice_value_con1, dynamic1);

    except IndexError:
        print("IndexError: list index out of range")





    return ("Invoice Number:",ino , "Invoice Vendor:", iname,"Invoice Date:", idate, "Invoice Total:",ibill)









"""
dynamic_invoice_value_con3 = listToString(dynamic_invoice_value3)
      dynamic3 = re.findall(rf'((?<=' + dynamic_invoice_value_con3 + ').{4,17}\s)', text)

      dynamic_invoice_value4 = list(data[4].values())[0][3]
      dynamic_invoice_value_con4 = listToString(dynamic_invoice_value4)
      dynamic4 = re.findall(rf'((?<=' + dynamic_invoice_value_con4 + ').{4,17}\s)', text)

      dynamic_invoice_value5 = list(data[4].values())[0][4]
      dynamic_invoice_value_con5 = listToString(dynamic_invoice_value5)
      dynamic5 = re.findall(rf'((?<=' + dynamic_invoice_value_con5 + ').{4,17}\s)', text)

"""