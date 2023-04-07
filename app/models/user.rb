require './app/models/application_record'
class User < ApplicationRecord
  has_many :posts
  has_many :likes
  has_many :comments
end
