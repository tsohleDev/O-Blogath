require './app/models/application_record'
class Comment < ApplicationRecord
  belongs_to :user, class_name: 'User', foreign_key: 'author_id'
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

  #VALIDATIONS
  #text must not be blank. and must not exceed 100 characters.
  validates :text, presence: true, length: { maximum: 100 }
end
