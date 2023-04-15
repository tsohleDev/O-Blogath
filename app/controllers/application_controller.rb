class ApplicationController < ActionController::Base
  def current_user
    # set the current user to the first user in the database
    @current_user ||= User.first
  end
end
