require 'rails_helper'

RSpec.describe 'Users', type: :system do
  let!(:first_user) do
    User.create(name: 'Tom',
                photo: 'https://avatars.githubusercontent.com/u/74411135?s=400&u=ab8a7e4c6500ab7f1e058755215e500e82f0821a&v=4',
                bio: 'Teacher from Mexico.')
  end
  let!(:second_user) do
    User.create(name: 'Lilly',
                photo: 'https://cdn.vectorstock.com/i/preview-1x/10/70/super-cool-pizza-character-cartoon-vector-15811070.webp',
                bio: 'Teacher from Poland.')
  end
  let!(:users) { [first_user, second_user] }

  let(:posts) do
    [
      [Post.create(author: users[0], title: 'Hey1', text: 'This is my first post'),
       Post.create(author: users[0], title: 'Hey2', text: 'This is my first post')],
      [Post.create(author: users[1], title: 'Hey3', text: 'This is my first post')]
    ]
  end

  it 'username of all users' do
    users.each do |user|
      visit "/users/#{user.id}"
      expect(page).to have_text(user.name)
    end
  end

  it 'can see the number of posts the user has written' do
    users.each do |user|
      visit "/users/#{user.id}"
      expect(page).to have_text("Number of posts: #{user.posts_counter}")
    end
  end

  it 'can see the user profile picture' do
    users.each do |user|
      visit "/users/#{user.id}"
      expect(page).to have_selector("img[src='#{user.photo}']")
    end
  end

  it 'user and shows bio' do
    users.each do |user|
      visit "/users/#{user.id}"
      expect(page).to have_text('Bio')
      expect(page).to have_text(user.bio.to_s)
    end
  end

  it 'see how many likes it has' do
    users.each_with_index do |user, i|
      visit "/users/#{user.id}"
      posts[i].each do |post|
        expect(page).to have_text("Likes: #{post.likes_counter}") if post.likes_counter > 0
      end
    end
  end

  it 'see how many comments it has' do
    users.each_with_index do |user, i|
      visit "/users/#{user.id}"
      posts[i].each do |post|
        expect(page).to have_text("Comments: #{post.comments_counter}") if post.comments_counter > 0
      end
    end
  end

  it 'see the body of the post' do
    users.each_with_index do |user, i|
      visit "/users/#{user.id}"
      posts[i].each do |post|
        expect(page).to have_text(post.text[0...99].to_s) if post.likes_counter > 0
      end
    end
  end

  it 'see title of post' do
    users.each_with_index do |user, i|
      visit "/users/#{user.id}"
      posts[i].each do |post|
        expect(page).to have_text("Likes: #{post.title}") if post.likes_counter > 0
      end
    end
  end

  it 'can see a button that lets me view all of a user posts' do
    visit "/users/#{first_user.id}"
    expect(page).to have_text('See all posts')
  end
end
