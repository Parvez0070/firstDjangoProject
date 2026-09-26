#i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data={'name':'Parvez', 'webname':'textutils'}
    return render(request,"index.html",data)

def analyzer(request):  

    #getting text from Form: 
    djtext=request.POST.get('text','')   #using post methid instead of get to keep the url link in browser more clean...

    #Checking djtext:
    if djtext == '':
        analyzed="No text is entered!"
        purposes=[] 

    else:  
        #getting CheckBox Logic:
        rempunc=request.POST.get('rempunc','off')
        capfirst=request.POST.get('capfirst','off')
        remln=request.POST.get('remln','off')
        remspc=request.POST.get('remspc','off')
        charcnt=request.POST.get('charcnt','off')

        #setting default values for analyzed and purpose variable, if no checkbox is selected...
        analyzed="No action was selected!"
        purposes=[]   

        #checking CheckBox Conditions:
        #code for Remove Punctuation:
        if rempunc == "on":
            analyzed = ''
            purposes.append('Remove Punctuation')
            punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
            for x in djtext:
                if x not in punctuations:
                    analyzed += x
            
            djtext=analyzed      #updating djtext, if rempunc is on then this updated value will be used for next checkbox.

        #code for Capitalize First:      
        if capfirst == 'on':
            analyzed = ''
            purposes.append('Capitalize First')
            analyzed=djtext.title()
            djtext=analyzed     #updating djtext, if capfirst is on then this updated value will be used for next checkbox.

        #code for Extra Line Remove:
        if remln == 'on':
            analyzed = ''
            purposes.append('Extra Line Remove')

            #This line converts all newline formats into \n. Different system(win,mac,lynux) use different type of formats.
            djtext = djtext.replace('\r\n', '\n').replace('\r', '\n')  
            
            pre = ''
            for x in djtext:
                if x == '\n' and pre == '\n':
                    continue
                analyzed += x
                pre = x
            djtext=analyzed      #updating djtext, if remln is on then this updated value will be used for next checkbox.
        
        #code for Extra Space Remove:
        if remspc == 'on':
            analyzed = ''
            purposes.append('Extra Space Remove')

            for i,x in enumerate(djtext):
                if djtext[0] == ' ' or (djtext[i-1] == ' ' and djtext[i] == ' '):
                    continue
                analyzed += x
            djtext=analyzed      #updating djtext, if remspc is on then this updated value will be used for next checkbox.

        #code for Total Character Count:
        if charcnt == 'on':
            purposes.append('Total Character Count')

            for i,x in enumerate(djtext):
                pass
            analyzed=f"Total {i+1} character in : {djtext}."


    #joining all purpose items
    if purposes:
        purpose = ', '.join(purposes)
    else:
        purpose = "No purpose"

    #sending data to analyzed tempaltes:
    data2={'purpose':purpose, 'analyzed_text':analyzed}
    return render(request, "analyzed.html",data2)

