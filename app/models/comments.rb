require './app/models/application_record'
class Comment < ApplicationRecord
  belongs_to :user
  belongs_to :post

  before_create :increment_user_commentcounter
  before_destroy :decrement_user_commentcounter

  private

  def increment_user_commentcounter
    post.increment(:comments_counter).save
  end

  def decrement_user_commentcounter
    post.decrement(:comments_counter).save
  end
end
