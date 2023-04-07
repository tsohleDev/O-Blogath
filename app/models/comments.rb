require './app/models/application_record'
class Comment < ApplicationRecord
    belongs_to :user
    belongs_to :post

    before_create :increment_user_commentcounter
    before_destroy :decrement_user_commentcounter

    private

    def increment_user_commentcounter
        user.increment(:commentcounter).save
    end

    def decrement_user_commentcounter
        user.decrement(:commentcounter).save
    end
end