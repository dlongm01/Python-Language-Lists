alfa=[[' *** ','*   *','*   *','*****','*   *','*   *','*   *'],['**** ','*   *','*   *','**** ','*   *','*   *','**** '],[' *** ','*   *','*    ','*    ','*    ','*   *',' *** '],['**** ','*   *','*   *','*   *','*   *','*   *','**** '],['*****','*    ','*    ','**** ','*    ','*    ','*****'],['*****','*    ','*    ','**** ','*    ','*    ','*    '],[' *** ','*   *','*    ','*    ','*  **','*   *',' *** '],['*   *','*   *','*   *','*****','*   *','*   *','*   *'],['***',' * ',' * ',' * ',' * ',' * ','***'],['    *','    *','    *','    *','*   *','*   *',' *** '],['*   *','*  * ','* *  ','**   ','* *  ','*  * ','*   *'],['*    ','*    ','*    ','*    ','*    ','*    ','*****'],['*   *','** **','* * *','* * *','*   *','*   *','*   *'],['*   *','*   *','**  *','* * *','*  **','*   *','*   *'],[' *** ','*   *','*   *','*   *','*   *','*   *',' *** '],['**** ','*   *','*   *','**** ','*    ','*    ','*    '],[' *** ','*   *','*   *','*   *','* * *','*  * ',' ** *'],['**** ','*   *','*   *','**** ','* *  ','*  * ','*   *'],[' *** ','*   *','*    ',' *** ','    *','*   *',' *** '],['*****','  *  ','  *  ','  *  ','  *  ','  *  ','  *  '],['*   *','*   *','*   *','*   *','*   *','*   *',' *** '],['*   *','*   *','*   *','*   *','*   *',' * * ','  *  '],['*   *','*   *','*   *','* * *','* * *','** **','*   *'],['*   *','*   *',' * * ','  *  ',' * * ','*   *','*   *'],['*   *','*   *',' * * ','  *  ','  *  ','  *  ','  *  '],['*****','    *','   * ','  *  ',' *   ','*    ','*****']]
lnames=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Put the letters into a dictionary
#using these lists

bigletters_d={}

for i in range(len(lnames)):
    bigletters_d[lnames[i]] = alfa[i]
