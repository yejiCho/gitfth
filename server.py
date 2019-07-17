from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

articles = []
articles_num = 1
art = []

## HTML을 주는 부분
@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/post', methods=['POST'])
def post():
   global articles
   global articles_num

   url_receive = request.form['url_give']
   comment_receive = request.form['comment_give']
   name_receive = request.form['name_give']


   article = {'num':articles_num,'url':url_receive,'comment':comment_receive,'name':name_receive}
   art = {}
   articles_num = articles_num + 1

   articles.append(article)


   return jsonify({'result':'success'})

@app.route('/post', methods=['GET'])
def view():
   global articles
   return jsonify({'result':'success','articles':articles})


# @app.route('/test', methods=['GET'])
# def test_get():
#    # global 변수 name을 보여주기
#    return jsonify({'result':'success', 'name': name})

if __name__ == '__main__':
   app.run('127.0.0.1',port=5000,debug=True)