class UsersController < ApplicationController
  # your code here
  def index
    @users = User.all
  end

  def show
    @user = User.find_by(id: params[:id])
    return unless @user.nil?

    # user not found
    # redirect to custom page or render custom view
    redirect_to '/error?message=User+not+found'
  end

  def error
    @message = params[:message]
  end

  def photo
    @user = User.find_by(id: params[:id])
    return unless @user.nil?

    # user not found
    # redirect to custom page or render custom view
    redirect_to '/error?message=User+not+found'
  end
end
