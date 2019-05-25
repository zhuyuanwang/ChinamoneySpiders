from urllib import request
import re,os

f = open('pdfurl.txt','r',encoding='utf-8')

for i in f:
    i = i.strip()
    pdfname = i.split('	')[0]
    pdfurl= i.split('	')[-1]
    contentId = i.split('=')[1].replace('&priority','')

    def auto_down(i,pdfname):
        try:
            if os.path.exists('PDFData/'+pdfname + '.pdf'):
                request.urlretrieve(pdfurl,'PDFData/'+pdfname + '_' + contentId + '.pdf')
            else:
                request.urlretrieve(pdfurl, 'PDFData/' + pdfname + '.pdf')
        except request.ContentTooShortError:
            print('Network conditions is not good.Reloading.')
            auto_down(i,'PDFData/'+pdfname + '.pdf')

    auto_down(i,pdfname)
