require 'rails_helper'

RSpec.describe 'User', type: :system do
  before(:all) do
    @user1 = User.create(name: 'John Mikaer Doe',
                         photo: 'https://avatars.githubusercontent.com/u/74411135?s=400&u=ab8a7e4c6500ab7f1e058755215e500e82f0821a&v=4',
                         bio: 'Teacher from Mexico.')
    @user2 = User.create(name: 'Lillian Mia Doe',
                         photo: 'https://avatars.githubusercontent.com/u/74411135?s=400&u=ab8a7e4c6500ab7f1e058755215e500e82f0821a&v=4',
                         bio: 'Teacher from Mexico.')

    @users = [@user1, @user2]
  end

  it 'displays usernames of all users' do
    visit '/users' # Visit the users index page
    @users.each do |user|
      expect(page).to have_text(user.name)
    end
  end

  it 'displays images of all users' do
    visit '/users'
    @users.each do |user|
      expect(page).to have_selector("img[src='#{user.photo}']")
    end
  end

  it 'displays the number of posts each user has written' do
    visit '/users'
    @users.each do |user|
      expect(page).to have_text("Number of posts: #{user.posts_counter}")
    end
  end

  it 'redirects to the user\'s show page when you click on a user' do
    visit '/users'
    click_on @user1.id
    expect(page).to have_current_path("/users/#{@user1.id}")
  end
end
