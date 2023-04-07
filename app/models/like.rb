require './app/models/application_record'
class Like < ApplicationRecord
  belongs_to :user
  belongs_to :post

  before_create :increment_user_likecounter
  before_destroy :decrement_user_likecounter

  private

  def increment_user_likecounter
    user.increment(:likecounter).save
  end

  def decrement_user_likecounter
    user.decrement(:likecounter).save
  end
end
