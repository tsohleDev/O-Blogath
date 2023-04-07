class CreateComments < ActiveRecord::Migration[7.0]
  def change
    create_table :comments do |t|
      t.text :text

      t.timestamps
    end

    add_reference :comments, :user, index: false
    add_reference :comments, :post, index: true
  end
end
