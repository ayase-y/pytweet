from flask import Flask,render_template,request,redirect,flash,session
from .app import app
from .database import db
import os
from .models.models import User,Post,Profile,Comments
from flask_login import login_user,LoginManager,login_required,current_user,logout_user
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/",methods=["GET","POST"])
def Index():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["email"]).first()
        if user is not None and request.form["email"] == user.username and request.form["password"] == user.password :
            login_user(user)
            return redirect("/dashboard")
        else :
            flash(u"Invalid Username or password","error")
            flash(u"Check your input Username or password","error2")
            return redirect("/")
    return render_template("login.html")


@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        user = User(fullname=request.form["fullname"],
                    username=request.form["email"],
                    password=request.form["password"])
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    return render_template("register.html")


@app.route("/dashboard",methods=["GET","POST"])
@login_required
def dashboard():
    title="Dashboard"
    return render_template("dashboard.html",title=title)


@app.route("/tweet",methods=["POST"])
@login_required
def tweet():
    post = Post(user_id=current_user.id,post=request.form["tweet"])
    db.session.add(post)
    db.session.commit()
    return redirect("/profile")


@app.route("/profile",methods=["GET","POST"])
@login_required
def profile():
    title="Tweet Page"
    if current_user:
        user = User.query.filter_by(id=current_user.id).first()
        posts = Post.query.order_by(Post.created_at.desc()).all()
        profile = Profile.query.filter_by(user_id=current_user.id).first()
        comments = Comments.query.order_by(Comments.created_at.desc()).all()
        return render_template("profile/profile.html",title=title,posts=posts,profile=profile,comments=comments,user=user)
    return redirect("/")


@app.route("/comment",methods=["POST"])
@login_required
def comment():
    if request.method == "POST":
        comment = Comments(
            user_id=current_user.id,
            comment=request.form["comment"],
            post_id=request.form["id"]
            )
        db.session.add(comment)
        db.session.commit()
        return redirect("/profile")
    return render_template("profile/profile.html")


@app.route("/about",methods=["GET","POST"])
@login_required
def about():
    if request.method == "POST":
        profile = Profile(
            user_id=current_user.id
            ,first_name=request.form["first_name"]
            ,second_name=request.form["second_name"]
            ,address=request.form["address"]
            ,occupation=request.form["occupation"]
            ,birth_day=request.form["birth_day"]
            ,skills=request.form["skills"]
            )
        db.session.add(profile)
        db.session.commit()
        return redirect("/profile")
    return render_template("profile/profile.html")


@app.route("/contacts")
@login_required
def contacts():
    title="Contacts"
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template("contacts/contacts.html",title=title,users=users)

@app.route("/viewprofile/<int:id>")
# @login_required
def viewprofile(id):
    user = User.query.filter_by(id=id).first()
    profile = Profile.query.filter_by(user_id=id).first()
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("profile/profile.html",user=user,posts=posts,profile=profile)


@app.route("/modals")
def modals():
    title="Modals"
    return render_template("modals.html",title=title)


# form
@app.route("/general")
def general():
    title="General Form"
    return render_template("general.html",title=title)


@app.route("/advanced")
def advanced():
    title="Advanced Form"
    return render_template("advanced.html",title=title)


@app.route("/editors")
def editors():
    title="Text Editors"
    return render_template("editors.html",title=title)


# table
@app.route("/simpletables")
def simpletables():
    title="Simple Tables"
    return render_template("simpletables.html",title=title)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))