class PostsController < ApplicationController
  def index
    @posts = Post.all
  end

  def show
    @post = Post.find(params[:id])
    return unless @post.nil?

    redirect_to '/error?message=Post+not+found'
  end
end
