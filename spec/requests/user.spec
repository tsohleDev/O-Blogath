require 'rails_helper'

RSpec.describe 'Users', type: :request do
  describe 'GET /' do
    before(:example) do
      get '/'
    end

    it 'renders a successful response' do
      expect(response).to be_successful
    end

    it 'contains the correct text' do
      expect(response.body).to include('A list of all users')
    end
  end

  describe 'GET /users/:id' do
    before(:example) do
      get '/users/1'
    end
    it 'renders a successful response' do
      expect(response).to be_successful
    end

    it 'contains the correct text' do
      expect(response.body).to include('A user with id 1')
    end
  end
end
