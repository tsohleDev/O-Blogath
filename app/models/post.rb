require './app/models/application_record'
class Post < ApplicationRecord
  belongs_to :author, class_name: 'User', foreign_key: 'author_id'

  before_create :increment_user_postcounter
  before_destroy :decrement_user_postcounter

  private

  def increment_user_postcounter
    author.increment(:posts_counter).save
  end

  def decrement_user_postcounter
    author.decrement(:posts_counter).save
  end
end
