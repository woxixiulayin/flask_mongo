from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from tumblelog.models import Post, Comment, Tieba_post_doc

posts = Blueprint('posts', __name__, template_folder='templates')

class ListView(MethodView):
    def get(self):
        posts = Tieba_post_doc.objects()
        return render_template('posts/list.html', posts=posts)

class DetailView(MethodView):
    def get(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        return render_template('posts/detail.html', post=post)

# Register the urls
posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('//', view_func=DetailView.as_view('detail'))