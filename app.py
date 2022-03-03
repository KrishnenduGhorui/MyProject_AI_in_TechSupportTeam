from flask import Flask, render_template, request
import pickle
import numpy as np
import TextPreProcessing

app = Flask(__name__)

model = pickle.load(open('model_mnb.pkl', 'rb'))
le_Component = pickle.load(open('le_Component.pkl', 'rb'))
le_Label = pickle.load(open('le_Label.pkl', 'rb'))
vect_tfidf=pickle.load(open('vect_tfidf.pkl', 'rb'))


dict_AssigneeTeam={0:'Leader',1:'L1',2:'L2',3:'Governance',4:'Datastage',5:'CloudOps',6:'Infra',7:'Cp4d',8:'K8',9:'ERDM',10:'Gov_Kyndryl',11:'DataDiscovery',12:'Others'}

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Summary = str(request.form['Summary'])
        Description=str(request.form['Description'])
        Compnt = request.form['Component']
        Component=str(le_Component.transform([Compnt])[0])
		
        Lbl=request.form['Label']
        Label=str(le_Label.transform([Lbl])[0])
		
		
        Issue_Type=request.form['Issue_Type']
        if(Issue_Type=='Service_Request'):            
            Issue_Type_Service_Request=1
            Issue_Type_Question=0
            Issue_Type_SR_Approvals=0
        elif(Issue_Type=='Question'):
            Issue_Type_Service_Request=0
            Issue_Type_Question=1
            Issue_Type_SR_Approvals=0
        elif(Issue_Type=='SR_Approvals'):
            Issue_Type_Service_Request=0
            Issue_Type_Question=0
            Issue_Type_SR_Approvals=1
        else:
            Issue_Type_Service_Request=0
            Issue_Type_Question=0
            Issue_Type_SR_Approvals=0

        Text=Summary+' '+Description+' '+Component+' '+Label+' '+str(Issue_Type_Question)+' '+str(Issue_Type_Service_Request)+' '+str(Issue_Type_SR_Approvals)
        Text=TextPreProcessing.textclean(Text)
        
        text_encoded=vect_tfidf.transform([Text]).toarray()
        prediction=model.predict(text_encoded)
        output=str(dict_AssigneeTeam[prediction[0]])		
        
        return render_template('index.html',prediction_text="This should be assigned to "+ output+" Team")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)