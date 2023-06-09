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

  def new
    post = Post.new
    user = current_user
    post.author = user
    respond_to do |format|
      format.html { render :new, locals: { post:, user: } }
    end
  end

  def create
    @user = current_user
    @post = Post.new(post_params)
    @post.author = @user

    respond_to do |format|
      if @post.save
        flash[:success] = 'Post saved successfully'
        # redirect to root
        format.html { redirect_to user_posts_path(@user) }
      else
        flash[:error] = 'Post failed to save'
        format.html { render :new, locals: { post: @post, user: @user } }
      end
    end
  end

  def like
    @post = Post.find(params[:id])
    @like = current_user.likes.new
    @like.post_id = params[:id]

    # check if user already liked the post
    return unless @like.save

    if @like.save
      redirect_to user_post_path(@like.post.author_id, @like.post), notice: 'like added successfully'
    else
      redirect_to user_post_path(@post.author_id, @post), notice: 'Failed to add a like'
    end
  end

  private

  def post_params
    params.require(:post).permit(:author_id, :title, :text)
  end
end
