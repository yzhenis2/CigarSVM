# This project is using the computational wine wheel to extract the attributes from reviews

import xlrd
import pandas as pd
import string
from string import digits

# step1 : two files are needed, first file contains the raw data reviews; second file contains the computational wine wheel(either cww2.0 or cww3.0)
Review = "E:/academia/fall23/ADM/midterm/cigarreview_full.xls"
CWW = "E:/academia/fall23/ADM/midterm/compcigarwheel_small.xls"
reviews = xlrd.open_workbook(Review)
CWWS = xlrd.open_workbook(CWW)
review = reviews.sheet_by_index(0)
cww = CWWS.sheet_by_index(0)

# step2: assign lists of name and score to variables, the column numbers are depending on the specific excel file
normalized_name = list(set(cww.col_values(3,1,cww.nrows)))
specific_name = list(set(cww.col_values(2,1,cww.nrows)))
wine_name = review.col_values(0,1,review.nrows)
score = review.col_values(1,1, review.nrows)



# step3 : create dataframe to contain results
df = pd.DataFrame(columns=normalized_name, index=wine_name)
word_extracted = pd.DataFrame(columns=[4,5], index=wine_name)
category = ['WRAPPER', 'SMOKE', 'TOBACCO', 'AROMA','CHARACTER','BODY','TEXTURE', 'DRAW','CARAMEL','SPICY',
            'MICROBIOLOGICAL','OVERALL', 'NUTTY', 'EARTHY', 'WOODY', 'FRUITY','FLORAL']
subcategory = ['wrapper', 'smoke', 'TOBACCO', 'AROMA', 'CHARACTER', 'BODY', 'TEXTURE', 'DRAW', 'CARAMEL', 'SPICE',
               'OTHER', 'EXPERIENCE', 'EARTHY', 'NUTTY', 'WOODY', 'FINISH', 'RESINOUS', 'DRIED FRUIT', 'FLAVOR/DESCRIPTORS',
               'PIGTAIL', 'FLORAL', 'CITRUS']

#category = list(set(cww.col_values(0,1,cww.nrows)))
#subcategory = list(set(cww.col_values(1,1,cww.nrows)))
cate = pd.DataFrame(columns=category, index=wine_name)
subCat = pd.DataFrame(columns=subcategory, index=wine_name)



# step4: split the specific_name into two type -- 'single word name' or 'word group name'
longword = []
shortword = []
for i in range(len(specific_name)):
    if specific_name[i].__contains__(" "):
        longword.append(specific_name[i])
    elif specific_name[i].__contains__("-"):
        longword.append(specific_name[i])
    else:
        shortword.append(specific_name[i])
longword.sort(key=len,reverse=True)

# step5: create variables for different values
containLong = []        # contains the long words that are extracted
containShort = []       # contains the short words that are extracted
wordCountR = []         # contains the amount of attributes that are extracted
phraseCountR = []       # contains the amount of all words in the review

# step6 : using cww to parse the attributes from reviews
for i in range(1, review.nrows):        # loop through the reviews data rows
    result1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0]        # variable holds the counts of category attributes
    result2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # variable holds the counts of subcategory attributes    a = []              # a contains the extracted long words
    a = []              # a contains the extracted long words
    b = []              # b contains the extracted short words
    d = 0               # d contains the counts of the extracted long words
    e = 0               # e contains the counts of the extracted short words
    o = 0

    c1 = review.cell_value(i, 6).upper()                                    # c1 contains the review in uppercase
    if c1.__contains__("RRIES"):
        c1 = c1.replace("RRIES", "RRY")                                     # replace all the rries to rry for the plurals
    for j in range(len(longword)):
        if c1.__contains__(longword[j]):
            a.append(longword[j])
            c1 = c1.replace(longword[j] , " ")                              # extract all the longwords and collect them, and replace them with a space in the reivew
            for x in range(1, cww.nrows-1):
                if longword[j] == cww.cell_value(x,2):
                    df[cww.cell_value(x,3)].iloc[i-1] = 1
                    for y in range(len(category)):
                        if category[y] == cww.cell_value(x, 0):
                            result1[y] += 1                                 # calculate the counts of the category based on the extracted longwords
                    for d in range(len(subcategory)):
                        if subcategory[d] == cww.cell_value(x,1):
                            result2[d] += 1                                 # calculate the counts of the subcategory based on the extracted longwords
    d = len(a)
    containLong.append(a)

    c1 = c1.replace("/", " ")
    c1 = c1.replace("-", " ")
    c1 = c1.translate(str.maketrans('', '', string.punctuation))
    c1 = c1.translate(str.maketrans('', '', digits))
    c1 = c1.split()                     # replace all the special characters with space and split the review into an array
    for g in range(len(shortword)):
        if c1.__contains__(shortword[g]):
            b.append(shortword[g])
            o = o + 1                                                               # extract the short words
            for x in range(1, cww.nrows-1):
                if shortword[g] == cww.cell_value(x,2):
                    df[cww.cell_value(x,3)].iloc[i-1] = 1
                    for y in range(len(category)):
                        if category[y] == cww.cell_value(x,0):
                            result1[y] += 1                                         # calculate the counts of the category based on the extracted longwords
                    for l in range(len(subcategory)):
                        if subcategory[l] == cww.cell_value(x,1):
                            result2[l] += 1                                         # calculate the counts of the subcategory based on the extracted longwords
    containShort.append(b)
    e = len(c1) + len(a)

    wordCountR.append(d+o)
    phraseCountR.append(e)

    for e in range(len(category)):
        cate[category[e]].iloc[i-1] = result1[e]
    for h in range(len(subcategory)):
        subCat[subcategory[h]].iloc[i-1] = result2[h]

# step7 : assign the class label based on the grades
grade=[]
for i in range(len(score)):
    if score[i] < 90.0:
        grade.append('0')
    else:
        grade.append('1')

# building the excel file for the word counting
word_extracted.insert(0, "PhraseCount", phraseCountR)
word_extracted.insert(1, "ExtractedCount", wordCountR)
word_extracted.insert(2, "Extracted LWords", containLong)
word_extracted.insert(3, "Extracted SWords", containShort)
word_extracted.to_excel("new_wordcount_cigarwheel_90.xlsx")

# build the excel file for the normalized_name dataset
df.insert(0, "score", grade)
df.to_excel('WS_cigarwheel_90.xlsx')



