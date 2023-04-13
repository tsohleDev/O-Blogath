class PostsController < ApplicationController
  def index
    @posts = Post.all
    @user = User.find(params[:user_id])
  end

  def show
    @post = Post.find(params[:id])
    @comments = @post.comments
    @likes = @post.likes
    return unless @post.nil?

    redirect_to '/error?message=Post+not+found'
  end
end
