class CreateLikes < ActiveRecord::Migration[7.0]
  def change
    create_table :likes do |t|

      t.timestamps
    end

    add_reference :likes, :user, index: false
    add_reference :likes, :post, index: true
  end
end
