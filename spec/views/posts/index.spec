require 'rails_helper'
RSpec.describe 'Post', type: :system do
  before(:all) do
    @user = User.create(name: 'John Doe',
                        photo: 'https://avatars.githubusercontent.com/u/74411135?s=400&u=ab8a7e4c6500ab7f1e058755215e500e82f0821a&v=4',
                        bio: 'Teacher from Mexico.')
    post1 = Post.create(author: @user, title: 'Hello1', text: 'This is my first post')
    post2 = Post.create(author: @user, title: 'Hello2', text: 'This is my first post')
    post3 = Post.create(author: @user, title: 'Hello3', text: 'This is my first post')
    @posts = [post1, post2, post3]
    @comments = Comment.all
  end
  it "can see the user's profile picture" do
    visit "/users/#{@user.id}/posts"
    expect(page).to have_selector("img[src='#{@user.photo}']")
  end

  it "can see the user's username" do
    visit "/users/#{@user.id}/posts"
    expect(page).to have_text(@user.name)
  end

  it 'can see the number of posts the user has written' do
    visit "/users/#{@user.id}/posts"
    expect(page).to have_text("Number of posts: #{@user.posts_counter}")
  end

  it 'can see a post title' do
    visit "/users/#{@user.id}/posts"
    @posts.each do |post|
      expect(page).to have_text(post.title)
    end
  end

  it 'can see a post body' do
    visit "/users/#{@user.id}/posts"
    @posts.each do |post|
      expect(page).to have_text(post.text[0..99])
    end
  end

  it 'can see the first comments on a post' do
    visit "/users/#{@user.id}/posts"
    first_comment = Comment.create(post: @posts[0], author_id: @user.id, text: 'first comment')
    Comment.create(post: @posts[0], author_id: @user.id, text: 'second comment')
    visit "/users/#{@user.id}/posts"
    expect(page).to have_text(first_comment.text)
  end

  it 'can see how many comments a post has' do
    visit "/users/#{@user.id}/posts"
    expect(page).to have_text('Comments:')
  end

  it 'can see how many likes a post has' do
    visit "/users/#{@user.id}/posts"
    expect(page).to have_text('Likes:')
  end 

  it 'can see the pagination' do
    visit "/users/#{@user.id}/posts"
    expect(page).to have_text('Pagination')
  end

  it 'redirects to the post page when the user clicks on the post title' do
    visit "/users/#{@user.id}/posts"
    
    post = @posts[0]
    click_on post.title
    expect(page).to have_current_path("/users/#{@user.id}/posts/#{post.id}")
  end
end
