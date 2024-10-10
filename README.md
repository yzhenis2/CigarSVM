# Cigar score prediction using Support Vector Machines(SVM)

## Use cigar reviews and apply SVM to predict the cigar score above or below of scores 90/100 and 95/100

This project is a score prediction of a  cuban cigar based on a review from Cigar Aficianado and Cigar Insider. 

Cigaraficionado provides their own score scale that ranges 70-100. The description is such:

95–100 Classic

90–94 Outstanding

80–89 Very good to excellent

70–79 Average to good commercial quality

Below 70 Don’t waste your money.

Both 90 and 95 were used as cut-off point. If cigars were guessed to be above cut-off point, they were marked as (1), otherwise (0) label is assigned. 
All previous tests of the same cigar by both Cigaraficionado and CigarInsider are on separate webpages and can be identified by the issue date of the review, 
the example above is dated on October 10,2023. When searching for a particular cigar, the results will show all previous test scores as separate instances

Keywords or attributes that are prominent in 90+ score cigars were extracted and then used to classify cigars in the dataset with and without Natural Language Processing (NLP).

The whole dataset size is 3026 data points. The data was shuffled and split into 5, thus making it 5-fold cross validation. 

## Statistical Metrics

TP: The real condition is true (1) and predicted as true (1); 90+ or 95+ cigar correctly classified as 90+ or 95+ cigar;
TN: The real condition is false (-1) and predicted as false (-1); 89- or 94- cigar correctly classified as 89- or 94- cigar;
FP: The real condition is false (-1) but predicted as true (1); 89- or 94- cigar incorrectly classified as 90+ or 95+ cigar;
FN: The real condition is true (1) but predicted as false (-1); 90+ or 95+ cigar incorrectly classified as 89- or 94- cigar;
The above values were used to calculate Accuracy, Precision and Recall. Accuracy provides proportion of all correctly classified cigars, and calculated such:

Accuracy= (TP+TN)/(TP+TN+FP+FN) (1)

The 5-fold Cross-Validation yields the following results.

Cut-off point &emsp;&nbsp;| &emsp; Accuracy

95+ w/ NLP &emsp; &nbsp; |   &emsp;      [0.99009901 0.99173554 0.99173554 0.99173554 0.99008264]

95+ w/o NLP &emsp;  | &emsp;   [0.99009901 0.99173554 0.99173554 0.99173554 0.99008264]

90+ w/ NLP &emsp; &nbsp; |  &emsp;      [0.53135314 0.52396694 0.53719008 0.51239669 0.53884298]

90+ w/o NLP &emsp; |  &emsp;  [0.54290429 0.54380165 0.54214876 0.52231405 0.54214876]
