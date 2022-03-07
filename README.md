# MyProject_Automation_in_TechSupportTeam

 
**Goal** - Making process automatic in Tech Support team by developing an automatic system with ML/DL models that can manage ticket/case raised by users for getting support, without any human intervention.
System will assign ticket to the corresponding responsible team, set the correct Label by processing text Summary and Description mentioned in the ticket by NLP and ML/DL algorithm.This will results support team’s function automatic, faster and error less and need of less man resource, ultimately saving cost.

**Responsibilities** -

* Collected data of resolved tickets from atlassian Jira tool’s service desk used for project work.
* Pre-processed data - 
  * Imputed missing data with other valid value ,  
  * Instead of individual ID of Assignee, having here AssigneeTeam name,the assignee person belongs to.This is required because, for a particular type of ticket,responsible         individual assignee may change over time but responsible assinee team doesn't change. This Assignee Team is target data.
  * For features Label and Component, all very less frequent values are replaced with a category like 'Lbl_others' and 'Component_others' respectively. 
  * There were some labels,component with different text value(or typo) but actually same label category, that handled by replacing using a mapping dictionary.
  * Encoded categorical data by LabelEncoder 
  * Cleaned text by NLTK, lemmatizing and removing stopwords   
  * Vectorized data by TfidfVectorizer 
  * Made data balanced by SMOTE
* Built and trained several ML models (Multinomial Naive Bayes, Random Forest Classifier, Support Vector Machine), DL modes (LSTM).
* Evaluated model’s performance by Confusion Matrix, Accuracy Score, classification report(Precision,recall,F1 score)
* Deployed the model performing best using Flask,Pickle.
