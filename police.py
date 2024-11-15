from flask import Flask,redirect,url_for,render_template,jsonify,request
app=Flask(__name__)
data=[]
@app.route('/dept')
def dept():
    return render_template('index.html')
@app.route('/allinfo',methods=['GET'])
def info():
    return jsonify(data)
@app.route('/addcategory',methods=['GET','POST'])
def add():
    if request.method=='POST':
        id1=request.form['id']
        name=request.form['name']
        category=request.form['category']
        transfer=request.form['transfer']
        data.append({'id':id1,'name':name,'category':category,'transfer':transfer})
        return redirect(url_for('dept'))
    return render_template('add.html')
@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        id1=request.form['id']
        name=request.form['name']
        category=request.form['category']
        transfer=request.form['transfer']
        for i in data:
            if i['id']==id1:
                i['name']=name
                i['category']=category
                i['transfer']=transfer
        return redirect(url_for('dept'))
    return render_template('update.html')
@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=='POST':
        id1=request.form['id']
        for i in data:
            if i['id']==id1:
                data.remove(i)
        return redirect(url_for('dept'))
    return render_template('delete.html')
app.run(use_reloader=True)


