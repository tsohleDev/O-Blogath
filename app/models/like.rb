require './app/models/application_record'
class Like < ApplicationRecord
  belongs_to :user, class_name: 'User', foreign_key: 'user_id'
  belongs_to :post, class_name: 'Post', foreign_key: 'post_id'

  before_create :increment_user_likecounter
  before_destroy :decrement_user_likecounter

  private

  def increment_user_likecounter
    post.increment(:likes_counter).save
  end

  def decrement_user_likecounter
    post.decrement(:likes_counter).save
  end
end
