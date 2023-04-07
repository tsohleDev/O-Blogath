require './app/models/application_record'
class User < ApplicationRecord
  has_many :posts
  has_many :likes
  has_many :comments

  def recent_posts
    posts.order(created_at: :desc).limit(3)
  end

  # name must be present
  validates :name, presence: true

  # posts_count must be a integer and greater than or equal to 0
  validates :posts_counter, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
end
