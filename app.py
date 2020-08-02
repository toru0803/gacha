import sqlite3

from flask import Flask, render_template, request, redirect

app = Flask(__name__)



#トップページへのルートです
@app.route("/")
def template():
    return render_template("index.html")


#ここがゆるっとボタンを押したときのルートです
@app.route("/relux")
def dbtest():
  conn = sqlite3.connect('todogacha.db')
  c = conn.cursor()
  c.execute("select plan_name,plan_details,plan_details2,url from plan_yurutto ORDER BY random() LIMIT 3")
  user_info = c.fetchall()
  c.close()
  return render_template("result.html", user_info = user_info,) 


#ここがしゃきっとボタンを押したときのルートです
@app.route("/fine")
def finetest():
  conn = sqlite3.connect('todogacha.db')
  c = conn.cursor()
  c.execute("select plan_name, plan_details,plan_details2,url from plan_shakitto ORDER BY random() LIMIT 3")
  user_info = c.fetchall()
  c.close()
  return render_template("result.html", user_info = user_info,)


#ここがやってみようボタンを押したときのルートです
@app.route("/try")
def trytest():
  conn = sqlite3.connect('todogacha.db')
  c = conn.cursor()
  c.execute("select plan_name,plan_detail,plan_detail2,url from plan_yattemiyo ORDER BY random() LIMIT 3")
  user_info = c.fetchall()
  c.close()
  return render_template("result.html", user_info = user_info,)


#ここが押さないでボタンを押したときのルートです押さないではDB未完成
@app.route("/osanaide")
def osanaide():
  conn = sqlite3.connect('todogacha.db')
  c = conn.cursor()
  c.execute("select plan_name,plan_details,plan_details2,url from plan_osunayo ORDER BY random() LIMIT 3")
  user_info = c.fetchall()
  c.close()
  return render_template("result.html", user_info = user_info,)


# 404エラーがでた場合
@app.errorhandler(404)
def page_not_found(error):
  return render_template("404error.html")



# 投稿機能
@app.route("/suggestion", methods=["POST"])
def suggestion():
  plan_name = request.form.get("plan_name")
  plan_detail = request.form.get("plan_detail")
  conn = sqlite3.connect("todogacha.db")
  c = conn.cursor()
  c.execute("insert into suggestion values (?, ?)", (plan_name, plan_detail))
  conn.commit()
  c.close()
  return render_template("thanks.html")








if __name__=="__main__":
    app.run(debug=True)



