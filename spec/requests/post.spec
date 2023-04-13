require 'rails_helper'

RSpec.describe 'Posts', type: :request do
  describe 'GET /users/:id/posts' do
    before(:example) do
      get '/users/1/posts'
    end

    it 'renders a successful response' do
      expect(response).to be_successful
    end

    it 'contains the correct text' do
      expect(response.body).to include('A list of all posts')
    end
  end

  describe 'GET users/:id/posts/:id' do
    before(:example) do
      get '/users/1/posts/1'
    end
    it 'renders a successful response' do
      expect(response).to be_successful
    end

    it 'contains the correct text' do
      expect(response.body).to include('A post with id 1')
    end
  end
end
