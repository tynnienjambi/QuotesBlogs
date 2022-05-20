
from flask import flash, render_template, redirect,url_for
from app.main import main
from ..models import Blog, User
from app.request import get_random_qoutes
from app.main.forms import BlogForm, SubscribeForm
from app import db
from flask_login import login_required



@main.route('/')
@main.route('/index')
def index():
    '''
    View function that sets index page
    '''
    title = 'Home'
    random_quote = get_random_qoutes()
    # blogs = Blog.query.all()
    return render_template('index.html', title=title, quotes=random_quote)



@main.route('/blog', methods=['GET','POST'])
@login_required
def createblog():
    '''
    View function that sets blog page
    '''
    title = 'Create blog'
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(blog_title=form.blog_title.data, blog_post=form.blog_post.data,)
        db.session.add(blog)
        db.session.commit()
        flash('Blog has been created')
        return redirect(url_for('main.createblog'))
    all_blogs = Blog.query.all()
    return render_template('blog.html', title=title, form=form, all_blogs=all_blogs)


@main.route('/blog/delete/<int:id>')
def delete_blog_post(id):
    '''
    Function to delete blog post
    '''
    blog = Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()
    flash(f'Blog {id} deleted')
    return redirect(url_for('main.createblog'))

@main.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    '''
    Function to subscribe users
    '''
    form = SubscribeForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flash('You have been added to our newsletter email list')
        return redirect(url_for('main.subscribe'))
    return render_template('subscribe.html', form=form )