import urllib.request
import xml.dom.minidom as minidom

def get_data(xml_url):
    web_file = urllib.request.urlopen(xml_url)
    #данные, что доступны по ссылке, теперь в виде файла у нас 
    return web_file.read()


def get_currencies_dictionary(xml_content):
    dom = minidom.parseString(xml_content)
    dom.normalize()

    elements = dom.getElementsByTagName("Valute")
    #если что, название не выборочно, это название узла Valute
    # если напишем иначе, ничего не найдётся
    
    currency_dict = {}

    #перебор всех узлов Valute 
    for node in elements:
        #перебор дочерних узлов нынешнего узла Valute 
        for child in node.childNodes:
            
            if child.nodeType == 1:

                #курс 
                if child.tagName == 'Value':
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))

                #название валюты        
                if child.tagName == 'CharCode':
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data
                        
        currency_dict[char_code] = value
        
    return currency_dict

def print_dict(dict):
    for key in dict.keys():
        print(key, dict[key])


if __name__ == '__main__':
    
    xml_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    
    currency_dict = get_currencies_dictionary(get_data(xml_url))
    '''print_dict(currency_dict)'''

