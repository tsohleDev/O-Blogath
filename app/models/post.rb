require './app/models/application_record'
class Post < ApplicationRecord
  belongs_to :author, class_name: 'User', foreign_key: 'author_id'
  has_many :comments, foreign_key: 'post_id'
  has_many :likes, foreign_key: 'post_id'

  before_create :increment_user_postcounter
  before_destroy :decrement_user_postcounter

  private

  def increment_user_postcounter
    author.increment(:posts_counter).save
  end

  def decrement_user_postcounter
    author.decrement(:posts_counter).save
  end

  def recent_comments
    comments.order(created_at: :desc).limit(5)
  end
end
