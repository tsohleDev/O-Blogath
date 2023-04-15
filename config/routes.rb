Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  resources :users, only: [:index, :show] do
    resources :posts, only: [:index, :show, :new, :create] do
      resources :comments, only: [:new, :create]
      resources :likes, only: [:create]
    end
  end

  root 'users#index'

  get '/error', to: 'users#error'

  post '/users/:user_id/posts/:post_id/comments', to: 'comments#create', as: 'create_post_comment'
  get '/users/:user_id/posts/:id/like', to: 'posts#like', as: 'like_post'
  get '/users/:user_id/posts/:id/unlike', to: 'posts#unlike', as: 'unlike_post'
end
