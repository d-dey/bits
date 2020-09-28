# -*- coding: utf-8 -*-
"""
Assignment PS7

"""


class interPretr:

 def __init__(self):
        self.vertices=[] 
        self.edges=[[],[]] 
        self.composeArry=[]
        self.promptArry=[]
        self.uniqueCand=[]  
        self.uniqueLang=[]
        #self.graph=[]
        self.output = open("outputPS7.txt", "w")
        self.indirectrans = ''

        self.pyfile = ''
        self.verticeslen = 0
        self.hireList = []
        
        
 def edgeCreation(self): #Create the adjacency matrix
    
    self.verticeslen = len(self.vertices)
    self.edges=[[None for i in range(self.verticeslen)] for j in range(self.verticeslen)]
    
    for i in range(self.verticeslen):
        for j in range(self.verticeslen):
            self.edges[i][j] = 0
    
    candpostn = -1
    langpostn = -1
    for i in range(len(self.composeArry)):
        candidate = self.composeArry[i][0]
        candpostn = self.findCandpos(candidate)
        for language in self.uniqueLang:
            if language in self.composeArry[i][1:]:
                langpostn = self.findLangpos(language)
                self.edges[candpostn][langpostn] = 1
                self.edges[langpostn][candpostn] = 1
                
 def findCandpos(self,candidate):   #Find the array position of candidate
    for i in range(len(self.vertices)):
        if self.vertices[i]==candidate:
            break
    return i
    
 def findLangpos(self,language):    #Find the array position of candidate
    keyisfound = False
    for i in range(len(self.vertices)):
        if self.vertices[i]==language:
            keyisfound=True
            break
    if keyisfound is True:
        return i
    else:
        return -1

            
 def uniqueCandidates(self):    #List out the unique canidates
    self.uniqueCand=[]
    for pline in self.composeArry:
        plinecand = pline[0]
        if plinecand not in self.uniqueCand:
            self.uniqueCand.append(plinecand)
    return self.uniqueCand

 def uniqueLanguages(self):     #List out the unique languages
    self.uniqueLang=[]
    for pline in self.composeArry:
        plinelang = pline[1:]
        for lang in plinelang:
            if lang not in self.uniqueLang:
                self.uniqueLang.append(lang)                    
    return self.uniqueLang




 def removeCovLang(self,ck,tbcl):    #Used to construct Q3 minimum hire list
    candKey = ck
    tobeCov = tbcl
    #print(tobeCov)
    tobeCovLang = []
    for l in range(self.verticeslen):
        if self.edges[candKey][l] != 1 and self.vertices[l] not in self.uniqueCand:
            #if len(tobeCov) == 0:
             #tobeCovLang.append(self.vertices[l])
            if self.vertices[l] in tobeCov:
             tobeCovLang.append(self.vertices[l]) 
            
    return tobeCovLang 
    
 def getInterpreterRank(self):    #Used to construct Q3 minimum hire list
    
    interpreterRank=[]
    langknown=0
    candlangtuple= ()
    for candkey in range(0,len(self.uniqueCand)):
        for langkey in range(len(self.uniqueCand), self.verticeslen):
            if self.edges[candkey][langkey]==1:
                langknown += 1
            candlangtuple = (candkey, langknown)
        langknown=0
        interpreterRank.append(candlangtuple)
    return interpreterRank
    
    

 def maxInterpreterRank(self, ir , tbcl):   #Used to construct Q3 minimum hire list
    tobeCov = tbcl
    knwl = []
    #temp = 0
    langtemp = 0
    interpreterRank=ir
    temprank = ()
    if len(interpreterRank) >= 1:
        for rank in interpreterRank:
          langknown = 0  
          knwl = self.knowlanguage(rank[0])
          for i in range(len(knwl)):  
            if knwl[i] in tobeCov:
              langknown = langknown + 1 
          if langknown > langtemp:      
           temprank = rank
           langtemp = langknown
    #print(temprank)      
    return temprank

 def displayHireList(self):   #Question no 3 function
        count = 0
        hirelist = []
        reqCovLang = self.uniqueLang
        tempcovLang = []
        interpreterRank = self.getInterpreterRank()
        #print(interpreterRank)
        for i in range(len(interpreterRank)): 
         #print(interpreterRank)   
         maxrank = self.maxInterpreterRank(interpreterRank,reqCovLang)
         #print(maxrank)
         candKey = maxrank[0]
         #print(candKey)
         interpreterRank.remove(maxrank)  
         reqCovLang =  self.removeCovLang(candKey,reqCovLang)
         if len(reqCovLang) == 0:  
          hirelist.append(self.printHirelist(candKey))
          count=count+1
          break
         if tempcovLang != reqCovLang:
          count = count + 1
          tempcovLang = reqCovLang
          hirelist.append(self.printHirelist(candKey))
         else:
          pass
        self.output.write('\n\n')
        self.output.write("--------Function displayHireList--------")
        self.output.write('\n')
        self.output.write("No of candidates required to cover all languages: %s" %count)
        for i in range(len(hirelist)):
         self.output.write('\n')   
         self.output.write(hirelist[i])

 def printHirelist(self,candKey):  #Used to construct Q3 minimum hire list
  languageList = ''   
  for l in range(len(self.uniqueCand), self.verticeslen):
     if self.edges[candKey][l] == 1:
      languageList+= ' / ' + self.vertices[l]
  return(self.vertices[candKey] + languageList) 

 def knowlanguage(self,candKey):   #Used to construct Q3 minimum hire list
  languageList = []  
  for l in range(len(self.uniqueCand), self.verticeslen):
     if self.edges[candKey][l] == 1:
      languageList.append(self.vertices[l])
  return languageList    


 def readApplications(self,pyfile):   #Question no. 1 function
    inputfile = open(pyfile,"r")
    listArry = []
    for y in inputfile:
            y = y.strip()
            listArry = y.split(' ')
            candidate = []
            
            for i in range(len(listArry)):        
                if listArry[i] != '/':
                  candidate.append(listArry[i])  
                
            
            self.composeArry.append(candidate)
    
    inputfile.close()
    
    self.vertices = self.uniqueCandidates() + self.uniqueLanguages()
    self.edgeCreation()
    #return self.composeArry
    if len(listArry) == 0:
        self.output.write("No Record found")
        self.output.close()
    else:    
        self.readpromtFile('promptsPS7.txt')


 
 def readpromtFile(self,pyprompfile):   #To read the prompt file and redirect to the corresponding functions
  inputPrompt = open(pyprompfile,"r")
  for i in inputPrompt:
   i = i.strip()
   listArry = i.split(' ')
   promptin = []
   for j in range(len(listArry)):
     if listArry[j] != ':':
      promptin.append(listArry[j])         
            
   self.promptArry.append(promptin)
   
  inputPrompt.close()
  
  
  self.showAll()
 
  for y in range(len(self.promptArry)):
        prompt = self.promptArry[y][0]
        if prompt in "showMinList":
         self.displayHireList()
         #pass   
        elif prompt in "searchLanguage:":   
         self.displayCandidates(self.promptArry[y][1])
        elif prompt in "DirectTranslate:":
         self.findDirectTranslator(self.promptArry[y][1],self.promptArry[y][2])
        elif prompt in "TransRelation:":
         self.findTransRelation(self.promptArry[y][1],self.promptArry[y][2])
         pass
        else:
         self.output.write('\n\n')
         self.output.write("%s has no matching Prompt definition"%prompt)   
         pass
  self.output.close()
  
  
 def showAll(self):   #Question no. 2 function
        self.uniqueCand = self.uniqueCandidates()
        self.uniqueLang = self.uniqueLanguages()
        #self.output.write('\n')
        self.output.write('Total no. of candidates: %s' %len(self.uniqueCand))
        self.output.write('\n')
        self.output.write('Total no. of languages: %s' %len(self.uniqueLang))
        self.output.write('\n\n')
        self.output.write('List of candidates: ')
        self.output.write('\n')
        for cand in self.uniqueCand:
            self.output.write('\n')
            self.output.write(cand)
        self.output.write('\n\n')
        
        self.output.write('List of languages: ')
        self.output.write('\n')
        for lang in self.uniqueLang:
            self.output.write('\n')
            self.output.write(lang)
            
            

 def displayCandidates(self, lang):   #Question no. 4 function
        #print('\n')
        self.output.write('\n\n')
        self.output.write("--------Function Display Candidates --------")
        self.output.write('\n')
        self.output.write("SearchLanguage: %s" %lang)
        
        
        langKey = self.findLangpos(lang) 
        canditransl = []
        if (langKey==-1):
            #self.output.write('\n')
            self.output.write('\n\n')
            self.output.write("No candidate knows %s language." %lang)
        else:
            for i in range(len(self.vertices)):
                if (self.edges[i][langKey]==1):
                    canditransl.append(self.vertices[i])
            #self.output.write('\n') 
            self.output.write('\n\n')
            self.output.write('List of candidates who can speak %s:\n%s ' %(lang, ('\n').join(canditransl)) )    
        self.output.write('\n')
        #self.output.write('\n')
        
        
        
        
 def findDirectTranslator(self, langA, langB):  #Question no. 5 function
        self.output.write('\n')
        self.output.write("--------Function findDirectTranslator --------")
        self.output.write('\n')
        self.output.write("Language A: %s" %langA)
        self.output.write('\n')
        self.output.write("Language B: %s" %langB)
        
        langApst = self.findLangpos(langA)
        langBpst = self.findLangpos(langB)
        
        if (langApst == -1 or langBpst == -1):
            self.output.write('\n')
            self.output.write("This language does not exist with any candidate, please select different languages. ")
            self.output.write('\n')
            return 0
        else:
            hastranslator = False
            
            translatorCands = []
            count = 0
            
            for i in range(len(self.vertices)):
                if (self.edges[i][langApst] == 1 and self.edges[i][langBpst] == 1):
                    self.output.write('\n')
                    self.output.write("Yes, %s can translate. " % self.vertices[i])
                    hastranslator = True
                    count+=1
                    translatorCands.append(self.vertices[i])
            
            if hastranslator is False:
                self.output.write('\n')
                self.output.write("Direct Translator: No" )
                self.output.write('\n')
                return 0
            else:
                self.output.write('\n')
                self.output.write("Total %d translator(s) can translate from %s to %s, and they are: %s." %(count, langA, langB, ', '.join(translatorCands)) )
                self.output.write('\n')
                return 1
        self.output.write('\n')       
        
 def findTransRelation(self, langA, langB):  #Question no. 6 function
           self.output.write('\n\n')
           self.output.write("--------Function findTransRelation --------")
           langApst = self.findLangpos(langA)
           langBpst = self.findLangpos(langB)
           #self.getPath(langApst,langBpst , '')
           self.output.write('\n')
           self.output.write("--------Unfinished --------")
           self.output.write('\n')
           self.output.write("--------Commented code works with less complex list --------")
           
 def getCandKnow(self, lang):   #Unused function. Created for the purpose Question. 6
     reqLanguage = lang
     translatorCands = []
     #print(reqLanguage)
     count = 0
     for i in range(len(self.vertices)):
                if self.edges[i][reqLanguage] == 1:
                    count = count +1
                    #print(i)
                    translatorCands.append(i)
     #print(count)               
     return translatorCands      
          
 def getPath(self,langA, langB , tempCand):   #Unused function. Created for the purpose Question. 6
     traverse = False
     RemoveCad = ''
     if tempCand != '':
      RemoveCad = tempCand
      self.indirectrans+= ' > ' + self.vertices[RemoveCad] + ' > '
     self.indirectrans+= self.vertices[langA] 
     SearchLang = langA
     listofCandAKey = self.getCandKnow(SearchLang)
     checklang = []
     requireCadlist = []
     for x in range(len(listofCandAKey)):
         if listofCandAKey[x] != RemoveCad:
             requireCadlist.append(listofCandAKey[x])      
     for i in range(len(requireCadlist)):
               langlistApos = []
               langlistA = self.knowlanguage(requireCadlist[i])
               for k in langlistA:
                   langlistApos.append(self.findLangpos(k))   
               for y in range(len(langlistApos)):
                   if langlistApos[y] != SearchLang:
                      checklang.append(langlistApos[y])      
               if langB in checklang:
                   self.indirectrans+= ' > ' + self.vertices[requireCadlist[i]]
                   print('Yes %s > %s'%(self.indirectrans,self.vertices[langB]))
                   traverse = True
                   break;
               else:
                  for j in range(len(checklang)):
                      tempCand = requireCadlist[i]
                      self.getPath(checklang[j],langB ,tempCand)
               if traverse == True:
                  break;         