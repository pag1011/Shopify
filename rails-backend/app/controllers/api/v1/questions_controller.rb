require_relative "../../application_controller"

class Api::V1::QuestionsController < ApplicationController
  require "net/http"
  require "json"

  def create
    python_service = ENV.fetch("PYTHON_SERVICE_URL", "http://127.0.0.1:8000")
    python_url = URI("#{python_service}/predict")

    http = Net::HTTP.new(python_url.host, python_url.port)
    http.read_timeout = 10

    request = Net::HTTP::Post.new(
      python_url,
      { "Content-Type" => "application/json" }
    )

    request.body = {
      question: params[:question],
      store_id: params[:store_id]
    }.to_json

    response = http.request(request)

    render json: JSON.parse(response.body)
  rescue => e
    render json: { error: e.message }, status: 500
  end
end
